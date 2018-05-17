"""Objects for dealing with Google Analaytics metrics sanely."""


class _Metric:
    """Class for dealing with Google Analytics metrics."""

    def __init__(self, expression=None, alias=None, formatting_type=None):
        self.expression = name
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
        name="ga:sessions",
        alias="Sessions",
        formatting_type="INTEGER"
    )
    bounces = _Metric(
        name="ga:bounces",
        alias="Bounces",
        formatting_type="INTEGER"
    )
    bounce_rate = _Metric(
        name="ga:bounceRate",
        alias="Bounce Rate",
        formatting_type="PERCENT"
    )
    session_duration = _Metric(
        name="ga:sessionDuration",
        alias="Session Duration",
        formatting_type="TIME"
    )
    avg_session_duration = _Metric(
        name="ga:avgSessionDuration",
        alias="Avg. Session Duration",
        formatting_type="TIME",
    )
    unique_dimensions_combination = _Metric(
        name="ga:uniqueDimensionCombinations",
        alias="Unique Dimension Combinations",
        formatting_type="INTEGER",
    )
    hits = _Metric(
        name="ga:hits",
        alias="Hits",
        formatting_type="INTEGER"
    )

    # Traffic Sources
    organic_searches = _Metric(
        name="ga:organicSearches",
        alias="Organic Searches",
        formatting_type="INTEGER"
    )

    # Adwords
    impressions = _Metric(
        name="ga:impressions",
        alias="Impressions",
        formatting_type="INTEGER"
    )
    ad_clicks = _Metric(
        name="ga:adClicks",
        alias="Clicks",
        formatting_type="INTEGER"
    )
    ad_cost = _Metric(
        name="ga:adCost",
        alias="Cost",
        formatting_type="CURRENCY"
    )
    cpm = _Metric(
        name="ga:CPM",
        alias="CPM",
        formatting_type="CURRENCY"
    )
    cpc = _Metric(
        name="ga:CPC",
        alias="CPC",
        formatting_type="CURRENCY"
    )
    ctr = _Metric(
        name="ga:CTR",
        alias="CTR",
        formatting_type="PERCENT"
    )
    cost_per_transaction = _Metric(
        name="ga:costPerTransaction",
        alias="Cost per Transaction",
        formatting_type="CURRENCY"
    )
    cost_per_conversion = _Metric(
        name="ga:costPerConversion",
        alias="Cost per Conversion",
        formatting_type="CURRENCY"
    )
    rpc = _Metric(
        name="ga:RPC",
        alias="RPC",
        formatting_type="CURRENCY"
    )
    roas = _Metric(
        name="ga:ROAS",
        alias="ROAS",
        formatting_type="CURRENCY"
    )

    # Goal Conversions (ALL)
    goal_stars_all = _Metric("ga:goalStartsAll")
    goal_completions_all = _Metric("ga:goalCompletionsAll")
    goal_value_all = _Metric("ga:goalValueAll")
    goal_value_per_session = _Metric("ga:goalValuePerSession")
    goal_conversion_rate_all = _Metric("ga:goalConversionRateAll")
    goal_abandons_all = _Metric("ga:goalAbandonsAll")
    goal_abandon_rate_all = _Metric("ga:goalAbandonRateAll")

    # Goal Conversions (Itemized)
    # Goal 01
    goal01_starts = _Metric("ga:goal01Starts")
    goal01_completions = _Metric("ga:goal01Completions")
    goal01_value = _Metric("ga:goal01Value")
    goal01_conversion_rate = _Metric("ga:goal01ConversionRate")
    goal01_abandons = _Metric("ga:goal01Abandons")
    goal01_abandon_rate = _Metric("ga:goal01AbandonRate")
    # Goal 02
    goal02_starts = _Metric("ga:goal02Starts")
    goal02_completions = _Metric("ga:goal02Completions")
    goal02_value = _Metric("ga:goal02Value")
    goal02_conversion_rate = _Metric("ga:goal02ConversionRate")
    goal02_abandons = _Metric("ga:goal02Abandons")
    goal02_abandon_rate = _Metric("ga:goal02AbandonRate")
    # Goal 03
    goal03_starts = _Metric("ga:goal03Starts")
    goal03_completions = _Metric("ga:goal03Completions")
    goal03_value = _Metric("ga:goal03Value")
    goal03_conversion_rate = _Metric("ga:goal03ConversionRate")
    goal03_abandons = _Metric("ga:goal03Abandons")
    goal03_abandon_rate = _Metric("ga:goal03AbandonRate")
    # Goal 04
    goal04_starts = _Metric("ga:goal04Starts")
    goal04_completions = _Metric("ga:goal04Completions")
    goal04_value = _Metric("ga:goal04Value")
    goal04_conversion_rate = _Metric("ga:goal04ConversionRate")
    goal04_abandons = _Metric("ga:goal04Abandons")
    goal04_abandon_rate = _Metric("ga:goal04AbandonRate")
    # Goal 05
    goal05_starts = _Metric("ga:goal05Starts")
    goal05_completions = _Metric("ga:goal05Completions")
    goal05_value = _Metric("ga:goal05Value")
    goal05_conversion_rate = _Metric("ga:goal05ConversionRate")
    goal05_abandons = _Metric("ga:goal05Abandons")
    goal05_abandon_rate = _Metric("ga:goal05AbandonRate")
    # Goal 06
    goal06_starts = _Metric("ga:goal06Starts")
    goal06_completions = _Metric("ga:goal06Completions")
    goal06_value = _Metric("ga:goal06Value")
    goal06_conversion_rate = _Metric("ga:goal06ConversionRate")
    goal06_abandons = _Metric("ga:goal06Abandons")
    goal06_abandon_rate = _Metric("ga:goal06AbandonRate")
    # Goal 07
    goal07_starts = _Metric("ga:goal07Starts")
    goal07_completions = _Metric("ga:goal07Completions")
    goal07_value = _Metric("ga:goal07Value")
    goal07_conversion_rate = _Metric("ga:goal07ConversionRate")
    goal07_abandons = _Metric("ga:goal07Abandons")
    goal07_abandon_rate = _Metric("ga:goal07AbandonRate")
    # Goal 08
    goal08_starts = _Metric("ga:goal08Starts")
    goal08_completions = _Metric("ga:goal08Completions")
    goal08_value = _Metric("ga:goal08Value")
    goal08_conversion_rate = _Metric("ga:goal08ConversionRate")
    goal08_abandons = _Metric("ga:goal08Abandons")
    goal08_abandon_rate = _Metric("ga:goal08AbandonRate")
    # Goal 09
    goal09_starts = _Metric("ga:goal09Starts")
    goal09_completions = _Metric("ga:goal09Completions")
    goal09_value = _Metric("ga:goal09Value")
    goal09_conversion_rate = _Metric("ga:goal09ConversionRate")
    goal09_abandons = _Metric("ga:goal09Abandons")
    goal09_abandon_rate = _Metric("ga:goal09AbandonRate")
    # Goal 10
    goal10_starts = _Metric("ga:goal10Starts")
    goal10_completions = _Metric("ga:goal10Completions")
    goal10_value = _Metric("ga:goal10Value")
    goal10_conversion_rate = _Metric("ga:goal10ConversionRate")
    goal10_abandons = _Metric("ga:goal10Abandons")
    goal10_abandon_rate = _Metric("ga:goal10AbandonRate")
    # Goal 11
    goal11_starts = _Metric("ga:goal11Starts")
    goal11_completions = _Metric("ga:goal11Completions")
    goal11_value = _Metric("ga:goal11Value")
    goal11_conversion_rate = _Metric("ga:goal11ConversionRate")
    goal11_abandons = _Metric("ga:goal11Abandons")
    goal11_abandon_rate = _Metric("ga:goal11AbandonRate")
    # Goal 12
    goal12_starts = _Metric("ga:goal12Starts")
    goal12_completions = _Metric("ga:goal12Completions")
    goal12_value = _Metric("ga:goal12Value")
    goal12_conversion_rate = _Metric("ga:goal12ConversionRate")
    goal12_abandons = _Metric("ga:goal12Abandons")
    goal12_abandon_rate = _Metric("ga:goal12AbandonRate")
    # Goal 13
    goal13_starts = _Metric("ga:goal13Starts")
    goal13_completions = _Metric("ga:goal13Completions")
    goal13_value = _Metric("ga:goal13Value")
    goal13_conversion_rate = _Metric("ga:goal13ConversionRate")
    goal13_abandons = _Metric("ga:goal13Abandons")
    goal13_abandon_rate = _Metric("ga:goal13AbandonRate")
    # Goal 14
    goal14_starts = _Metric("ga:goal14Starts")
    goal14_completions = _Metric("ga:goal14Completions")
    goal14_value = _Metric("ga:goal14Value")
    goal14_conversion_rate = _Metric("ga:goal14ConversionRate")
    goal14_abandons = _Metric("ga:goal14Abandons")
    goal14_abandon_rate = _Metric("ga:goal14AbandonRate")
    # Goal 15
    goal15_starts = _Metric("ga:goal15Starts")
    goal15_completions = _Metric("ga:goal15Completions")
    goal15_value = _Metric("ga:goal15Value")
    goal15_conversion_rate = _Metric("ga:goal15ConversionRate")
    goal15_abandons = _Metric("ga:goal15Abandons")
    goal15_abandon_rate = _Metric("ga:goal15AbandonRate")
    # Goal 16
    goal16_starts = _Metric("ga:goal16Starts")
    goal16_completions = _Metric("ga:goal16Completions")
    goal16_value = _Metric("ga:goal16Value")
    goal16_conversion_rate = _Metric("ga:goal16ConversionRate")
    goal16_abandons = _Metric("ga:goal16Abandons")
    goal16_abandon_rate = _Metric("ga:goal16AbandonRate")
    # Goal 17
    goal17_starts = _Metric("ga:goal17Starts")
    goal17_completions = _Metric("ga:goal17Completions")
    goal17_value = _Metric("ga:goal17Value")
    goal17_conversion_rate = _Metric("ga:goal17ConversionRate")
    goal17_abandons = _Metric("ga:goal17Abandons")
    goal17_abandon_rate = _Metric("ga:goal17AbandonRate")
    # Goal 18
    goal18_starts = _Metric("ga:goal18Starts")
    goal18_completions = _Metric("ga:goal18Completions")
    goal18_value = _Metric("ga:goal18Value")
    goal18_conversion_rate = _Metric("ga:goal18ConversionRate")
    goal18_abandons = _Metric("ga:goal18Abandons")
    goal18_abandon_rate = _Metric("ga:goal18AbandonRate")
    # Goal 19
    goal19_starts = _Metric("ga:goal19Starts")
    goal19_completions = _Metric("ga:goal19Completions")
    goal19_value = _Metric("ga:goal19Value")
    goal19_conversion_rate = _Metric("ga:goal19ConversionRate")
    goal19_abandons = _Metric("ga:goal19Abandons")
    goal19_abandon_rate = _Metric("ga:goal19AbandonRate")
    # Goal 20
    goal20_starts = _Metric("ga:goal20Starts")
    goal20_completions = _Metric("ga:goal20Completions")
    goal20_value = _Metric("ga:goal20Value")
    goal20_conversion_rate = _Metric("ga:goal20ConversionRate")
    goal20_abandons = _Metric("ga:goal20Abandons")
    goal20_abandon_rate = _Metric("ga:goal20AbandonRate")

    # Page Tracking
    page_value = _Metric("ga:pageValue")
    entrances = _Metric("ga:entrances")
    entrance_rate = _Metric("ga:entranceRate")
    page_previews = _Metric("ga:pagePreviews")
    pageviews = _Metric("ga:pageviews")
    pageviews_per_session = _Metric("ga:pageviewsPerSession")
    unique_pageviews = _Metric("ga:uniquePageviews")
    time_on_page = _Metric("ga:timeOnPage")
    exits = _Metric("ga:exits")
    exit_rate = _Metric("ga:exitRate")


metrics = _Metrics()
