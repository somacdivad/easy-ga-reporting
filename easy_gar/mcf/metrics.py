"""Google Analytics Muti-channel Funnel API v3 Metrics."""

from easy_gar.base import Metric


class MCFMetric(Metric):
    """Multi-Channel Funnel Metric."""

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return self.expression


class Metrics:
    """Multi-Channel Funnel metrics for use with API object."""

    @property
    def first_impressions_conversions(self):
        return MCFMetric(
            expression="mcf:firstImpressionConversions",
            alias="First Impression Conversions",
            formatting_type="INTEGER",
        )

    @property
    def first_impression_value(self):
        return MCFMetric(
            expression="mcf:firstImpressionValue",
            alias="First Impression Value",
            formatting_type="CURRENCY",
        )

    @property
    def assisted_conversions(self):
        return MCFMetric(
            expression="mcf:impressionAssistedConversions",
            alias="Assisted Conversions",
            formatting_type="INTEGER",
        )

    @property
    def assisted_conversions_value(self):
        return MCFMetric(
            expression="mcf:impressionAssistedValue",
            alias="Assisted Conversions Value",
            formatting_type="CURRENCY",
        )

    @property
    def total_conversions(self):
        return MCFMetric(
            expression="mcf:totalConversions",
            alias="Total Conversions",
            formatting_type="INTEGER",
        )

    @property
    def total_conversion_value(self):
        return MCFMetric(
            expression="mcf:totalConversionValue",
            alias="Total Conversion Value",
            formatting_type="CURRENCY",
        )
