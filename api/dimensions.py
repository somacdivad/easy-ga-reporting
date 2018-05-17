"""Objects for dealing with Google Analytics dimensions sanely."""

from collections import namedtuple


class _Dimension(namedtuple("Dimension", ["name"])):
    """Class for dealing with Google Analaytics dimensions."""

    __slots__ = ()

    def __repr__(self):
        """Repr string for class."""
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        """String representation of dimension name."""
        return f"{self.name}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"name": str(self)}


class _Dimensions:
    """Google Analytics dimensions for use with the API class."""

    # Users
    user_type = _Dimension("ga:userType")
    session_count = _Dimension("ga:sessionCount")
    days_since_last_session = _Dimension("ga:daysSinceLastSession")
    user_defined_value = _Dimension("ga:userDefinedValue")
    user_bucket = _Dimension("ga:userBucket")

    # Sessions
    session_duration_bucket = _Dimension("ga:sessionDurationBucket")

    # Traffic Sources
    referral_path = _Dimension("ga:referralPath")
    full_referrer = _Dimension("ga:fullReferrer")
    campaign = _Dimension("ga:campaign")
    source = _Dimension("ga:source")
    medium = _Dimension("ga:medium")
    source_medium = _Dimension("ga:sourceMedium")
    keyword = _Dimension("ga:keyword")
    ad_content = _Dimension("ga:adContent")
    social_network = _Dimension("ga:socialNetwork")
    has_social_source_referral = _Dimension("ga:hasSocialSourceReferral")
    campaign_code = _Dimension("ga:campaignCode")

    # AdWords
    ad_group = _Dimension("ga:adGroup")
    ad_slot = _Dimension("ga:adSlot")
    ad_distribution_network = _Dimension("ga:adDistributionNetwork")
    ad_match_type = _Dimension("ga:adMatchType")
    ad_keyword_match_type = _Dimension("ga:adKeywordMatchType")
    ad_matched_query = _Dimension("ga:adMatchedQuery")
    ad_placement_domain = _Dimension("ga:adPlacementDomain")
    ad_placement_url = _Dimension("ga:adPlacementUrl")
    ad_format = _Dimension("ga:adFormat")
    ad_targeting_type = _Dimension("ga:adTargetingType")
    ad_targeting_option = _Dimension("ga:adTargetingOption")
    ad_display_url = _Dimension("ga:adDisplayUrl")
    ad_destination_url = _Dimension("ga:adDestinationUrl")
    adwords_customer_id = _Dimension("ga:adwordsCustomerID")
    adwords_campaign_id = _Dimension("ga:adwordsCampaignID")
    adwords_ad_group_id = _Dimension("ga:adwordsAdGroupID")
    adwords_creative_id = _Dimension("ga:adwordsCreativeID")
    adwords_criterial_id = _Dimension("ga:adwordsCriterialsID")
    ad_query_word_count = _Dimension("ga:adQueryWordCount")
    is_true_video_view_ad = _Dimension("ga:isTrueViewVideoAd")

    # Goal Conversions
    goal_completion_location = _Dimension("ga:goalCompletionLocation")
    goal_previous_step1 = _Dimension("ga:goalPreviousStep1")
    goal_previous_step2 = _Dimension("ga:goalPreviousStep2")
    goal_previous_step3 = _Dimension("ga:goalPreviousStep3")

    # Platform or Device
    browser = _Dimension("ga:browser")
    browser_version = _Dimension("ga:browserVersion")
    os = _Dimension("ga:operatingSystem")
    os_version = _Dimension("ga:operatingSystemVersion")
    mobile_branding = _Dimension("ga:mobileDeviceBranding")
    mobile_model = _Dimension("ga:mobileDeviceModel")
    mobile_input_selector = _Dimension("ga:mobileInputSelector")
    mobile_info = _Dimension("ga:mobileDeviceInfo")
    mobile_marketing_name = _Dimension("ga:mobileDeviceMarketingName")
    device_category = _Dimension("ga:deviceCategory")
    browser_size = _Dimension("ga:browserSize")
    data_source = _Dimension("ga:dataSource")

    # Geo Network
    continent = _Dimension("ga:continent")
    subcontinent = _Dimension("ga:subContinent")
    country = _Dimension("ga:country")
    region = _Dimension("ga:region")
    metro = _Dimension("ga:metro")
    city = _Dimension("ga:city")
    latitude = _Dimension("ga:latitude")
    longitude = _Dimension("ga:longitude")
    network_domain = _Dimension("ga:networkDomain")
    network_location = _Dimension("ga:networkLocation")
    city_id = _Dimension("ga:cityId")
    country_iso_code = _Dimension("ga:countryIsoCode")
    metro_id = _Dimension("ga:metroId")
    region_id = _Dimension("ga:regionId")
    region_iso_code = _Dimension("ga:regionIsoCode")
    subcontinent_code = _Dimension("ga:subContenentCode")

    # System
    flash_version = _Dimension("ga:flashVersion")
    java_enabled = _Dimension("ga:javaEnabled")
    language = _Dimension("ga:language")
    screen_colors = _Dimension("ga:screenColors")
    source_property_display_name = _Dimension("ga:sourcePropertyDisplayName")
    source_property_tracking_id = _Dimension("ga:sourcePropertyTrackingId")
    screen_resolution = _Dimension("ga:screenResolution")

    # Page Tracking
    hostname = _Dimension("ga:hostname")
    page_path = _Dimension("ga:pagePath")
    page_path_level1 = _Dimension("ga:pagePathLevel1")
    page_path_level2 = _Dimension("ga:pagePathLevel2")
    page_path_level3 = _Dimension("ga:pagePathLevel3")
    page_path_level4 = _Dimension("ga:pagePathLevel4")
    page_title = _Dimension("ga:pageTitle")
    landing_path_path = _Dimension("ga:landingPagePath")
    second_page_path = _Dimension("ga:secondPagePath")
    exit_page_path = _Dimension("ga:exitPagePath")
    previous_page_path = _Dimension("ga:previousPagePath")
    page_depth = _Dimension("ga:pageDepth")

    # Time
    date = _Dimension("ga:date")
    year = _Dimension("ga:year")
    month = _Dimension("ga:month")
    week = _Dimension("ga:week")
    day = _Dimension("ga:day")
    hour = _Dimension("ga:hour")
    minute = _Dimension("ga:minute")
    nth_month = _Dimension("ga:nthMonth")
    nth_week = _Dimension("ga:nthWeek")
    nth_day = _Dimension("ga:nthDay")
    nth_minute = _Dimension("ga:nthMinute")
    day_of_week = _Dimension("ga:dayOfWeek")
    day_of_week_name = _Dimension("ga:dayOfWeekName")
    date_hour = _Dimension("ga:dateHour")
    date_hour_minute = _Dimension("ga:dateHourMinute")
    year_month = _Dimension("ga:yearMonth")
    ga_year_week = _Dimension("ga:yearWeek")
    iso_week = _Dimension("ga:isoWeek")
    iso_year = _Dimension("ga:isoYear")
    iso_year_iso_week = _Dimension("ga:isoYearIsoWeek")
    nth_hour = _Dimension("ga:nthHour")

    # Audience
    user_age_bracket = _Dimension("ga:userAgeBracket")
    user_gender = _Dimension("ga:userGender")
    interest_other_category = _Dimension("ga:interestOtherCategory")
    interest_affinity_category = _Dimension("ga:interestAffinityCategory")
    interest_in_market_category = _Dimension("ga:interestInMarketCategory")


dimensions = _Dimensions()
