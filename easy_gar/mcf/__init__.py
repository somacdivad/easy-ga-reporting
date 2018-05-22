"""Classes and functions for working with Google Analytics Multi-channel
Funnels API v3.
"""

from apiclient.discovery import build
# from apiclient.errors import HttpError
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

import easy_gar
from easy_gar.mcf.metrics import Metrics
from easy_gar.mcf.dimensions import Dimensions

__all__ = ["dimensions", "McfAPI", "metrics"]

metrics = Metrics()
dimensions = Dimensions()


class McfAPI:
    """Google Analytics Multi-channel Fulls API class."""

    sampling_level = easy_gar.constants.sampling_level.default

    def __init__(self, secrets_json, view_id):
        """Init McfAPI object."""
        self._view_id = view_id

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_json,
            scope=("https://www.googleapis.com/auth/analytics.readonly",),
            message=tools.message_if_missing(secrets_json),
        )

        # Prepare credentials, and authorize HTTP object with them.
        storage = file.Storage("analyticsreporting.dat")
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(http=httplib2.Http())

        # build the anlaytics v3 service object
        self._analytics = build("analytics", "v3", http=http)

    def get_report(self):
        raise NotImplementedError
