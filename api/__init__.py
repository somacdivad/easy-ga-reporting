"""Google Analytics API object."""

from collections import namedtuple

from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

__all__ = [
    'API',
    'Dimension',
]

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')


class Dimension(namedtuple('Dimension', ['name'])):
    """Google Analytics Dimension class."""

    __slots__ = ()

    def __repr__(self):
        """Repr string for class."""
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self):
        """String representation of dimension name."""
        return f'ga:{self.name}'

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {'name': str(self)}


class Metric(namedtuple('Metric', ['name'])):
    """Google Analytics Metric class."""

    __slots__ = ()

    def __repr__(self):
        """Repr string for class."""
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self):
        """String representation of metric name."""
        return f'ga:{self.name}'

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {'expression': str(self)}

    def __add__(self, other):
        """Metric addition."""
        return Metric(f'{self}+{other}')

    def __sub__(self, other):
        """Metric subtraction."""
        return Metric(f'{self}-{other}')

    def __mul__(self, other):
        """Metric multiplication."""
        return Metric(f'{self}*{other}')

    def __truediv__(self, other):
        """Metric division."""
        return Metric(f'{self}/{other}')


class Dimensions:
    """Google Analytics Dimensions for use with the API class."""

    # Users
    user_type = Dimension('userType')
    session_count = Dimension('sessionCount')
    days_since_last_session = Dimension('daysSinceLastSession')
    user_defined_value = Dimension('userDefinedValue')
    user_bucket = Dimension('userBucket')

    # Sessions
    session_duration_bucket = Dimension('sessionDurationBucket')

    # Traffic Sources
    referral_path = Dimension('referralPath')
    full_referrer = Dimension('fullReferrer')
    campaign = Dimension('campaign')
    source = Dimension('source')
    medium = Dimension('medium')
    source_medium = Dimension('sourceMedium')
    keyword = Dimension('keyword')
    ad_content = Dimension('adContent')
    social_network = Dimension('socialNetwork')
    has_social_source_referral = Dimension('hasSocialSourceReferral')
    campaign_code = Dimension('campaignCode')

    # AdWords
    ad_group = Dimension('adGroup')
    ad_slot = Dimension('adSlot')
    ad_distribution_network = Dimension('adDistributionNetwork')
    ad_match_type = Dimension('adMatchType')
    ad_keyword_match_type = Dimension('adKeywordMatchType')
    ad_matched_query = Dimension('adMatchedQuery')
    ad_placement_domain = Dimension('adPlacementDomain')
    ad_placement_url = Dimension('adPlacementUrl')
    ad_format = Dimension('adFormat')
    ad_targeting_type = Dimension('adTargetingType')
    ad_targeting_option = Dimension('adTargetingOption')
    ad_display_url = Dimension('adDisplayUrl')
    ad_destination_url = Dimension('adDestinationUrl')
    adwords_customer_id = Dimension('adwordsCustomerID')
    adwords_campaign_id = Dimension('adwordsCampaignID')
    adwords_ad_group_id = Dimension('adwordsAdGroupID')
    adwords_creative_id = Dimension('adwordsCreativeID')
    adwords_criterial_id = Dimension('adwordsCriterialsID')
    ad_query_word_count = Dimension('adQueryWordCount')
    is_true_video_view_ad = Dimension('isTrueViewVideoAd')

    # Goal Conversions
    goal_completion_location = Dimension('goalCompletionLocation')
    goal_previous_step1 = Dimension('goalPreviousStep1')
    goal_previous_step2 = Dimension('goalPreviousStep2')
    goal_previous_step3 = Dimension('goalPreviousStep3')

    # Platform or Device
    browser = Dimension('browser')
    browser_version = Dimension('browserVersion')
    os = Dimension('operatingSystem')
    os_version = Dimension('operatingSystemVersion')
    mobile_branding = Dimension('mobileDeviceBranding')
    mobile_model = Dimension('mobileDeviceModel')
    mobile_input_selector = Dimension('mobileInputSelector')
    mobile_info = Dimension('mobileDeviceInfo')
    mobile_marketing_name = Dimension('mobileDeviceMarketingName')
    device_category = Dimension('deviceCategory')
    browser_size = Dimension('browserSize')
    data_source = Dimension('dataSource')

    # Geo Network
    continent = Dimension('continent')
    subcontinent = Dimension('subContinent')
    country = Dimension('country')
    region = Dimension('region')
    metro = Dimension('metro')
    city = Dimension('city')
    latitude = Dimension('latitude')
    longitude = Dimension('longitude')
    network_domain = Dimension('networkDomain')
    network_location = Dimension('networkLocation')
    city_id = Dimension('cityId')
    country_iso_code = Dimension('countryIsoCode')
    metro_id = Dimension('metroId')
    region_id = Dimension('regionId')
    region_iso_code = Dimension('regionIsoCode')
    subcontinent_code = Dimension('subContenentCode')

    # System
    flash_version = Dimension('flashVersion')
    java_enabled = Dimension('javaEnabled')
    language = Dimension('language')
    screen_colors = Dimension('screenColors')
    source_property_display_name = Dimension('sourcePropertyDisplayName')
    source_property_tracking_id = Dimension('sourcePropertyTrackingId')
    screen_resolution = Dimension('screenResolution')

    # Page Tracking
    hostname = Dimension('hostname')
    page_path = Dimension('pagePath')
    page_path_level1 = Dimension('pagePathLevel1')
    page_path_level2 = Dimension('pagePathLevel2')
    page_path_level3 = Dimension('pagePathLevel3')
    page_path_level4 = Dimension('pagePathLevel4')
    page_title = Dimension('pageTitle')
    landing_path_path = Dimension('landingPagePath')
    second_page_path = Dimension('secondPagePath')
    exit_page_path = Dimension('exitPagePath')
    previous_page_path = Dimension('previousPagePath')
    page_depth = Dimension('pageDepth')

    # Time
    date = Dimension('date')
    year = Dimension('year')
    month = Dimension('month')
    week = Dimension('week')
    day = Dimension('day')
    hour = Dimension('hour')
    minute = Dimension('minute')
    nth_month = Dimension('nthMonth')
    nth_week = Dimension('nthWeek')
    nth_day = Dimension('nthDay')
    nth_minute = Dimension('nthMinute')
    day_of_week = Dimension('dayOfWeek')
    day_of_week_name = Dimension('dayOfWeekName')
    date_hour = Dimension('dateHour')
    date_hour_minute = Dimension('dateHourMinute')
    year_month = Dimension('yearMonth')
    ga_year_week = Dimension('yearWeek')
    iso_week = Dimension('isoWeek')
    iso_year = Dimension('isoYear')
    iso_year_iso_week = Dimension('isoYearIsoWeek')
    nth_hour = Dimension('nthHour')

    # Audience
    user_age_bracket = Dimension('userAgeBracket')
    user_gender = Dimension('userGender')
    interest_other_category = Dimension('interestOtherCategory')
    interest_affinity_category = Dimension('interestAffinityCategory')
    interest_in_market_category = Dimension('interestInMarketCategory')


