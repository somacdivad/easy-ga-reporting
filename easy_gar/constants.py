"""Google Analytics Reporting API Constants."""

from collections import namedtuple

SamplingLevel = namedtuple("SamplingLevel", ["default", "small", "large"])
sampling_level = SamplingLevel(default="DEFAULT", small="SMALL", large="LARGE")

OrderType = namedtuple(
    "OrderType",
    [
        "default",
        "value",
        "delta",
        "smart",
        "histogram_bucket",
        "dimension_as_integer",
    ],
)
order_type = OrderType(
    default="VALUE",
    value="VALUE",
    delta="DELTA",
    smart="SMART",
    histogram_bucket="HISTOGRAM_BUCKET",
    dimension_as_integer="DIMENSION_AS_INTEGER",
)

SortOrder = namedtuple("SortOrder", ["default", "ascending", "descending"])
sort_order = SortOrder(
    default="ASCENDING", ascending="ASCENDING", descending="DESCENDING"
)
