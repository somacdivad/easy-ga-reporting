"""Report class for dealing with Google Analytics Reporting API responses sanely."""

from collections import namedtuple
import pandas as pd
import re

from pprint import pprint


class Report():
    """Report class."""

    def __init__(self, api_report, name=None):
        """Init Report object."""

        pprint(api_report)

        def _fmt(ga_string):
            s = re.sub("(.)([A-Z][a-z]+)", r"\1 \2", ga_string)
            return re.sub("([a-z0-9])([A-Z])", r"\1 \2", s).lstrip("ga:").title()

        fieldnames = (
            _fmt(entry["name"])
            for entry in api_report["columnHeader"]["metricHeader"][
                "metricHeaderEntries"
            ]
        )
        rows = (row["metrics"][0]["values"] for row in api_report["data"]["rows"])
        data = zip(fieldnames, zip(*rows))

        index = pd.MultiIndex.from_tuples(
            tuple(tuple(row["dimensions"]) for row in api_report["data"]["rows"]),
            names=tuple(_fmt(dim) for dim in api_report["columnHeader"]["dimensions"]),
        )

        self.name = name
        self.df = pd.DataFrame(dict(data), dtype=float, index=index)

    def __repr__(self):
        return repr(self.df)
