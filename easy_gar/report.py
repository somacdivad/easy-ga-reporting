"""Report class."""

import pandas as pd


class Report:
    """Report class."""

    def __init__(self, data, index, name=None):
        """Init Report object."""

        self.name = name
        self.DataFrame = pd.DataFrame(dict(data), dtype=float, index=index)

    def __repr__(self):
        return repr(self.DataFrame)
