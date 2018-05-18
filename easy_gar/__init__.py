"""Google Analytics API object."""

import itertools

from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import pandas as pd

import easy_gar
from easy_gar.dimensions import dimensions
from easy_gar.metrics import metrics
from easy_gar.report import Report

from pprint import pprint

__version__ = "1.0.0"
__author__ = "David Amos"

__all__ = ["API", "dimensions", "metrics", "Report"]

_scopes = ("https://www.googleapis.com/auth/analytics.readonly",)
_discovery_uri = ("https://analyticsreporting.googleapis.com/$discovery/rest")


class API:
    """API class."""

    def __init__(self, secrets_json, view_id):
        """Init API class."""
        self._view_id = view_id

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_json, scope=_scopes, message=tools.message_if_missing(secrets_json)
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
        start_date=None,
        end_date=None,
        metrics=None,
        dimensions=None,
        page_token=None,
        page_size=None,
    ):
        """Return Google Analytics Reporing API response object."""
        request_body = {
            "viewId": self._view_id,
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": metrics,
            "dimensions": dimensions,
            "pageSize": str(page_size) if page_size else "10000"
        }
        if page_token:
            request_body["pageToken"] = str(page_token)

        return self._analytics.reports().batchGet(
            body={"reportRequests": [request_body]}
        ).execute()

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
        report = response["reports"][0]
        rows = (tuple(row["metrics"][0]["values"]) for row in report["data"]["rows"])
        indices = (tuple(row["dimensions"]) for row in report["data"]["rows"])

        # Retrieve additional data if response is paginated
        while "nextPageToken" in report.keys():
            page_token = report["nextPageToken"]
            response = self._batch_get(
                start_date, end_date, _metrics, _dimensions, page_token
            )
            report = response["reports"][0]
            rows = itertools.chain(
                rows,
                (tuple(row["metrics"][0]["values"]) for row in report["data"]["rows"]),
            )
            indices = itertools.chain(
                indices, (tuple(row["dimensions"]) for row in report["data"]["rows"])
            )

        # Set up report data (for pandas DataFrame)
        fieldnames = (metric.alias for metric in metrics)
        data = zip(fieldnames, zip(*rows))
        index = pd.MultiIndex.from_tuples(
            tuple(indices), names=tuple(dimension.alias for dimension in dimensions)
        )

        return Report(data, index, name)
