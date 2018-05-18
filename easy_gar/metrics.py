"""Objects for dealing with Google Analaytics metrics sanely."""

from collections import namedtuple


class Metric:
    """Class for dealing with Google Analytics metrics."""

    def __init__(self, expression=None, alias=None, formatting_type=None):
        self.expression = expression
        self.alias = alias
        self.formatting_type = formatting_type

    def __repr__(self, alias=None, formatting_type=None):
        """Repr string for class."""
        return f"{self.__class__.__name__}('{self.expression}', '{self.alias}', '{self.formatting_type}')"

    def __str__(self):
        """String representation of metric name."""
        return f"{self.alias}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        obj = {"expression": self.expression}
        if self.alias:
            obj["alias"] = self.alias
        if self.formatting_type:
            obj["formattingType"] = self.formatting_type
        return obj

    def __add__(self, other):
        """Metric addition."""
        return Metric(expression=f"({self})+{other}")

    def __sub__(self, other):
        """Metric subtraction."""
        return Metric(expression=f"({self})-{other}")

    def __mul__(self, other):
        """Metric multiplication."""
        return Metric(expression=f"({self})*{other}")

    def __truediv__(self, other):
        """Metric division."""
        return Metric(expression=f"({self})/{other}", formatting_type="FLOAT")


