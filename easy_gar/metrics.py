"""Objects for dealing with Google Analaytics metrics sanely."""


class _Metric:
    """Class for dealing with Google Analytics metrics."""

    def __init__(self, expression=None, alias=None, formatting_type=None):
        self.expression = expression
        self.alias = alias
        self.formatting_type = formatting_type

    def __repr__(self, alias=None, formatting_type=None):
        """Repr string for class."""
        return f"{self.__class__.__name__}({self.expression}, {self.alias}, {self.formatting_type})"

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
        return _Metric(expression=f"({self})+{other}")

    def __sub__(self, other):
        """Metric subtraction."""
        return _Metric(expression=f"({self})-{other}")

    def __mul__(self, other):
        """Metric multiplication."""
        return _Metric(expression=f"({self})*{other}")

    def __truediv__(self, other):
        """Metric division."""
        return _Metric(expression=f"({self})/{other}", formatting_type="FLOAT")


class _Metrics:
    """Google Analytics Metrics for use with the API class."""

    # Users
    users = _Metric(
        expression="ga:users",
        alias="Users",
        formatting_type="INTEGER"
    )
    new_users = _Metric(
        expression="ga:newUsers",
        alias="New Users",
        formatting_type="INTEGER"
    )
    users_1d = _Metric(
        expression="ga:1dayUsers",
        alias="1 Day Active Users",
        formatting_type="INTEGER"
    )
    users_7d = _Metric(
        expression="ga:7dayUsers",
        alias="7 Day Active Users",
        formatting_type="INTEGER"
    )
    users_14d = _Metric(
        expression="ga:14dayUsers",
        alias="14 Day Active Users",
        formatting_type="INTEGER",
    )
    users_28d = _Metric(
        expression="ga:28dayUsers",
        alias="28 Day Active Users",
        formatting_type="INTEGER",
    )
    users_30d = _Metric(
        expression="ga:30dayUsers",
        alias="30 Day Active Users",
        formatting_type="INTEGER",
    )
    sessions_per_user = _Metric(
        expression="ga:sessionsPerUser",
        alias="Sessions per User",
        formatting_type="FLOAT",
    )
    percent_new_sessions = _Metric(
        expression="ga:percentNewSessions",
        alias="% New Sessions",
        formatting_type="PERCENT",
    )

    # Sessions
    sessions = _Metric(
        expression="ga:sessions",
        alias="Sessions",
        formatting_type="INTEGER"
    )
    bounces = _Metric(
        expression="ga:bounces",
        alias="Bounces",
        formatting_type="INTEGER"
    )
    bounce_rate = _Metric(
        expression="ga:bounceRate",
        alias="Bounce Rate",
        formatting_type="PERCENT"
    )
    session_duration = _Metric(
        expression="ga:sessionDuration",
        alias="Session Duration",
        formatting_type="TIME"
    )
    avg_session_duration = _Metric(
        expression="ga:avgSessionDuration",
        alias="Avg. Session Duration",
        formatting_type="TIME",
    )
    unique_dimensions_combination = _Metric(
        expression="ga:uniqueDimensionCombinations",
        alias="Unique Dimension Combinations",
        formatting_type="INTEGER",
    )
    hits = _Metric(
        expression="ga:hits",
        alias="Hits",
        formatting_type="INTEGER"
    )

    # Traffic Sources
    organic_searches = _Metric(
        expression="ga:organicSearches",
        alias="Organic Searches",
        formatting_type="INTEGER"
    )

    # Adwords
    impressions = _Metric(
        expression="ga:impressions",
        alias="Impressions",
        formatting_type="INTEGER"
    )
    ad_clicks = _Metric(
        expression="ga:adClicks",
        alias="Clicks",
        formatting_type="INTEGER"
    )
    ad_cost = _Metric(
        expression="ga:adCost",
        alias="Cost",
        formatting_type="CURRENCY"
    )
    cpm = _Metric(
        expression="ga:CPM",
        alias="CPM",
        formatting_type="CURRENCY"
    )
    cpc = _Metric(
        expression="ga:CPC",
        alias="CPC",
        formatting_type="CURRENCY"
    )
    ctr = _Metric(
        expression="ga:CTR",
        alias="CTR",
        formatting_type="PERCENT"
    )
    cost_per_transaction = _Metric(
        expression="ga:costPerTransaction",
        alias="Cost per Transaction",
        formatting_type="CURRENCY"
    )
    cost_per_conversion = _Metric(
        expression="ga:costPerConversion",
        alias="Cost per Conversion",
        formatting_type="CURRENCY"
    )
    rpc = _Metric(
        expression="ga:RPC",
        alias="RPC",
        formatting_type="CURRENCY"
    )
    roas = _Metric(
        expression="ga:ROAS",
        alias="ROAS",
        formatting_type="CURRENCY"
    )

    # Goal Conversions (ALL)
    goal_stars_all = _Metric(
        expression="ga:goalStartsAll",
        alias="Goal Starts",
        formatting_type="INTEGER"
    )
    goal_completions_all = _Metric(
        expression="ga:goalCompletionsAll",
        alias="Goal Completions",
        formatting_type="INTEGER"
    )
    goal_value_all = _Metric(
        expression="ga:goalValueAll",
        alias="Goal Value",
        formatting_type="CURRENCY"
    )
    goal_value_per_session = _Metric(
        expression="ga:goalValuePerSession",
        alias="Per Session Goal Value",
        formatting_type="CURRENCY"
    )
    goal_conversion_rate_all = _Metric(
        expression="ga:goalConversionRateAll",
        alias="Goal Conversion Rate",
        formatting_type="PERCENT"
    )
    goal_abandons_all = _Metric(
        expression="ga:goalAbandonsAll",
        alias="Abandoned Funnels",
        formatting_type="INTEGER")
    goal_abandon_rate_all = _Metric(
        expression="ga:goalAbandonRateAll",
        alias="Total Abondonment Rate",
        formatting_type="PERCENT"
    )

    # Goal Conversions (Itemized)
    # Goal 01
    goal01_starts = _Metric(
        expression="ga:goal01Starts",
        alias="Goal 01 Starts",
        formatting_type="INTEGER"
    )
    goal01_completions = _Metric(
        expression="ga:goal01Completions",
        alias="Goal 01 Completions",
        formatting_type="INTEGER")
    goal01_value = _Metric(
        expression="ga:goal01Value",
        alias="Goal 01 Value",
        formatting_type="CURRENCY"
    )
    goal01_conversion_rate = _Metric(
        expression="ga:goal01ConversionRate",
        alias="Goal 01 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal01_abandons = _Metric(
        expression="ga:goal01Abandons",
        alias="Goal 01 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal01_abandon_rate = _Metric(
        expression="ga:goal01AbandonRate",
        alias="Goal 01 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 02
    goal02_starts = _Metric(
        expression="ga:goal02Starts",
        alias="Goal 02 Starts",
        formatting_type="INTEGER"
    )
    goal02_completions = _Metric(
        expression="ga:goal02Completions",
        alias="Goal 02 Completions",
        formatting_type="INTEGER")
    goal02_value = _Metric(
        expression="ga:goal02Value",
        alias="Goal 02 Value",
        formatting_type="CURRENCY"
    )
    goal02_conversion_rate = _Metric(
        expression="ga:goal02ConversionRate",
        alias="Goal 02 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal02_abandons = _Metric(
        expression="ga:goal02Abandons",
        alias="Goal 02 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal02_abandon_rate = _Metric(
        expression="ga:goal02AbandonRate",
        alias="Goal 02 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 03
    goal03_starts = _Metric(
        expression="ga:goal03Starts",
        alias="Goal 03 Starts",
        formatting_type="INTEGER"
    )
    goal03_completions = _Metric(
        expression="ga:goal03Completions",
        alias="Goal 03 Completions",
        formatting_type="INTEGER")
    goal03_value = _Metric(
        expression="ga:goal03Value",
        alias="Goal 03 Value",
        formatting_type="CURRENCY"
    )
    goal03_conversion_rate = _Metric(
        expression="ga:goal03ConversionRate",
        alias="Goal 03 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal03_abandons = _Metric(
        expression="ga:goal03Abandons",
        alias="Goal 03 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal03_abandon_rate = _Metric(
        expression="ga:goal03AbandonRate",
        alias="Goal 03 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 04
    goal04_starts = _Metric(
        expression="ga:goal04Starts",
        alias="Goal 04 Starts",
        formatting_type="INTEGER"
    )
    goal04_completions = _Metric(
        expression="ga:goal04Completions",
        alias="Goal 04 Completions",
        formatting_type="INTEGER")
    goal04_value = _Metric(
        expression="ga:goal04Value",
        alias="Goal 04 Value",
        formatting_type="CURRENCY"
    )
    goal04_conversion_rate = _Metric(
        expression="ga:goal04ConversionRate",
        alias="Goal 04 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal04_abandons = _Metric(
        expression="ga:goal04Abandons",
        alias="Goal 04 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal04_abandon_rate = _Metric(
        expression="ga:goal04AbandonRate",
        alias="Goal 04 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 05
    goal05_starts = _Metric(
        expression="ga:goal05Starts",
        alias="Goal 05 Starts",
        formatting_type="INTEGER"
    )
    goal05_completions = _Metric(
        expression="ga:goal05Completions",
        alias="Goal 05 Completions",
        formatting_type="INTEGER")
    goal05_value = _Metric(
        expression="ga:goal05Value",
        alias="Goal 05 Value",
        formatting_type="CURRENCY"
    )
    goal05_conversion_rate = _Metric(
        expression="ga:goal05ConversionRate",
        alias="Goal 05 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal05_abandons = _Metric(
        expression="ga:goal05Abandons",
        alias="Goal 05 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal05_abandon_rate = _Metric(
        expression="ga:goal05AbandonRate",
        alias="Goal 05 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 06
    goal06_starts = _Metric(
        expression="ga:goal06Starts",
        alias="Goal 06 Starts",
        formatting_type="INTEGER"
    )
    goal06_completions = _Metric(
        expression="ga:goal06Completions",
        alias="Goal 06 Completions",
        formatting_type="INTEGER")
    goal06_value = _Metric(
        expression="ga:goal06Value",
        alias="Goal 06 Value",
        formatting_type="CURRENCY"
    )
    goal06_conversion_rate = _Metric(
        expression="ga:goal06ConversionRate",
        alias="Goal 06 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal06_abandons = _Metric(
        expression="ga:goal06Abandons",
        alias="Goal 06 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal06_abandon_rate = _Metric(
        expression="ga:goal06AbandonRate",
        alias="Goal 06 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 07
    goal07_starts = _Metric(
        expression="ga:goal07Starts",
        alias="Goal 07 Starts",
        formatting_type="INTEGER"
    )
    goal07_completions = _Metric(
        expression="ga:goal07Completions",
        alias="Goal 07 Completions",
        formatting_type="INTEGER")
    goal07_value = _Metric(
        expression="ga:goal07Value",
        alias="Goal 07 Value",
        formatting_type="CURRENCY"
    )
    goal07_conversion_rate = _Metric(
        expression="ga:goal07ConversionRate",
        alias="Goal 07 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal07_abandons = _Metric(
        expression="ga:goal07Abandons",
        alias="Goal 07 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal07_abandon_rate = _Metric(
        expression="ga:goal07AbandonRate",
        alias="Goal 07 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 08
    goal08_starts = _Metric(
        expression="ga:goal08Starts",
        alias="Goal 08 Starts",
        formatting_type="INTEGER"
    )
    goal08_completions = _Metric(
        expression="ga:goal08Completions",
        alias="Goal 08 Completions",
        formatting_type="INTEGER")
    goal08_value = _Metric(
        expression="ga:goal08Value",
        alias="Goal 08 Value",
        formatting_type="CURRENCY"
    )
    goal08_conversion_rate = _Metric(
        expression="ga:goal08ConversionRate",
        alias="Goal 08 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal08_abandons = _Metric(
        expression="ga:goal08Abandons",
        alias="Goal 08 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal08_abandon_rate = _Metric(
        expression="ga:goal08AbandonRate",
        alias="Goal 08 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 09
    goal09_starts = _Metric(
        expression="ga:goal09Starts",
        alias="Goal 09 Starts",
        formatting_type="INTEGER"
    )
    goal09_completions = _Metric(
        expression="ga:goal09Completions",
        alias="Goal 09 Completions",
        formatting_type="INTEGER")
    goal09_value = _Metric(
        expression="ga:goal09Value",
        alias="Goal 09 Value",
        formatting_type="CURRENCY"
    )
    goal09_conversion_rate = _Metric(
        expression="ga:goal09ConversionRate",
        alias="Goal 09 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal09_abandons = _Metric(
        expression="ga:goal09Abandons",
        alias="Goal 09 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal09_abandon_rate = _Metric(
        expression="ga:goal09AbandonRate",
        alias="Goal 09 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 10
    goal10_starts = _Metric(
        expression="ga:goal10Starts",
        alias="Goal 10 Starts",
        formatting_type="INTEGER"
    )
    goal10_completions = _Metric(
        expression="ga:goal10Completions",
        alias="Goal 10 Completions",
        formatting_type="INTEGER")
    goal10_value = _Metric(
        expression="ga:goal10Value",
        alias="Goal 10 Value",
        formatting_type="CURRENCY"
    )
    goal10_conversion_rate = _Metric(
        expression="ga:goal10ConversionRate",
        alias="Goal 10 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal10_abandons = _Metric(
        expression="ga:goal10Abandons",
        alias="Goal 10 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal10_abandon_rate = _Metric(
        expression="ga:goal10AbandonRate",
        alias="Goal 10 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 11
    goal11_starts = _Metric(
        expression="ga:goal11Starts",
        alias="Goal 11 Starts",
        formatting_type="INTEGER"
    )
    goal11_completions = _Metric(
        expression="ga:goal11Completions",
        alias="Goal 11 Completions",
        formatting_type="INTEGER")
    goal11_value = _Metric(
        expression="ga:goal11Value",
        alias="Goal 11 Value",
        formatting_type="CURRENCY"
    )
    goal11_conversion_rate = _Metric(
        expression="ga:goal11ConversionRate",
        alias="Goal 11 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal11_abandons = _Metric(
        expression="ga:goal11Abandons",
        alias="Goal 11 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal11_abandon_rate = _Metric(
        expression="ga:goal11AbandonRate",
        alias="Goal 11 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 12
    goal12_starts = _Metric(
        expression="ga:goal12Starts",
        alias="Goal 12 Starts",
        formatting_type="INTEGER"
    )
    goal12_completions = _Metric(
        expression="ga:goal12Completions",
        alias="Goal 12 Completions",
        formatting_type="INTEGER")
    goal12_value = _Metric(
        expression="ga:goal12Value",
        alias="Goal 12 Value",
        formatting_type="CURRENCY"
    )
    goal12_conversion_rate = _Metric(
        expression="ga:goal12ConversionRate",
        alias="Goal 12 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal12_abandons = _Metric(
        expression="ga:goal12Abandons",
        alias="Goal 12 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal12_abandon_rate = _Metric(
        expression="ga:goal12AbandonRate",
        alias="Goal 12 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 13
    goal13_starts = _Metric(
        expression="ga:goal13Starts",
        alias="Goal 13 Starts",
        formatting_type="INTEGER"
    )
    goal13_completions = _Metric(
        expression="ga:goal13Completions",
        alias="Goal 13 Completions",
        formatting_type="INTEGER")
    goal13_value = _Metric(
        expression="ga:goal13Value",
        alias="Goal 13 Value",
        formatting_type="CURRENCY"
    )
    goal13_conversion_rate = _Metric(
        expression="ga:goal13ConversionRate",
        alias="Goal 13 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal13_abandons = _Metric(
        expression="ga:goal13Abandons",
        alias="Goal 13 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal13_abandon_rate = _Metric(
        expression="ga:goal13AbandonRate",
        alias="Goal 13 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 14
    goal14_starts = _Metric(
        expression="ga:goal14Starts",
        alias="Goal 14 Starts",
        formatting_type="INTEGER"
    )
    goal14_completions = _Metric(
        expression="ga:goal14Completions",
        alias="Goal 14 Completions",
        formatting_type="INTEGER")
    goal14_value = _Metric(
        expression="ga:goal14Value",
        alias="Goal 14 Value",
        formatting_type="CURRENCY"
    )
    goal14_conversion_rate = _Metric(
        expression="ga:goal14ConversionRate",
        alias="Goal 14 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal14_abandons = _Metric(
        expression="ga:goal14Abandons",
        alias="Goal 14 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal14_abandon_rate = _Metric(
        expression="ga:goal14AbandonRate",
        alias="Goal 14 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 15
    goal15_starts = _Metric(
        expression="ga:goal15Starts",
        alias="Goal 15 Starts",
        formatting_type="INTEGER"
    )
    goal15_completions = _Metric(
        expression="ga:goal15Completions",
        alias="Goal 15 Completions",
        formatting_type="INTEGER")
    goal15_value = _Metric(
        expression="ga:goal15Value",
        alias="Goal 15 Value",
        formatting_type="CURRENCY"
    )
    goal15_conversion_rate = _Metric(
        expression="ga:goal15ConversionRate",
        alias="Goal 15 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal15_abandons = _Metric(
        expression="ga:goal15Abandons",
        alias="Goal 15 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal15_abandon_rate = _Metric(
        expression="ga:goal15AbandonRate",
        alias="Goal 15 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 16
    goal16_starts = _Metric(
        expression="ga:goal16Starts",
        alias="Goal 16 Starts",
        formatting_type="INTEGER"
    )
    goal16_completions = _Metric(
        expression="ga:goal16Completions",
        alias="Goal 16 Completions",
        formatting_type="INTEGER")
    goal16_value = _Metric(
        expression="ga:goal16Value",
        alias="Goal 16 Value",
        formatting_type="CURRENCY"
    )
    goal16_conversion_rate = _Metric(
        expression="ga:goal16ConversionRate",
        alias="Goal 16 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal16_abandons = _Metric(
        expression="ga:goal16Abandons",
        alias="Goal 16 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal16_abandon_rate = _Metric(
        expression="ga:goal16AbandonRate",
        alias="Goal 16 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 17
    goal17_starts = _Metric(
        expression="ga:goal17Starts",
        alias="Goal 17 Starts",
        formatting_type="INTEGER"
    )
    goal17_completions = _Metric(
        expression="ga:goal17Completions",
        alias="Goal 17 Completions",
        formatting_type="INTEGER")
    goal17_value = _Metric(
        expression="ga:goal17Value",
        alias="Goal 17 Value",
        formatting_type="CURRENCY"
    )
    goal17_conversion_rate = _Metric(
        expression="ga:goal17ConversionRate",
        alias="Goal 17 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal17_abandons = _Metric(
        expression="ga:goal17Abandons",
        alias="Goal 17 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal17_abandon_rate = _Metric(
        expression="ga:goal17AbandonRate",
        alias="Goal 17 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 18
    goal18_starts = _Metric(
        expression="ga:goal18Starts",
        alias="Goal 18 Starts",
        formatting_type="INTEGER"
    )
    goal18_completions = _Metric(
        expression="ga:goal18Completions",
        alias="Goal 18 Completions",
        formatting_type="INTEGER")
    goal18_value = _Metric(
        expression="ga:goal18Value",
        alias="Goal 18 Value",
        formatting_type="CURRENCY"
    )
    goal18_conversion_rate = _Metric(
        expression="ga:goal18ConversionRate",
        alias="Goal 18 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal18_abandons = _Metric(
        expression="ga:goal18Abandons",
        alias="Goal 18 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal18_abandon_rate = _Metric(
        expression="ga:goal18AbandonRate",
        alias="Goal 18 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 19
    goal19_starts = _Metric(
        expression="ga:goal19Starts",
        alias="Goal 19 Starts",
        formatting_type="INTEGER"
    )
    goal19_completions = _Metric(
        expression="ga:goal19Completions",
        alias="Goal 19 Completions",
        formatting_type="INTEGER")
    goal19_value = _Metric(
        expression="ga:goal19Value",
        alias="Goal 19 Value",
        formatting_type="CURRENCY"
    )
    goal19_conversion_rate = _Metric(
        expression="ga:goal19ConversionRate",
        alias="Goal 19 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal19_abandons = _Metric(
        expression="ga:goal19Abandons",
        alias="Goal 19 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal19_abandon_rate = _Metric(
        expression="ga:goal19AbandonRate",
        alias="Goal 19 Abandonment Rate",
        formatting_type="PERCENT"
    )
    # Goal 20
    goal20_starts = _Metric(
        expression="ga:goal20Starts",
        alias="Goal 20 Starts",
        formatting_type="INTEGER"
    )
    goal20_completions = _Metric(
        expression="ga:goal20Completions",
        alias="Goal 20 Completions",
        formatting_type="INTEGER")
    goal20_value = _Metric(
        expression="ga:goal20Value",
        alias="Goal 20 Value",
        formatting_type="CURRENCY"
    )
    goal20_conversion_rate = _Metric(
        expression="ga:goal20ConversionRate",
        alias="Goal 20 Conversion Rate",
        formatting_type="PERCENT"
    )
    goal20_abandons = _Metric(
        expression="ga:goal20Abandons",
        alias="Goal 20 Abandoned Funnels",
        formatting_type="INTEGER"
    )
    goal20_abandon_rate = _Metric(
        expression="ga:goal20AbandonRate",
        alias="Goal 20 Abandonment Rate",
        formatting_type="PERCENT"
    )

    # Page Tracking
    page_value = _Metric(
        expression="ga:pageValue",
        alias="Page Value",
        formatting_type="CURRENCY"
    )
    entrances = _Metric(
        expression="ga:entrances",
        alias="Entrances",
        formatting_type="INTEGER"
    )
    entrance_rate = _Metric(
        expression="ga:entranceRate",
        alias="Entrances / Pageviews",
        formatting_type="PERCENT"
    )
    pageviews = _Metric(
        expression="ga:pageviews",
        alias="Pageviews",
        formatting_type="INTEGER"
    )
    pageviews_per_session = _Metric(
        expression="ga:pageviewsPerSession",
        alias="Pages / Session",
        formatting_type="FLOAT"
    )
    unique_pageviews = _Metric(
        expression="ga:uniquePageviews",
        alias="Unique Page Views",
        formatting_type="INTEGER"
    )
    time_on_page = _Metric(
        expression="ga:timeOnPage",
        alias="Time on Page",
        formatting_type="TIME"
    )
    exits = _Metric(
        expression="ga:exits",
        alias="Exits",
        formatting_type="INTEGER"
    )
    avg_time_on_page = _Metric(
        expression="ga:avgTimeOnPage",
        alias="Avg. Time on Page",
        formatting_type="TIME"
    )
    exit_rate = _Metric(
        expression="ga:exitRate",
        alias="% Exit",
        formatting_type="PERCENT"
    )


metrics = _Metrics()
