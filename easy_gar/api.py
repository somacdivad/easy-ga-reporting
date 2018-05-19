"""Google Analytics API object."""

import itertools
import time
import random

from apiclient.discovery import build
from apiclient.errors import HttpError
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import pandas as pd

import easy_gar as gar
from easy_gar.report import Report

_scopes = ("https://www.googleapis.com/auth/analytics.readonly",)
_discovery_uri = "https://analyticsreporting.googleapis.com/$discovery/rest"


class API:
    """API class."""

    def __init__(self, secrets_json, view_id):
        """Init API class."""
        self._view_id = view_id

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_json,
            scope=_scopes,
            message=tools.message_if_missing(secrets_json),
        )

        # Prepare credentials, and authorize HTTP object with them.
        storage = file.Storage("analyticsreporting.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(http=httplib2.Http())

        # Build the service object.
        self._analytics = build(
            "analytics", "v4", http=http, discoveryServiceUrl=_discovery_uri
        )

    def _batch_get(
        self,
        sampling_level=None,
        start_date=None,
        end_date=None,
        metrics=None,
        dimensions=None,
        page_token=None,
        page_size=None,
    ):
        """Return Google Analytics Reporing API response object."""
        request_body = {
            "samplingLevel": sampling_level or gar.sampling_level.default,
            "viewId": self._view_id,
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": metrics,
            "dimensions": dimensions,
            "pageSize": str(page_size) or "10000",
        }
        if page_token:
            request_body["pageToken"] = str(page_token)

        # attempt request using exponential backoff
        error = None
        for n in range(0, 5):
            try:
                response = (
                    self._analytics.reports()
                    .batchGet(body={"reportRequests": [request_body]})
                    .execute()
                )
                return response["reports"][0]

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

    def get_report(
        self,
        start_date="7daysAgo",
        end_date="today",
        metrics=None,
        dimensions=None,
        name=None,
    ):
        """Return an API response object reporting metrics for set dates."""
        if not dimensions:
            dimensions = [easy_gar.dimensions.date]

        # Create GA metric/dimensions objects
        _metrics = [metric() for metric in metrics]
        _dimensions = [dimension() for dimension in dimensions]

        # Get initial data
        response = self._batch_get(start_date, end_date, _metrics, _dimensions)

        if response:
            rows = (
                tuple(row["metrics"][0]["values"])
                for row in response["data"]["rows"]
            )
            indices = (
                tuple(row["dimensions"]) for row in response["data"]["rows"]
            )

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
                        (
                            tuple(row["dimensions"])
                            for row in response["data"]["rows"]
                        ),
                    )

            # Set up report data (for pandas DataFrame)
            fieldnames = (metric.alias for metric in metrics)
            data = zip(fieldnames, zip(*rows))
            index = pd.MultiIndex.from_tuples(
                tuple(indices),
                names=tuple(dimension.alias for dimension in dimensions),
            )

            return Report(data, index, name)
