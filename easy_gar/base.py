"""Base classes."""

import itertools
import time
import random

from apiclient.discovery import build
from apiclient.errors import HttpError
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

import easy_gar


class ReportingAPI:
    """API class."""

    sampling_level = "DEFAULT"

    def _build_from_oauth_keys(self, secrets_path):
        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_path,
            scope=self._scopes,
            message=tools.message_if_missing(secrets_path),
        )

        # Prepare credentials, and authorize HTTP object with them.
        storage = file.Storage("analyticsreporting.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(http=httplib2.Http())

        # Build the analytics reporting v4 service object.
        self._reporting = build(
            "analytics",
            "v4",
            http=http,
            discoveryServiceUrl="https://analyticsreporting.googleapis.com/"
            "$discovery/rest",
        )

    def _build_from_service_account_keys(self, secrets_path):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            secrets_path, self._scopes
        )

        # Build the analytics reporting v4 service object.
        self._reporting = build("analyticsreporting", "v4", credentials=credentials)

    def __init__(
        self,
        view_id,
        secrets_path,
        secrets_type="oauth",
        scopes=("https://www.googleapis.com/auth/analytics.readonly",),
    ):
        """Init ReportingAPI object."""
        self._view_id = view_id
        self._scopes = scopes

        build = {
            "oauth": self._build_from_oauth_keys,
            "service": self._build_from_service_account_keys,
        }.get(
            secrets_type, None
        )

        if build is None:
            msg = "Invalid secrets_type; must be one of 'oauth' or 'service'"
            raise ValueError(msg)

        build(secrets_path)

    def _request_with_exponential_backoff(self, body):
        """Return Google Analytic Reporting API v4 reponse object."""
        errors = [
            "userRateLimitExceeded",
            "quotaExceeded",
            "internalServerError",
            "backendError",
        ]
        for n in range(0, 5):
            try:
                return self._reporting.reports().batchGet(
                    body={"reportRequests": [body]}
                ).execute()

            except HttpError as err:
                exception = err
                if err.resp.reason in errors:
                    time.sleep((2 ** n)) + random.random()
                else:
                    break

        raise exception

    def _get(
        self,
        sampling_level=None,
        start_date=None,
        end_date=None,
        metrics=None,
        dimensions=None,
        order_by=None,
        page_token=None,
        page_size=None,
    ):
        """Return Google Analytics Reporing API response object."""
        request_body = {
            "samplingLevel": sampling_level or self.sampling_level,
            "viewId": self._view_id,
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": metrics,
            "dimensions": dimensions,
            "pageSize": page_size and str(page_size) or "10000",
        }
        if page_token:
            request_body["pageToken"] = str(page_token)
        if order_by:
            request_body["orderBys"] = [obj() for obj in order_by]

        # attempt request using exponential backoff
        response = self._request_with_exponential_backoff(request_body)
        return response["reports"][0]

    def get_report(
        self,
        sampling_level=None,
        start_date="7daysAgo",
        end_date="today",
        metrics=None,
        dimensions=None,
        order_by=None,
        name=None,
    ):
        """Return an API response object reporting metrics for set dates."""
        if not dimensions:
            dimensions = [easy_gar.dimensions.date]

        # Create GA metric/dimensions objects
        _metrics = [metric() for metric in metrics]
        _dimensions = [dimension() for dimension in dimensions]

        # Get initial data
        response = self._get(
            sampling_level=sampling_level,
            start_date=start_date,
            end_date=end_date,
            metrics=_metrics,
            dimensions=_dimensions,
            order_by=order_by,
        )

        if response:
            rows = response["data"]["rows"]
            values = (tuple(row["metrics"][0]["values"]) for row in rows)
            row_dims = (tuple(row["dimensions"]) for row in rows)

            # Retrieve additional data if response is paginated
            while "nextPageToken" in response.keys():
                page_token = response["nextPageToken"]
                args = (start_date, end_date, _metrics, _dimensions, page_token)
                response = self._get(*args)
                if response:
                    rows = response["data"]["rows"]
                    new_values = (tuple(row["metrics"][0]["values"]) for row in rows)
                    new_dims = (tuple(row["dimensions"]) for row in rows)
                    values = itertools.chain(values, new_values)
                    row_dims = itertools.chain(row_dims, new_dims)

            # Set up report data (for pandas DataFrame)
            fieldnames = (metric.alias for metric in metrics)
            data = zip(fieldnames, zip(*values))
            indices = tuple(row_dims)
            names = tuple(dimension.alias for dimension in dimensions)
            index = pd.MultiIndex.from_tuples(indices, names=names)
            return Report(data, index, name)


class Metric:
    """Base Metric class."""

    def __init__(self, expression=None, alias=None, formatting_type=None):
        """Init Metric object."""
        self.expression = expression
        self.alias = alias
        self.formatting_type = formatting_type

    def __repr__(self, alias=None, formatting_type=None):
        """Repr string for class."""
        return (
            f"{self.__class__.__name__}('{self.expression}', "
            f"'{self.alias}', '{self.formatting_type}')"
        )

    def __str__(self):
        """String representation of metric name."""
        return f"{self.expression}"

    def __call__(self):
        raise NotImplementedError


class Dimension:
    """Base Dimension class."""

    def __init__(self, name, alias=""):
        """Init Dimension object."""
        self.name = name
        self.alias = alias

    def __repr__(self):
        """Repr string for Dimension object."""
        return f"{self.__class__.__name__}(name='{self.name}', alias='{self.alias}')"

    def __str__(self):
        """String representation of Dimension object."""
        return f"{self.name}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"name": self.name}


class OrderBy:
    """Reporting API orderBy object."""

    def __init__(self, field_name, order_type="VALUE", sort_order="ASCENDING"):
        """Init OrderBy object."""
        self.field_name = field_name
        self.order_type = order_type
        self.sort_order = sort_order

    def __call__(self):
        return {
            "fieldName": str(self.field_name),
            "orderType": self.order_type,
            "sortOrder": self.sort_order,
        }


class Report:
    """Report class."""

    def __init__(self, data, index, name=None):
        """Init Report object."""
        self.name = name
        self.DataFrame = pd.DataFrame(dict(data), dtype=float, index=index)

    def __repr__(self):
        return repr(self.DataFrame)