class Metrics:
    """Google Analytics Metrics for use with the API class."""

    # Users
    users = Metric('users')
    new_users = Metric('newUsers')
    users_1d = Metric('1dayUsers')
    users_7d = Metric('7dayUsers')
    users_14d = Metric('14dayUsers')
    users_28d = Metric('28dayUsers')
    users_30d = Metric('30dayUsers')
    sessions_per_user = Metric('sessionsPerUser')

    # Sessions
    sessions = Metric('sessions')
    bounces = Metric('bounces')
    bounce_rate = Metric('bounceRate')
    session_duration = Metric('sessionDuration')
    avg_session_duration = Metric('avgSessionDuration')
    unique_dimensions_combination = Metric('uniqueDimensionCombinations')
    hits = Metric('hits')

    # Traffic Sources
    organic_searches = Metric('organicSearches')

    # Adwords
    impressions = Metric('impressions')
    ad_clicks = Metric('adClicks')
    ad_cost = Metric('adCost')
    cpm = Metric('CPM')
    cpc = Metric('CPC')
    ctr = Metric('CTR')
    cost_per_transaction = Metric('costPerTransaction')
    cost_per_conversion = Metric('costPerConversion')
    rpc = Metric('RPC')
    roas = Metric('ROAS')

    # Goal Conversions (ALL)
    goal_stars_all = Metric('goalStartsAll')
    goal_completions_all = Metric('goalCompletionsAll')
    goal_value_all = Metric('goalValueAll')
    goal_value_per_session = Metric('goalValuePerSession')
    goal_conversion_rate_all = Metric('goalConversionRateAll')
    goal_abandons_all = Metric('goalAbandonsAll')
    goal_abandon_rate_all = Metric('goalAbandonRateAll')

    # Goal Conversions (Itemized)
    # Goal 01
    goal01_starts = Metric('goal01Starts')
    goal01_completions = Metric('goal01Completions')
    goal01_value = Metric('goal01Value')
    goal01_conversion_rate = Metric('goal01ConversionRate')
    goal01_abandons = Metric('goal01Abandons')
    goal01_abandon_rate = Metric('goal01AbandonRate')
    # Goal 02
    goal02_starts = Metric('goal02Starts')
    goal02_completions = Metric('goal02Completions')
    goal02_value = Metric('goal02Value')
    goal02_conversion_rate = Metric('goal02ConversionRate')
    goal02_abandons = Metric('goal02Abandons')
    goal02_abandon_rate = Metric('goal02AbandonRate')
    # Goal 03
    goal03_starts = Metric('goal03Starts')
    goal03_completions = Metric('goal03Completions')
    goal03_value = Metric('goal03Value')
    goal03_conversion_rate = Metric('goal03ConversionRate')
    goal03_abandons = Metric('goal03Abandons')
    goal03_abandon_rate = Metric('goal03AbandonRate')
    # Goal 04
    goal04_starts = Metric('goal04Starts')
    goal04_completions = Metric('goal04Completions')
    goal04_value = Metric('goal04Value')
    goal04_conversion_rate = Metric('goal04ConversionRate')
    goal04_abandons = Metric('goal04Abandons')
    goal04_abandon_rate = Metric('goal04AbandonRate')
    # Goal 05
    goal05_starts = Metric('goal05Starts')
    goal05_completions = Metric('goal05Completions')
    goal05_value = Metric('goal05Value')
    goal05_conversion_rate = Metric('goal05ConversionRate')
    goal05_abandons = Metric('goal05Abandons')
    goal05_abandon_rate = Metric('goal05AbandonRate')
    # Goal 06
    goal06_starts = Metric('goal06Starts')
    goal06_completions = Metric('goal06Completions')
    goal06_value = Metric('goal06Value')
    goal06_conversion_rate = Metric('goal06ConversionRate')
    goal06_abandons = Metric('goal06Abandons')
    goal06_abandon_rate = Metric('goal06AbandonRate')
    # Goal 07
    goal07_starts = Metric('goal07Starts')
    goal07_completions = Metric('goal07Completions')
    goal07_value = Metric('goal07Value')
    goal07_conversion_rate = Metric('goal07ConversionRate')
    goal07_abandons = Metric('goal07Abandons')
    goal07_abandon_rate = Metric('goal07AbandonRate')
    # Goal 08
    goal08_starts = Metric('goal08Starts')
    goal08_completions = Metric('goal08Completions')
    goal08_value = Metric('goal08Value')
    goal08_conversion_rate = Metric('goal08ConversionRate')
    goal08_abandons = Metric('goal08Abandons')
    goal08_abandon_rate = Metric('goal08AbandonRate')
    # Goal 09
    goal09_starts = Metric('goal09Starts')
    goal09_completions = Metric('goal09Completions')
    goal09_value = Metric('goal09Value')
    goal09_conversion_rate = Metric('goal09ConversionRate')
    goal09_abandons = Metric('goal09Abandons')
    goal09_abandon_rate = Metric('goal09AbandonRate')
    # Goal 10
    goal10_starts = Metric('goal10Starts')
    goal10_completions = Metric('goal10Completions')
    goal10_value = Metric('goal10Value')
    goal10_conversion_rate = Metric('goal10ConversionRate')
    goal10_abandons = Metric('goal10Abandons')
    goal10_abandon_rate = Metric('goal10AbandonRate')
    # Goal 11
    goal11_starts = Metric('goal11Starts')
    goal11_completions = Metric('goal11Completions')
    goal11_value = Metric('goal11Value')
    goal11_conversion_rate = Metric('goal11ConversionRate')
    goal11_abandons = Metric('goal11Abandons')
    goal11_abandon_rate = Metric('goal11AbandonRate')
    # Goal 12
    goal12_starts = Metric('goal12Starts')
    goal12_completions = Metric('goal12Completions')
    goal12_value = Metric('goal12Value')
    goal12_conversion_rate = Metric('goal12ConversionRate')
    goal12_abandons = Metric('goal12Abandons')
    goal12_abandon_rate = Metric('goal12AbandonRate')
    # Goal 13
    goal13_starts = Metric('goal13Starts')
    goal13_completions = Metric('goal13Completions')
    goal13_value = Metric('goal13Value')
    goal13_conversion_rate = Metric('goal13ConversionRate')
    goal13_abandons = Metric('goal13Abandons')
    goal13_abandon_rate = Metric('goal13AbandonRate')
    # Goal 14
    goal14_starts = Metric('goal14Starts')
    goal14_completions = Metric('goal14Completions')
    goal14_value = Metric('goal14Value')
    goal14_conversion_rate = Metric('goal14ConversionRate')
    goal14_abandons = Metric('goal14Abandons')
    goal14_abandon_rate = Metric('goal14AbandonRate')
    # Goal 15
    goal15_starts = Metric('goal15Starts')
    goal15_completions = Metric('goal15Completions')
    goal15_value = Metric('goal15Value')
    goal15_conversion_rate = Metric('goal15ConversionRate')
    goal15_abandons = Metric('goal15Abandons')
    goal15_abandon_rate = Metric('goal15AbandonRate')
    # Goal 16
    goal16_starts = Metric('goal16Starts')
    goal16_completions = Metric('goal16Completions')
    goal16_value = Metric('goal16Value')
    goal16_conversion_rate = Metric('goal16ConversionRate')
    goal16_abandons = Metric('goal16Abandons')
    goal16_abandon_rate = Metric('goal16AbandonRate')
    # Goal 17
    goal17_starts = Metric('goal17Starts')
    goal17_completions = Metric('goal17Completions')
    goal17_value = Metric('goal17Value')
    goal17_conversion_rate = Metric('goal17ConversionRate')
    goal17_abandons = Metric('goal17Abandons')
    goal17_abandon_rate = Metric('goal17AbandonRate')
    # Goal 18
    goal18_starts = Metric('goal18Starts')
    goal18_completions = Metric('goal18Completions')
    goal18_value = Metric('goal18Value')
    goal18_conversion_rate = Metric('goal18ConversionRate')
    goal18_abandons = Metric('goal18Abandons')
    goal18_abandon_rate = Metric('goal18AbandonRate')
    # Goal 19
    goal19_starts = Metric('goal19Starts')
    goal19_completions = Metric('goal19Completions')
    goal19_value = Metric('goal19Value')
    goal19_conversion_rate = Metric('goal19ConversionRate')
    goal19_abandons = Metric('goal19Abandons')
    goal19_abandon_rate = Metric('goal19AbandonRate')
    # Goal 20
    goal20_starts = Metric('goal20Starts')
    goal20_completions = Metric('goal20Completions')
    goal20_value = Metric('goal20Value')
    goal20_conversion_rate = Metric('goal20ConversionRate')
    goal20_abandons = Metric('goal20Abandons')
    goal20_abandon_rate = Metric('goal20AbandonRate')

    # Page Tracking
    page_value = Metric('pageValue')
    entrances = Metric('entrances')
    entrance_rate = Metric('entranceRate')
    page_previews = Metric('pagePreviews')
    pageviews = Metric('pageviews')
    pageviews_per_session = Metric('pageviewsPerSession')
    unique_pageviews = Metric('uniquePageviews')
    time_on_page = Metric('timeOnPage')
    exits = Metric('exits')
    exit_rate = Metric('exitRate')


