"""Base classes."""

import pandas as pd


class Metric:
    """Base Metric class."""

    def __init__(self, expression=None, alias=None, formatting_type=None):
        """Init Metric object."""
        self.expression = expression
        self.alias = alias
        self.formatting_type = formatting_type

    def __repr__(self, alias=None, formatting_type=None):
        """Repr string for class."""
        return (
            f"{self.__class__.__name__}('{self.expression}', "
            f"'{self.alias}', '{self.formatting_type}')"
        )

    def __str__(self):
        """String representation of metric name."""
        return f"{self.expression}"

    def __call__(self):
        raise NotImplementedError


class Dimension:
    """Base Dimension class."""

    def __init__(self, name, alias=""):
        """Init Dimension object."""
        self.name = name
        self.alias = alias

    def __repr__(self):
        """Repr string for Dimension object."""
        return f"{self.__class__.__name__}(name='{self.name}', alias='{self.alias}')"

    def __str__(self):
        """String representation of Dimension object."""
        return f"{self.name}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"name": self.name}


class OrderBy:
    """Reporting API orderBy object."""

    def __init__(self, field_name, order_type="VALUE", sort_order="ASCENDING"):
        """Init OrderBy object."""
        self.field_name = field_name
        self.order_type = order_type
        self.sort_order = sort_order

    def __call__(self):
        return {
            "fieldName": str(self.field_name),
            "orderType": self.order_type,
            "sortOrder": self.sort_order,
        }


class Report:
    """Report class."""

    def __init__(self, data, index, name=None):
        """Init Report object."""
        self.name = name
        self.DataFrame = pd.DataFrame(dict(data), dtype=float, index=index)

    def __repr__(self):
        return repr(self.DataFrame)
