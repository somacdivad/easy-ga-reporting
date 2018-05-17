"""Google Analytics API object."""

from collections import namedtuple

from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

from api.dimensions import dimensions
from api.metrics import metrics

__all__ = ["API", "dimensions", "metrics", "Report"]

__scopes = ["https://www.googleapis.com/auth/analytics.readonly"]
__discovery_uri = ("https://analyticsreporting.googleapis.com/$discovery/rest")


class API:
    """API class."""

    dimensions = Dimensions()
    metrics = Metrics()

    def __init__(self, secrets_json, view_id):
        """Init API class."""
        self._view_id = view_id

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_json, scope=__scopes, message=tools.message_if_missing(
                secrets_json)
        )

        # Prepare credentials, and authorize HTTP object with them.
        # If the credentials don't exist or are invalid run through the
        # native client flow. The Storage object will ensure that if
        # successful the good credentials will get written back to a file.
        storage = file.Storage("analyticsreporting.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(http=httplib2.Http())

        # Build the service object.
        self._analytics = build(
            "analytics", "v4", http=http, discoveryServiceUrl=__discovery_uri
        )

    def get_report(
        self, start_date="7daysAgo", end_date="today", metrics=None, dimensions=None
    ):
        """Return an API response object reporting metrics for set dates."""
        return self._analytics.reports().batchGet(
            body={
                "reportRequests": [
                    {
                        "viewId": self._view_id,
                        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
                        "metrics": metrics,
                        "dimensions": dimensions,
                    }
                ]
            }
        ).execute()