class Metrics:
    """Google Analytics Metrics for use with the API class."""

    # Users
    @property
    def users(self):
        return Metric(expression="ga:users", alias="Users", formatting_type="INTEGER")

    @property
    def new_users(self):
        return Metric(
            expression="ga:newUsers", alias="New Users", formatting_type="INTEGER"
        )

    @property
    def users_1d(self):
        return Metric(
            expression="ga:1dayUsers",
            alias="1 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_7d(self):
        return Metric(
            expression="ga:7dayUsers",
            alias="7 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_14d(self):
        return Metric(
            expression="ga:14dayUsers",
            alias="14 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_28d(self):
        return Metric(
            expression="ga:28dayUsers",
            alias="28 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_30d(self):
        return Metric(
            expression="ga:30dayUsers",
            alias="30 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def sessions_per_user(self):
        return Metric(
            expression="ga:sessionsPerUser",
            alias="Sessions per User",
            formatting_type="FLOAT",
        )

    @property
    def percent_new_sessions(self):
        return Metric(
            expression="ga:percentNewSessions",
            alias="% New Sessions",
            formatting_type="PERCENT",
        )

    # Sessions
    @property
    def sessions(self):
        return Metric(
            expression="ga:sessions", alias="Sessions", formatting_type="INTEGER"
        )

    @property
    def bounces(self):
        return Metric(
            expression="ga:bounces", alias="Bounces", formatting_type="INTEGER"
        )

    @property
    def bounce_rate(self):
        return Metric(
            expression="ga:bounceRate", alias="Bounce Rate", formatting_type="PERCENT"
        )

    @property
    def session_duration(self):
        return Metric(
            expression="ga:sessionDuration",
            alias="Session Duration",
            formatting_type="TIME",
        )

    @property
    def avg_session_duration(self):
        return Metric(
            expression="ga:avgSessionDuration",
            alias="Avg. Session Duration",
            formatting_type="TIME",
        )

    @property
    def unique_dimensions_combination(self):
        return Metric(
            expression="ga:uniqueDimensionCombinations",
            alias="Unique Dimension Combinations",
            formatting_type="INTEGER",
        )

    @property
    def hits(self):
        return Metric(expression="ga:hits", alias="Hits", formatting_type="INTEGER")

    # Traffic Sources
    @property
    def organic_searches(self):
        return Metric(
            expression="ga:organicSearches",
            alias="Organic Searches",
            formatting_type="INTEGER",
        )

    # Adwords
    @property
    def impressions(self):
        return Metric(
            expression="ga:impressions", alias="Impressions", formatting_type="INTEGER"
        )

    @property
    def ad_clicks(self):
        return Metric(
            expression="ga:adClicks", alias="Clicks", formatting_type="INTEGER"
        )

    @property
    def ad_cost(self):
        return Metric(expression="ga:adCost", alias="Cost", formatting_type="CURRENCY")

    @property
    def cpm(self):
        return Metric(expression="ga:CPM", alias="CPM", formatting_type="CURRENCY")

    @property
    def cpc(self):
        return Metric(expression="ga:CPC", alias="CPC", formatting_type="CURRENCY")

    @property
    def ctr(self):
        return Metric(expression="ga:CTR", alias="CTR", formatting_type="PERCENT")

    @property
    def cost_per_transaction(self):
        return Metric(
            expression="ga:costPerTransaction",
            alias="Cost per Transaction",
            formatting_type="CURRENCY",
        )

    @property
    def cost_per_conversion(self):
        return Metric(
            expression="ga:costPerConversion",
            alias="Cost per Conversion",
            formatting_type="CURRENCY",
        )

    @property
    def rpc(self):
        return Metric(expression="ga:RPC", alias="RPC", formatting_type="CURRENCY")

    @property
    def roas(self):
        return Metric(expression="ga:ROAS", alias="ROAS", formatting_type="CURRENCY")

    # Goal Conversions (ALL)
    @property
    def goal_stars_all(self):
        return Metric(
            expression="ga:goalStartsAll",
            alias="Goal Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal_completions_all(self):
        return Metric(
            expression="ga:goalCompletionsAll",
            alias="Goal Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal_value_all(self):
        return Metric(
            expression="ga:goalValueAll", alias="Goal Value", formatting_type="CURRENCY"
        )

    @property
    def goal_value_per_session(self):
        return Metric(
            expression="ga:goalValuePerSession",
            alias="Per Session Goal Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal_conversion_rate_all(self):
        return Metric(
            expression="ga:goalConversionRateAll",
            alias="Goal Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal_abandons_all(self):
        return Metric(
            expression="ga:goalAbandonsAll",
            alias="Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal_abandon_rate_all(self):
        return Metric(
            expression="ga:goalAbandonRateAll",
            alias="Total Abondonment Rate",
            formatting_type="PERCENT",
        )

    # Goal Conversions (Itemized)
    # Goal 01
    @property
    def goal01_starts(self):
        return Metric(
            expression="ga:goal01Starts",
            alias="Goal 01 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal01_completions(self):
        return Metric(
            expression="ga:goal01Completions",
            alias="Goal 01 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal01_value(self):
        return Metric(
            expression="ga:goal01Value",
            alias="Goal 01 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal01_conversion_rate(self):
        return Metric(
            expression="ga:goal01ConversionRate",
            alias="Goal 01 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal01_abandons(self):
        return Metric(
            expression="ga:goal01Abandons",
            alias="Goal 01 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal01_abandon_rate(self):
        return Metric(
            expression="ga:goal01AbandonRate",
            alias="Goal 01 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 02
    @property
    def goal02_starts(self):
        return Metric(
            expression="ga:goal02Starts",
            alias="Goal 02 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal02_completions(self):
        return Metric(
            expression="ga:goal02Completions",
            alias="Goal 02 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal02_value(self):
        return Metric(
            expression="ga:goal02Value",
            alias="Goal 02 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal02_conversion_rate(self):
        return Metric(
            expression="ga:goal02ConversionRate",
            alias="Goal 02 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal02_abandons(self):
        return Metric(
            expression="ga:goal02Abandons",
            alias="Goal 02 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal02_abandon_rate(self):
        return Metric(
            expression="ga:goal02AbandonRate",
            alias="Goal 02 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 03
    @property
    def goal03_starts(self):
        return Metric(
            expression="ga:goal03Starts",
            alias="Goal 03 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal03_completions(self):
        return Metric(
            expression="ga:goal03Completions",
            alias="Goal 03 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal03_value(self):
        return Metric(
            expression="ga:goal03Value",
            alias="Goal 03 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal03_conversion_rate(self):
        return Metric(
            expression="ga:goal03ConversionRate",
            alias="Goal 03 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal03_abandons(self):
        return Metric(
            expression="ga:goal03Abandons",
            alias="Goal 03 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal03_abandon_rate(self):
        return Metric(
            expression="ga:goal03AbandonRate",
            alias="Goal 03 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 04
    @property
    def goal04_starts(self):
        return Metric(
            expression="ga:goal04Starts",
            alias="Goal 04 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal04_completions(self):
        return Metric(
            expression="ga:goal04Completions",
            alias="Goal 04 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal04_value(self):
        return Metric(
            expression="ga:goal04Value",
            alias="Goal 04 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal04_conversion_rate(self):
        return Metric(
            expression="ga:goal04ConversionRate",
            alias="Goal 04 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal04_abandons(self):
        return Metric(
            expression="ga:goal04Abandons",
            alias="Goal 04 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal04_abandon_rate(self):
        return Metric(
            expression="ga:goal04AbandonRate",
            alias="Goal 04 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 05
    @property
    def goal05_starts(self):
        return Metric(
            expression="ga:goal05Starts",
            alias="Goal 05 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal05_completions(self):
        return Metric(
            expression="ga:goal05Completions",
            alias="Goal 05 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal05_value(self):
        return Metric(
            expression="ga:goal05Value",
            alias="Goal 05 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal05_conversion_rate(self):
        return Metric(
            expression="ga:goal05ConversionRate",
            alias="Goal 05 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal05_abandons(self):
        return Metric(
            expression="ga:goal05Abandons",
            alias="Goal 05 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal05_abandon_rate(self):
        return Metric(
            expression="ga:goal05AbandonRate",
            alias="Goal 05 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 06
    @property
    def goal06_starts(self):
        return Metric(
            expression="ga:goal06Starts",
            alias="Goal 06 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal06_completions(self):
        return Metric(
            expression="ga:goal06Completions",
            alias="Goal 06 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal06_value(self):
        return Metric(
            expression="ga:goal06Value",
            alias="Goal 06 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal06_conversion_rate(self):
        return Metric(
            expression="ga:goal06ConversionRate",
            alias="Goal 06 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal06_abandons(self):
        return Metric(
            expression="ga:goal06Abandons",
            alias="Goal 06 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal06_abandon_rate(self):
        return Metric(
            expression="ga:goal06AbandonRate",
            alias="Goal 06 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 07
    @property
    def goal07_starts(self):
        return Metric(
            expression="ga:goal07Starts",
            alias="Goal 07 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal07_completions(self):
        return Metric(
            expression="ga:goal07Completions",
            alias="Goal 07 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal07_value(self):
        return Metric(
            expression="ga:goal07Value",
            alias="Goal 07 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal07_conversion_rate(self):
        return Metric(
            expression="ga:goal07ConversionRate",
            alias="Goal 07 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal07_abandons(self):
        return Metric(
            expression="ga:goal07Abandons",
            alias="Goal 07 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal07_abandon_rate(self):
        return Metric(
            expression="ga:goal07AbandonRate",
            alias="Goal 07 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 08
    @property
    def goal08_starts(self):
        return Metric(
            expression="ga:goal08Starts",
            alias="Goal 08 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal08_completions(self):
        return Metric(
            expression="ga:goal08Completions",
            alias="Goal 08 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal08_value(self):
        return Metric(
            expression="ga:goal08Value",
            alias="Goal 08 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal08_conversion_rate(self):
        return Metric(
            expression="ga:goal08ConversionRate",
            alias="Goal 08 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal08_abandons(self):
        return Metric(
            expression="ga:goal08Abandons",
            alias="Goal 08 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal08_abandon_rate(self):
        return Metric(
            expression="ga:goal08AbandonRate",
            alias="Goal 08 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 09
    @property
    def goal09_starts(self):
        return Metric(
            expression="ga:goal09Starts",
            alias="Goal 09 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal09_completions(self):
        return Metric(
            expression="ga:goal09Completions",
            alias="Goal 09 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal09_value(self):
        return Metric(
            expression="ga:goal09Value",
            alias="Goal 09 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal09_conversion_rate(self):
        return Metric(
            expression="ga:goal09ConversionRate",
            alias="Goal 09 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal09_abandons(self):
        return Metric(
            expression="ga:goal09Abandons",
            alias="Goal 09 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal09_abandon_rate(self):
        return Metric(
            expression="ga:goal09AbandonRate",
            alias="Goal 09 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 10
    @property
    def goal10_starts(self):
        return Metric(
            expression="ga:goal10Starts",
            alias="Goal 10 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal10_completions(self):
        return Metric(
            expression="ga:goal10Completions",
            alias="Goal 10 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal10_value(self):
        return Metric(
            expression="ga:goal10Value",
            alias="Goal 10 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal10_conversion_rate(self):
        return Metric(
            expression="ga:goal10ConversionRate",
            alias="Goal 10 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal10_abandons(self):
        return Metric(
            expression="ga:goal10Abandons",
            alias="Goal 10 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal10_abandon_rate(self):
        return Metric(
            expression="ga:goal10AbandonRate",
            alias="Goal 10 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 11
    @property
    def goal11_starts(self):
        return Metric(
            expression="ga:goal11Starts",
            alias="Goal 11 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal11_completions(self):
        return Metric(
            expression="ga:goal11Completions",
            alias="Goal 11 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal11_value(self):
        return Metric(
            expression="ga:goal11Value",
            alias="Goal 11 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal11_conversion_rate(self):
        return Metric(
            expression="ga:goal11ConversionRate",
            alias="Goal 11 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal11_abandons(self):
        return Metric(
            expression="ga:goal11Abandons",
            alias="Goal 11 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal11_abandon_rate(self):
        return Metric(
            expression="ga:goal11AbandonRate",
            alias="Goal 11 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 12
    @property
    def goal12_starts(self):
        return Metric(
            expression="ga:goal12Starts",
            alias="Goal 12 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal12_completions(self):
        return Metric(
            expression="ga:goal12Completions",
            alias="Goal 12 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal12_value(self):
        return Metric(
            expression="ga:goal12Value",
            alias="Goal 12 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal12_conversion_rate(self):
        return Metric(
            expression="ga:goal12ConversionRate",
            alias="Goal 12 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal12_abandons(self):
        return Metric(
            expression="ga:goal12Abandons",
            alias="Goal 12 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal12_abandon_rate(self):
        return Metric(
            expression="ga:goal12AbandonRate",
            alias="Goal 12 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 13
    @property
    def goal13_starts(self):
        return Metric(
            expression="ga:goal13Starts",
            alias="Goal 13 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal13_completions(self):
        return Metric(
            expression="ga:goal13Completions",
            alias="Goal 13 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal13_value(self):
        return Metric(
            expression="ga:goal13Value",
            alias="Goal 13 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal13_conversion_rate(self):
        return Metric(
            expression="ga:goal13ConversionRate",
            alias="Goal 13 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal13_abandons(self):
        return Metric(
            expression="ga:goal13Abandons",
            alias="Goal 13 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal13_abandon_rate(self):
        return Metric(
            expression="ga:goal13AbandonRate",
            alias="Goal 13 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 14
    @property
    def goal14_starts(self):
        return Metric(
            expression="ga:goal14Starts",
            alias="Goal 14 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal14_completions(self):
        return Metric(
            expression="ga:goal14Completions",
            alias="Goal 14 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal14_value(self):
        return Metric(
            expression="ga:goal14Value",
            alias="Goal 14 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal14_conversion_rate(self):
        return Metric(
            expression="ga:goal14ConversionRate",
            alias="Goal 14 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal14_abandons(self):
        return Metric(
            expression="ga:goal14Abandons",
            alias="Goal 14 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal14_abandon_rate(self):
        return Metric(
            expression="ga:goal14AbandonRate",
            alias="Goal 14 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 15
    @property
    def goal15_starts(self):
        return Metric(
            expression="ga:goal15Starts",
            alias="Goal 15 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal15_completions(self):
        return Metric(
            expression="ga:goal15Completions",
            alias="Goal 15 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal15_value(self):
        return Metric(
            expression="ga:goal15Value",
            alias="Goal 15 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal15_conversion_rate(self):
        return Metric(
            expression="ga:goal15ConversionRate",
            alias="Goal 15 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal15_abandons(self):
        return Metric(
            expression="ga:goal15Abandons",
            alias="Goal 15 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal15_abandon_rate(self):
        return Metric(
            expression="ga:goal15AbandonRate",
            alias="Goal 15 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 16
    @property
    def goal16_starts(self):
        return Metric(
            expression="ga:goal16Starts",
            alias="Goal 16 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal16_completions(self):
        return Metric(
            expression="ga:goal16Completions",
            alias="Goal 16 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal16_value(self):
        return Metric(
            expression="ga:goal16Value",
            alias="Goal 16 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal16_conversion_rate(self):
        return Metric(
            expression="ga:goal16ConversionRate",
            alias="Goal 16 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal16_abandons(self):
        return Metric(
            expression="ga:goal16Abandons",
            alias="Goal 16 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal16_abandon_rate(self):
        return Metric(
            expression="ga:goal16AbandonRate",
            alias="Goal 16 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 17
    @property
    def goal17_starts(self):
        return Metric(
            expression="ga:goal17Starts",
            alias="Goal 17 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal17_completions(self):
        return Metric(
            expression="ga:goal17Completions",
            alias="Goal 17 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal17_value(self):
        return Metric(
            expression="ga:goal17Value",
            alias="Goal 17 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal17_conversion_rate(self):
        return Metric(
            expression="ga:goal17ConversionRate",
            alias="Goal 17 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal17_abandons(self):
        return Metric(
            expression="ga:goal17Abandons",
            alias="Goal 17 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal17_abandon_rate(self):
        return Metric(
            expression="ga:goal17AbandonRate",
            alias="Goal 17 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 18
    @property
    def goal18_starts(self):
        return Metric(
            expression="ga:goal18Starts",
            alias="Goal 18 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal18_completions(self):
        return Metric(
            expression="ga:goal18Completions",
            alias="Goal 18 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal18_value(self):
        return Metric(
            expression="ga:goal18Value",
            alias="Goal 18 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal18_conversion_rate(self):
        return Metric(
            expression="ga:goal18ConversionRate",
            alias="Goal 18 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal18_abandons(self):
        return Metric(
            expression="ga:goal18Abandons",
            alias="Goal 18 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal18_abandon_rate(self):
        return Metric(
            expression="ga:goal18AbandonRate",
            alias="Goal 18 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 19
    @property
    def goal19_starts(self):
        return Metric(
            expression="ga:goal19Starts",
            alias="Goal 19 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal19_completions(self):
        return Metric(
            expression="ga:goal19Completions",
            alias="Goal 19 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal19_value(self):
        return Metric(
            expression="ga:goal19Value",
            alias="Goal 19 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal19_conversion_rate(self):
        return Metric(
            expression="ga:goal19ConversionRate",
            alias="Goal 19 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal19_abandons(self):
        return Metric(
            expression="ga:goal19Abandons",
            alias="Goal 19 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal19_abandon_rate(self):
        return Metric(
            expression="ga:goal19AbandonRate",
            alias="Goal 19 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 20
    @property
    def goal20_starts(self):
        return Metric(
            expression="ga:goal20Starts",
            alias="Goal 20 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal20_completions(self):
        return Metric(
            expression="ga:goal20Completions",
            alias="Goal 20 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal20_value(self):
        return Metric(
            expression="ga:goal20Value",
            alias="Goal 20 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal20_conversion_rate(self):
        return Metric(
            expression="ga:goal20ConversionRate",
            alias="Goal 20 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal20_abandons(self):
        return Metric(
            expression="ga:goal20Abandons",
            alias="Goal 20 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal20_abandon_rate(self):
        return Metric(
            expression="ga:goal20AbandonRate",
            alias="Goal 20 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Page Tracking
    @property
    def page_value(self):
        return Metric(
            expression="ga:pageValue", alias="Page Value", formatting_type="CURRENCY"
        )

    @property
    def entrances(self):
        return Metric(
            expression="ga:entrances", alias="Entrances", formatting_type="INTEGER"
        )

    @property
    def entrance_rate(self):
        return Metric(
            expression="ga:entranceRate",
            alias="Entrances / Pageviews",
            formatting_type="PERCENT",
        )

    @property
    def pageviews(self):
        return Metric(
            expression="ga:pageviews", alias="Pageviews", formatting_type="INTEGER"
        )

    @property
    def pageviews_per_session(self):
        return Metric(
            expression="ga:pageviewsPerSession",
            alias="Pages / Session",
            formatting_type="FLOAT",
        )

    @property
    def unique_pageviews(self):
        return Metric(
            expression="ga:uniquePageviews",
            alias="Unique Page Views",
            formatting_type="INTEGER",
        )

    @property
    def time_on_page(self):
        return Metric(
            expression="ga:timeOnPage", alias="Time on Page", formatting_type="TIME"
        )

    @property
    def exits(self):
        return Metric(expression="ga:exits", alias="Exits", formatting_type="INTEGER")

    @property
    def avg_time_on_page(self):
        return Metric(
            expression="ga:avgTimeOnPage",
            alias="Avg. Time on Page",
            formatting_type="TIME",
        )

    @property
    def exit_rate(self):
        return Metric(
            expression="ga:exitRate", alias="% Exit", formatting_type="PERCENT"
        )


metrics = Metrics()
