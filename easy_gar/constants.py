"""Google Analytics Reporting API Constants."""

from collections import namedtuple


def _default_namedtuple(typename, fieldnames, default_values=None):
    nt = namedtuple(typename, fieldnames)
    if default_values is not None:
        nt.__new__.__defaults__ = tuple(default_values)
    return nt()


levels = ["default", "small", "large"]
sampling_level = _default_namedtuple(
    "SamplingLevel", levels, tuple(s.upper() for s in levels)
)

orders = ["default", "ascending", "descending"]
sort_order = _default_namedtuple("SortOrder", orders, tuple(s.upper() for s in orders))


types = [
    "default", "value", "delta", "smart", "histogram_bucket", "dimension_as_integer"
]
order_type = _default_namedtuple("OrderType", types, tuple(s.upper() for s in types))
