"""Report class for dealing with Google Analytics Reporting API responses sanely."""

from collections import namedtuple
import itertools
import pandas as pd
import re

from pprint import pprint

class Report():
    """Report class."""

    def __init__(self, data, index, name=None):
        """Init Report object."""

        self.name = name
        self.df = pd.DataFrame(dict(data), dtype=float, index=index)

    def __repr__(self):
        return repr(self.df)
