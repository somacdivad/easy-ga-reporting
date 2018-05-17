"""Objects for dealing with Google Analaytics metrics sanely."""

from collections import namedtuple


class _Metric(namedtuple("Metric", ["name"])):
    """Class for dealing with Google Analytics metrics."""

    __slots__ = ()

    def __repr__(self):
        """Repr string for class."""
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        """String representation of metric name."""
        return f"{self.name}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"expression": str(self)}

    def __add__(self, other):
        """Metric addition."""
        return _Metric(f"({self})+{other}")

    def __sub__(self, other):
        """Metric subtraction."""
        return _Metric(f"({self})-{other}")

    def __mul__(self, other):
        """Metric multiplication."""
        return _Metric(f"({self})*{other}")

    def __truediv__(self, other):
        """Metric division."""
        return _Metric(f"({self})/{other}")


class _Metrics:
    """Google Analytics Metrics for use with the API class."""

    # Users
    users = _Metric("ga:users")
    new_users = _Metric("ga:newUsers")
    users_1d = _Metric("ga:1dayUsers")
    users_7d = _Metric("ga:7dayUsers")
    users_14d = _Metric("ga:14dayUsers")
    users_28d = _Metric("ga:28dayUsers")
    users_30d = _Metric("ga:30dayUsers")
    sessions_per_user = _Metric("ga:sessionsPerUser")

    # Sessions
    sessions = _Metric("ga:sessions")
    bounces = _Metric("ga:bounces")
    bounce_rate = _Metric("ga:bounceRate")
    session_duration = _Metric("ga:sessionDuration")
    avg_session_duration = _Metric("ga:avgSessionDuration")
    unique_dimensions_combination = _Metric("ga:uniqueDimensionCombinations")
    hits = _Metric("ga:hits")

    # Traffic Sources
    organic_searches = _Metric("ga:organicSearches")

    # Adwords
    impressions = _Metric("ga:impressions")
    ad_clicks = _Metric("ga:adClicks")
    ad_cost = _Metric("ga:adCost")
    cpm = _Metric("ga:CPM")
    cpc = _Metric("ga:CPC")
    ctr = _Metric("ga:CTR")
    cost_per_transaction = _Metric("ga:costPerTransaction")
    cost_per_conversion = _Metric("ga:costPerConversion")
    rpc = _Metric("ga:RPC")
    roas = _Metric("ga:ROAS")

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
