"""Classes and functions for working with Google Analytics Reporting API v4."""

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
from easy_gar.base import Report
from easy_gar.metrics import Metrics
from easy_gar.dimensions import Dimensions

__version__ = "1.0.0"
__author__ = "David Amos"

__all__ = ["dimensions", "metrics", "OrderBy", "ReportingAPI"]

metrics = Metrics()
dimensions = Dimensions()


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

        print(secrets_type)

        build = {
            "oauth": self._build_from_oauth_keys,
            "service": self._build_from_service_account_keys,
        }.get(
            secrets_type, None
        )

        if build is None:
            raise ValueError("Invalid secrets_type; must be on of 'oauth' or 'service'")

        build(secrets_path)

    def _request_with_exponential_backoff(self, body):
        """Return Google Analytic Reporting API v4 reponse object."""
        error = None
        for n in range(0, 5):
            try:
                return (
                    self._reporting.reports().batchGet(
                        body={"reportRequests": [body]}
                    ).execute()
                )

            except HttpError as err:
                error = err
                if err.resp.reason in [
                    "userRateLimitExceeded",
                    "quotaExceeded",
                    "internalServerError",
                    "backendError",
                ]:
                    time.sleep((2 ** n)) + random.random()
                else:
                    break

        raise error

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
            rows = (
                tuple(row["metrics"][0]["values"]) for row in response["data"]["rows"]
            )
            indices = (tuple(row["dimensions"]) for row in response["data"]["rows"])

            # Retrieve additional data if response is paginated
            while "nextPageToken" in response.keys():
                page_token = response["nextPageToken"]
                response = self._batch_get(
                    start_date, end_date, _metrics, _dimensions, page_token
                )
                if response:
                    rows = itertools.chain(
                        rows,
                        (
                            tuple(row["metrics"][0]["values"])
                            for row in response["data"]["rows"]
                        ),
                    )
                    indices = itertools.chain(
                        indices,
                        (tuple(row["dimensions"]) for row in response["data"]["rows"]),
                    )

            # Set up report data (for pandas DataFrame)
            fieldnames = (metric.alias for metric in metrics)
            data = zip(fieldnames, zip(*rows))
            index = pd.MultiIndex.from_tuples(
                tuple(indices), names=tuple(dimension.alias for dimension in dimensions)
            )

            return Report(data, index, name)


class OrderBy:
    """Reporting API orderBy object."""

    def __init__(self, field_name=None, order_type=None, sort_order=None):
        """Init OrderBy object."""
        self.field_name = field_name
        self.order_type = order_type or "VALUE"
        self.sort_order = sort_order or "ASCENDING"

    def __call__(self):
        return {
            "fieldName": str(self.field_name),
            "orderType": self.order_type,
            "sortOrder": self.sort_order,
        }