class API:
    """API class."""

    dimensions = Dimensions()
    metrics = Metrics()

    def __init__(self, secrets_json, view_id):
        """Init API class."""
        self._view_id = view_id

        # Set up a Flow object to be used if we need to authenticate.
        flow = client.flow_from_clientsecrets(
            secrets_json,
            scope=SCOPES,
            message=tools.message_if_missing(secrets_json))

        # Prepare credentials, and authorize HTTP object with them.
        # If the credentials don't exist or are invalid run through the
        # native client flow. The Storage object will ensure that if
        # successful the good credentials will get written back to a file.
        storage = file.Storage('analyticsreporting.dat')
        credentials = storage.get()
        if credentials is None or credentials.invalid:
            credentials = tools.run_flow(flow, storage)
        http = credentials.authorize(http=httplib2.Http())

        # Build the service object.
        self._analytics = build('analytics', 'v4', http=http,
                                discoveryServiceUrl=DISCOVERY_URI)

    def get_report(self, start_date='7daysAgo', end_date='today',
                   metrics=None, dimensions=None):
        """Return an API response object reporting metrics for set dates."""
        return self._analytics.reports().batchGet(
            body={
                'reportRequests': [
                    {
                        'viewId': self._view_id,
                        'dateRanges': [{'startDate': start_date,
                                        'endDate': end_date}],
                        'metrics': metrics,
                        'dimensions': dimensions
                    }]
            }
        ).execute()
