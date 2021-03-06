"""Google Analytics Reporting API v4 Metrics."""

from easy_gar.base import Metric


class ReportingMetric(Metric):
    """Analytics Metric class."""

    def __init__(self, expression, alias=None, formatting_type=None):
        super().__init__(expression, alias, formatting_type)

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
        m = ReportingMetric(expression=f"({self.expression})+{other.expression}")
        m.alias = f"{self} + {other}"
        return m

    def __sub__(self, other):
        """Metric subtraction."""
        m = ReportingMetric(expression=f"({self.expression})-{other.expression}")
        m.alias = f"{self} - {other}"
        return m

    def __mul__(self, other):
        """Metric multiplication."""
        m = ReportingMetric(expression=f"({self.expression})*{other.expression}")
        m.alias = f"{self} * {other}"
        return m

    def __truediv__(self, other):
        """Metric division."""
        m = ReportingMetric(
            expression=f"({self.expression})/{other.expression}",
            formatting_type="FLOAT",
        )
        m.alias = f"{self} / {other}"
        return m


class Metrics:
    """Analytics Metrics for use with the API objects."""

    # Users
    @property
    def users(self):
        return ReportingMetric(
            expression="ga:users", alias="Users", formatting_type="INTEGER"
        )

    @property
    def new_users(self):
        return ReportingMetric(
            expression="ga:newUsers", alias="New Users", formatting_type="INTEGER"
        )

    @property
    def users_1d(self):
        return ReportingMetric(
            expression="ga:1dayUsers",
            alias="1 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_7d(self):
        return ReportingMetric(
            expression="ga:7dayUsers",
            alias="7 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_14d(self):
        return ReportingMetric(
            expression="ga:14dayUsers",
            alias="14 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_28d(self):
        return ReportingMetric(
            expression="ga:28dayUsers",
            alias="28 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def users_30d(self):
        return ReportingMetric(
            expression="ga:30dayUsers",
            alias="30 Day Active Users",
            formatting_type="INTEGER",
        )

    @property
    def sessions_per_user(self):
        return ReportingMetric(
            expression="ga:sessionsPerUser",
            alias="Sessions per User",
            formatting_type="FLOAT",
        )

    @property
    def percent_new_sessions(self):
        return ReportingMetric(
            expression="ga:percentNewSessions",
            alias="% New Sessions",
            formatting_type="PERCENT",
        )

    # Sessions
    @property
    def sessions(self):
        return ReportingMetric(
            expression="ga:sessions", alias="Sessions", formatting_type="INTEGER"
        )

    @property
    def bounces(self):
        return ReportingMetric(
            expression="ga:bounces", alias="Bounces", formatting_type="INTEGER"
        )

    @property
    def bounce_rate(self):
        return ReportingMetric(
            expression="ga:bounceRate", alias="Bounce Rate", formatting_type="PERCENT"
        )

    @property
    def session_duration(self):
        return ReportingMetric(
            expression="ga:sessionDuration",
            alias="Session Duration",
            formatting_type="TIME",
        )

    @property
    def avg_session_duration(self):
        return ReportingMetric(
            expression="ga:avgSessionDuration",
            alias="Avg. Session Duration",
            formatting_type="TIME",
        )

    @property
    def unique_dimensions_combination(self):
        return ReportingMetric(
            expression="ga:uniqueDimensionCombinations",
            alias="Unique Dimension Combinations",
            formatting_type="INTEGER",
        )

    @property
    def hits(self):
        return ReportingMetric(
            expression="ga:hits", alias="Hits", formatting_type="INTEGER"
        )

    # Traffic Sources
    @property
    def organic_searches(self):
        return ReportingMetric(
            expression="ga:organicSearches",
            alias="Organic Searches",
            formatting_type="INTEGER",
        )

    # Adwords
    @property
    def impressions(self):
        return ReportingMetric(
            expression="ga:impressions", alias="Impressions", formatting_type="INTEGER"
        )

    @property
    def ad_clicks(self):
        return ReportingMetric(
            expression="ga:adClicks", alias="Clicks", formatting_type="INTEGER"
        )

    @property
    def ad_cost(self):
        return ReportingMetric(
            expression="ga:adCost", alias="Cost", formatting_type="CURRENCY"
        )

    @property
    def cpm(self):
        return ReportingMetric(
            expression="ga:CPM", alias="CPM", formatting_type="CURRENCY"
        )

    @property
    def cpc(self):
        return ReportingMetric(
            expression="ga:CPC", alias="CPC", formatting_type="CURRENCY"
        )

    @property
    def ctr(self):
        return ReportingMetric(
            expression="ga:CTR", alias="CTR", formatting_type="PERCENT"
        )

    @property
    def cost_per_transaction(self):
        return ReportingMetric(
            expression="ga:costPerTransaction",
            alias="Cost per Transaction",
            formatting_type="CURRENCY",
        )

    @property
    def cost_per_conversion(self):
        return ReportingMetric(
            expression="ga:costPerConversion",
            alias="Cost per Conversion",
            formatting_type="CURRENCY",
        )

    @property
    def rpc(self):
        return ReportingMetric(
            expression="ga:RPC", alias="RPC", formatting_type="CURRENCY"
        )

    @property
    def roas(self):
        return ReportingMetric(
            expression="ga:ROAS", alias="ROAS", formatting_type="CURRENCY"
        )

    # Goal Conversions (ALL)
    @property
    def goal_stars_all(self):
        return ReportingMetric(
            expression="ga:goalStartsAll",
            alias="Goal Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal_completions_all(self):
        return ReportingMetric(
            expression="ga:goalCompletionsAll",
            alias="Goal Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal_value_all(self):
        return ReportingMetric(
            expression="ga:goalValueAll", alias="Goal Value", formatting_type="CURRENCY"
        )

    @property
    def goal_value_per_session(self):
        return ReportingMetric(
            expression="ga:goalValuePerSession",
            alias="Per Session Goal Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal_conversion_rate_all(self):
        return ReportingMetric(
            expression="ga:goalConversionRateAll",
            alias="Goal Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal_abandons_all(self):
        return ReportingMetric(
            expression="ga:goalAbandonsAll",
            alias="Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal_abandon_rate_all(self):
        return ReportingMetric(
            expression="ga:goalAbandonRateAll",
            alias="Total Abondonment Rate",
            formatting_type="PERCENT",
        )

    # Goal Conversions (Itemized)
    # Goal 01
    @property
    def goal01_starts(self):
        return ReportingMetric(
            expression="ga:goal1Starts",
            alias="Goal 01 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal01_completions(self):
        return ReportingMetric(
            expression="ga:goal1Completions",
            alias="Goal 01 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal01_value(self):
        return ReportingMetric(
            expression="ga:goal1Value",
            alias="Goal 01 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal01_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal1ConversionRate",
            alias="Goal 01 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal01_abandons(self):
        return ReportingMetric(
            expression="ga:goal1Abandons",
            alias="Goal 01 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal01_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal1AbandonRate",
            alias="Goal 01 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 02
    @property
    def goal02_starts(self):
        return ReportingMetric(
            expression="ga:goal2Starts",
            alias="Goal 02 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal02_completions(self):
        return ReportingMetric(
            expression="ga:goal2Completions",
            alias="Goal 02 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal02_value(self):
        return ReportingMetric(
            expression="ga:goal2Value",
            alias="Goal 02 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal02_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal2ConversionRate",
            alias="Goal 02 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal02_abandons(self):
        return ReportingMetric(
            expression="ga:goal2Abandons",
            alias="Goal 02 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal02_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal2AbandonRate",
            alias="Goal 02 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 03
    @property
    def goal03_starts(self):
        return ReportingMetric(
            expression="ga:goal3Starts",
            alias="Goal 03 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal03_completions(self):
        return ReportingMetric(
            expression="ga:goal3Completions",
            alias="Goal 03 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal03_value(self):
        return ReportingMetric(
            expression="ga:goal3Value",
            alias="Goal 03 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal03_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal3ConversionRate",
            alias="Goal 03 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal03_abandons(self):
        return ReportingMetric(
            expression="ga:goal3Abandons",
            alias="Goal 03 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal03_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal3AbandonRate",
            alias="Goal 03 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 04
    @property
    def goal04_starts(self):
        return ReportingMetric(
            expression="ga:goal4Starts",
            alias="Goal 04 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal04_completions(self):
        return ReportingMetric(
            expression="ga:goal4Completions",
            alias="Goal 04 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal04_value(self):
        return ReportingMetric(
            expression="ga:goal4Value",
            alias="Goal 04 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal04_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal4ConversionRate",
            alias="Goal 04 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal04_abandons(self):
        return ReportingMetric(
            expression="ga:goal4Abandons",
            alias="Goal 04 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal04_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal4AbandonRate",
            alias="Goal 04 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 05
    @property
    def goal05_starts(self):
        return ReportingMetric(
            expression="ga:goal5Starts",
            alias="Goal 05 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal05_completions(self):
        return ReportingMetric(
            expression="ga:goal5Completions",
            alias="Goal 05 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal05_value(self):
        return ReportingMetric(
            expression="ga:goal5Value",
            alias="Goal 05 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal05_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal5ConversionRate",
            alias="Goal 05 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal05_abandons(self):
        return ReportingMetric(
            expression="ga:goal5Abandons",
            alias="Goal 05 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal05_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal5AbandonRate",
            alias="Goal 05 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 06
    @property
    def goal06_starts(self):
        return ReportingMetric(
            expression="ga:goal6Starts",
            alias="Goal 06 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal06_completions(self):
        return ReportingMetric(
            expression="ga:goal6Completions",
            alias="Goal 06 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal06_value(self):
        return ReportingMetric(
            expression="ga:goal6Value",
            alias="Goal 06 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal06_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal6ConversionRate",
            alias="Goal 06 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal06_abandons(self):
        return ReportingMetric(
            expression="ga:goal6Abandons",
            alias="Goal 06 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal06_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal6AbandonRate",
            alias="Goal 06 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 07
    @property
    def goal07_starts(self):
        return ReportingMetric(
            expression="ga:goal7Starts",
            alias="Goal 07 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal07_completions(self):
        return ReportingMetric(
            expression="ga:goal7Completions",
            alias="Goal 07 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal07_value(self):
        return ReportingMetric(
            expression="ga:goal7Value",
            alias="Goal 07 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal07_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal7ConversionRate",
            alias="Goal 07 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal07_abandons(self):
        return ReportingMetric(
            expression="ga:goal7Abandons",
            alias="Goal 07 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal07_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal7AbandonRate",
            alias="Goal 07 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 08
    @property
    def goal08_starts(self):
        return ReportingMetric(
            expression="ga:goal8Starts",
            alias="Goal 08 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal08_completions(self):
        return ReportingMetric(
            expression="ga:goal8Completions",
            alias="Goal 08 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal08_value(self):
        return ReportingMetric(
            expression="ga:goal8Value",
            alias="Goal 08 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal08_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal8ConversionRate",
            alias="Goal 08 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal08_abandons(self):
        return ReportingMetric(
            expression="ga:goal8Abandons",
            alias="Goal 08 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal08_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal8AbandonRate",
            alias="Goal 08 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 09
    @property
    def goal09_starts(self):
        return ReportingMetric(
            expression="ga:goal9Starts",
            alias="Goal 09 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal09_completions(self):
        return ReportingMetric(
            expression="ga:goal9Completions",
            alias="Goal 09 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal09_value(self):
        return ReportingMetric(
            expression="ga:goal9Value",
            alias="Goal 09 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal09_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal9ConversionRate",
            alias="Goal 09 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal09_abandons(self):
        return ReportingMetric(
            expression="ga:goal9Abandons",
            alias="Goal 09 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal09_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal9AbandonRate",
            alias="Goal 09 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 10
    @property
    def goal10_starts(self):
        return ReportingMetric(
            expression="ga:goal10Starts",
            alias="Goal 10 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal10_completions(self):
        return ReportingMetric(
            expression="ga:goal10Completions",
            alias="Goal 10 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal10_value(self):
        return ReportingMetric(
            expression="ga:goal10Value",
            alias="Goal 10 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal10_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal10ConversionRate",
            alias="Goal 10 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal10_abandons(self):
        return ReportingMetric(
            expression="ga:goal10Abandons",
            alias="Goal 10 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal10_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal10AbandonRate",
            alias="Goal 10 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 11
    @property
    def goal11_starts(self):
        return ReportingMetric(
            expression="ga:goal11Starts",
            alias="Goal 11 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal11_completions(self):
        return ReportingMetric(
            expression="ga:goal11Completions",
            alias="Goal 11 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal11_value(self):
        return ReportingMetric(
            expression="ga:goal11Value",
            alias="Goal 11 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal11_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal11ConversionRate",
            alias="Goal 11 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal11_abandons(self):
        return ReportingMetric(
            expression="ga:goal11Abandons",
            alias="Goal 11 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal11_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal11AbandonRate",
            alias="Goal 11 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 12
    @property
    def goal12_starts(self):
        return ReportingMetric(
            expression="ga:goal12Starts",
            alias="Goal 12 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal12_completions(self):
        return ReportingMetric(
            expression="ga:goal12Completions",
            alias="Goal 12 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal12_value(self):
        return ReportingMetric(
            expression="ga:goal12Value",
            alias="Goal 12 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal12_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal12ConversionRate",
            alias="Goal 12 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal12_abandons(self):
        return ReportingMetric(
            expression="ga:goal12Abandons",
            alias="Goal 12 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal12_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal12AbandonRate",
            alias="Goal 12 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 13
    @property
    def goal13_starts(self):
        return ReportingMetric(
            expression="ga:goal13Starts",
            alias="Goal 13 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal13_completions(self):
        return ReportingMetric(
            expression="ga:goal13Completions",
            alias="Goal 13 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal13_value(self):
        return ReportingMetric(
            expression="ga:goal13Value",
            alias="Goal 13 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal13_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal13ConversionRate",
            alias="Goal 13 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal13_abandons(self):
        return ReportingMetric(
            expression="ga:goal13Abandons",
            alias="Goal 13 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal13_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal13AbandonRate",
            alias="Goal 13 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 14
    @property
    def goal14_starts(self):
        return ReportingMetric(
            expression="ga:goal14Starts",
            alias="Goal 14 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal14_completions(self):
        return ReportingMetric(
            expression="ga:goal14Completions",
            alias="Goal 14 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal14_value(self):
        return ReportingMetric(
            expression="ga:goal14Value",
            alias="Goal 14 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal14_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal14ConversionRate",
            alias="Goal 14 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal14_abandons(self):
        return ReportingMetric(
            expression="ga:goal14Abandons",
            alias="Goal 14 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal14_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal14AbandonRate",
            alias="Goal 14 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 15
    @property
    def goal15_starts(self):
        return ReportingMetric(
            expression="ga:goal15Starts",
            alias="Goal 15 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal15_completions(self):
        return ReportingMetric(
            expression="ga:goal15Completions",
            alias="Goal 15 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal15_value(self):
        return ReportingMetric(
            expression="ga:goal15Value",
            alias="Goal 15 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal15_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal15ConversionRate",
            alias="Goal 15 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal15_abandons(self):
        return ReportingMetric(
            expression="ga:goal15Abandons",
            alias="Goal 15 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal15_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal15AbandonRate",
            alias="Goal 15 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 16
    @property
    def goal16_starts(self):
        return ReportingMetric(
            expression="ga:goal16Starts",
            alias="Goal 16 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal16_completions(self):
        return ReportingMetric(
            expression="ga:goal16Completions",
            alias="Goal 16 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal16_value(self):
        return ReportingMetric(
            expression="ga:goal16Value",
            alias="Goal 16 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal16_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal16ConversionRate",
            alias="Goal 16 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal16_abandons(self):
        return ReportingMetric(
            expression="ga:goal16Abandons",
            alias="Goal 16 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal16_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal16AbandonRate",
            alias="Goal 16 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 17
    @property
    def goal17_starts(self):
        return ReportingMetric(
            expression="ga:goal17Starts",
            alias="Goal 17 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal17_completions(self):
        return ReportingMetric(
            expression="ga:goal17Completions",
            alias="Goal 17 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal17_value(self):
        return ReportingMetric(
            expression="ga:goal17Value",
            alias="Goal 17 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal17_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal17ConversionRate",
            alias="Goal 17 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal17_abandons(self):
        return ReportingMetric(
            expression="ga:goal17Abandons",
            alias="Goal 17 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal17_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal17AbandonRate",
            alias="Goal 17 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 18
    @property
    def goal18_starts(self):
        return ReportingMetric(
            expression="ga:goal18Starts",
            alias="Goal 18 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal18_completions(self):
        return ReportingMetric(
            expression="ga:goal18Completions",
            alias="Goal 18 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal18_value(self):
        return ReportingMetric(
            expression="ga:goal18Value",
            alias="Goal 18 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal18_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal18ConversionRate",
            alias="Goal 18 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal18_abandons(self):
        return ReportingMetric(
            expression="ga:goal18Abandons",
            alias="Goal 18 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal18_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal18AbandonRate",
            alias="Goal 18 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 19
    @property
    def goal19_starts(self):
        return ReportingMetric(
            expression="ga:goal19Starts",
            alias="Goal 19 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal19_completions(self):
        return ReportingMetric(
            expression="ga:goal19Completions",
            alias="Goal 19 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal19_value(self):
        return ReportingMetric(
            expression="ga:goal19Value",
            alias="Goal 19 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal19_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal19ConversionRate",
            alias="Goal 19 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal19_abandons(self):
        return ReportingMetric(
            expression="ga:goal19Abandons",
            alias="Goal 19 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal19_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal19AbandonRate",
            alias="Goal 19 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Goal 20
    @property
    def goal20_starts(self):
        return ReportingMetric(
            expression="ga:goal20Starts",
            alias="Goal 20 Starts",
            formatting_type="INTEGER",
        )

    @property
    def goal20_completions(self):
        return ReportingMetric(
            expression="ga:goal20Completions",
            alias="Goal 20 Completions",
            formatting_type="INTEGER",
        )

    @property
    def goal20_value(self):
        return ReportingMetric(
            expression="ga:goal20Value",
            alias="Goal 20 Value",
            formatting_type="CURRENCY",
        )

    @property
    def goal20_conversion_rate(self):
        return ReportingMetric(
            expression="ga:goal20ConversionRate",
            alias="Goal 20 Conversion Rate",
            formatting_type="PERCENT",
        )

    @property
    def goal20_abandons(self):
        return ReportingMetric(
            expression="ga:goal20Abandons",
            alias="Goal 20 Abandoned Funnels",
            formatting_type="INTEGER",
        )

    @property
    def goal20_abandon_rate(self):
        return ReportingMetric(
            expression="ga:goal20AbandonRate",
            alias="Goal 20 Abandonment Rate",
            formatting_type="PERCENT",
        )

    # Page Tracking
    @property
    def page_value(self):
        return ReportingMetric(
            expression="ga:pageValue", alias="Page Value", formatting_type="CURRENCY"
        )

    @property
    def entrances(self):
        return ReportingMetric(
            expression="ga:entrances", alias="Entrances", formatting_type="INTEGER"
        )

    @property
    def entrance_rate(self):
        return ReportingMetric(
            expression="ga:entranceRate",
            alias="Entrances / Pageviews",
            formatting_type="PERCENT",
        )

    @property
    def pageviews(self):
        return ReportingMetric(
            expression="ga:pageviews", alias="Pageviews", formatting_type="INTEGER"
        )

    @property
    def pageviews_per_session(self):
        return ReportingMetric(
            expression="ga:pageviewsPerSession",
            alias="Pages / Session",
            formatting_type="FLOAT",
        )

    @property
    def unique_pageviews(self):
        return ReportingMetric(
            expression="ga:uniquePageviews",
            alias="Unique Page Views",
            formatting_type="INTEGER",
        )

    @property
    def time_on_page(self):
        return ReportingMetric(
            expression="ga:timeOnPage", alias="Time on Page", formatting_type="TIME"
        )

    @property
    def exits(self):
        return ReportingMetric(
            expression="ga:exits", alias="Exits", formatting_type="INTEGER"
        )

    @property
    def avg_time_on_page(self):
        return ReportingMetric(
            expression="ga:avgTimeOnPage",
            alias="Avg. Time on Page",
            formatting_type="TIME",
        )

    @property
    def exit_rate(self):
        return ReportingMetric(
            expression="ga:exitRate", alias="% Exit", formatting_type="PERCENT"
        )


metrics = Metrics()
