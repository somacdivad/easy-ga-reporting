"""Objects for dealing with Google Analytics dimensions sanely."""

from collections import namedtuple


class Dimension:
    """Class for dealing with Google Analaytics dimensions."""

    def __init__(self, name, alias="", histogram_buckets=None):
        """Init Dimension object."""
        self.name = name
        self.alias = alias
        self.histogram_buckets = [histogram_buckets] if histogram_buckets else []

    def __repr__(self):
        """Repr string for class."""
        return f"{self.__class__.__name__}('{self.name}', '{self.histogram_buckets}')"

    def __str__(self):
        """String representation of dimension name."""
        return f"{self.name}"

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"name": self.name, "histogramBuckets": self.histogram_buckets}


class Dimensions:
    """Google Analytics dimensions for use with the API class."""

    # Users
    @property
    def user_type(self):
        return Dimension(name="ga:userType", alias="User Type")

    @property
    def session_count(self):
        return Dimension(name="ga:sessionCount", alias="Count of Sessions")

    @property
    def days_since_last_session(self):
        return Dimension(
            name="ga:daysSinceLastSession", alias="Days Since Last Session"
        )

    @property
    def user_defined_value(self):
        return Dimension(name="ga:userDefinedValue", alias="User Defined Value")

    @property
    def user_bucket(self):
        return Dimension(name="ga:userBucket", alias="User Bucket")

    # Sessions
    @property
    def session_duration_bucket(self):
        return Dimension(name="ga:sessionDurationBucket", alias="Session Duration")

    # Traffic Sources
    @property
    def referral_path(self):
        return Dimension(name="ga:referralPath", alias="Referral Path")

    @property
    def full_referrer(self):
        return Dimension(name="ga:fullReferrer", alias="Full Referrer")

    @property
    def campaign(self):
        return Dimension(name="ga:campaign", alias="Campaign")

    @property
    def source(self):
        return Dimension(name="ga:source", alias="Source")

    @property
    def medium(self):
        return Dimension(name="ga:medium", alias="Medium")

    @property
    def source_medium(self):
        return Dimension(name="ga:sourceMedium", alias="Source / Medium")

    @property
    def keyword(self):
        return Dimension(name="ga:keyword", alias="Keyword")

    @property
    def ad_content(self):
        return Dimension(name="ga:adContent", alias="Ad Content")

    @property
    def social_network(self):
        return Dimension(name="ga:socialNetwork", alias="Social Network")

    @property
    def has_social_source_referral(self):
        return Dimension(
            name="ga:hasSocialSourceReferral", alias="Social Source Referral"
        )

    @property
    def campaign_code(self):
        return Dimension(name="ga:campaignCode", alias="Campaign Code")

    # AdWords
    @property
    def ad_group(self):
        return Dimension(name="ga:adGroup", alias="AdWords Ad Group")

    @property
    def ad_slot(self):
        return Dimension(name="ga:adSlot", alias="AdWord Ad Slot")

    @property
    def ad_distribution_network(self):
        return Dimension(
            name="ga:adDistributionNetwork", alias="Ad Distribution Network"
        )

    @property
    def ad_match_type(self):
        return Dimension(name="ga:adMatchType", alias="Query Match Type")

    @property
    def ad_keyword_match_type(self):
        return Dimension(name="ga:adKeywordMatchType", alias="Keyword Match Type")

    @property
    def ad_matched_query(self):
        return Dimension(name="ga:adMatchedQuery", alias="Search Query")

    @property
    def ad_placement_domain(self):
        return Dimension(name="ga:adPlacementDomain", alias="Placement Domain")

    @property
    def ad_placement_url(self):
        return Dimension(name="ga:adPlacementUrl", alias="Placement URL")

    @property
    def ad_format(self):
        return Dimension(name="ga:adFormat", alias="Ad Format")

    @property
    def ad_targeting_type(self):
        return Dimension(name="ga:adTargetingType", alias="Targeting Type")

    @property
    def ad_targeting_option(self):
        return Dimension(name="ga:adTargetingOption", alias="Placement Type")

    @property
    def ad_display_url(self):
        return Dimension(name="ga:adDisplayUrl", alias="Display URL")

    @property
    def ad_destination_url(self):
        return Dimension(name="ga:adDestinationUrl", alias="Destination URL")

    @property
    def adwords_customer_id(self):
        return Dimension(name="ga:adwordsCustomerID", alias="AdWords Customer ID")

    @property
    def adwords_campaign_id(self):
        return Dimension(name="ga:adwordsCampaignID", alias="AdWords Campaign ID")

    @property
    def adwords_ad_group_id(self):
        return Dimension(name="ga:adwordsAdGroupID", alias="AdWords Ad Group ID")

    @property
    def adwords_creative_id(self):
        return Dimension(name="ga:adwordsCreativeID", alias="AdWords Creative ID")

    @property
    def adwords_criterial_id(self):
        return Dimension(name="ga:adwordsCriterialsID", alias="AdWord Criteria ID")

    @property
    def ad_query_word_count(self):
        return Dimension(name="ga:adQueryWordCount", alias="Query Word Count")

    @property
    def is_true_video_view_ad(self):
        return Dimension(name="ga:isTrueViewVideoAd", alias="TrueView Video Ad")

    # Goal Conversions
    @property
    def goal_completion_location(self):
        return Dimension(
            name="ga:goalCompletionLocation", alias="Goal Completion Location"
        )

    @property
    def goal_previous_step1(self):
        return Dimension(name="ga:goalPreviousStep1", alias="Goal Previous Step - 1")

    @property
    def goal_previous_step2(self):
        return Dimension(name="ga:goalPreviousStep2", alias="Goal Previous Step - 2")

    @property
    def goal_previous_step3(self):
        return Dimension(name="ga:goalPreviousStep3", alias="Goal Previous Step - 3")

    # Platform or Device
    @property
    def browser(self):
        return Dimension(name="ga:browser", alias="Browser")

    @property
    def browser_version(self):
        return Dimension(name="ga:browserVersion", alias="Browser Version")

    @property
    def os(self):
        return Dimension(name="ga:operatingSystem", alias="Operating System")

    @property
    def os_version(self):
        return Dimension(name="ga:operatingSystemVersion", alias="Operating System")

    @property
    def mobile_branding(self):
        return Dimension(name="ga:mobileDeviceBranding", alias="Mobile Device Branding")

    @property
    def mobile_model(self):
        return Dimension(name="ga:mobileDeviceModel", alias="Mobile Device Model")

    @property
    def mobile_input_selector(self):
        return Dimension(name="ga:mobileInputSelector", alias="Mobile Input Selector")

    @property
    def mobile_device_info(self):
        return Dimension(name="ga:mobileDeviceInfo", alias="Mobile Device Info")

    @property
    def mobile_marketing_name(self):
        return Dimension(
            name="ga:mobileDeviceMarketingName", alias="Mobile Device Marketing Name"
        )

    @property
    def device_category(self):
        return Dimension(name="ga:deviceCategory", alias="Device Category")

    @property
    def browser_size(self):
        return Dimension(name="ga:browserSize", alias="Browser Size")

    @property
    def data_source(self):
        return Dimension(name="ga:dataSource", alias="Data Source")

    # Geo Network
    @property
    def continent(self):
        return Dimension(name="ga:continent", alias="Continent")

    @property
    def subcontinent(self):
        return Dimension(name="ga:subContinent", alias="Sub Continent")

    @property
    def country(self):
        return Dimension(name="ga:country", alias="Country")

    @property
    def region(self):
        return Dimension(name="ga:region", alias="Region")

    @property
    def metro(self):
        return Dimension(name="ga:metro", alias="Metro")

    @property
    def city(self):
        return Dimension(name="ga:city", alias="City")

    @property
    def latitude(self):
        return Dimension(name="ga:latitude", alias="Latitude")

    @property
    def longitude(self):
        return Dimension(name="ga:longitude", alias="Longitude")

    @property
    def network_domain(self):
        return Dimension(name="ga:networkDomain", alias="Network Domain")

    @property
    def network_location(self):
        return Dimension(name="ga:networkLocation", alias="Service Provider")

    @property
    def city_id(self):
        return Dimension(name="ga:cityId", alias="City ID")

    @property
    def continent_id(self):
        return Dimension(name="ga:continentId", alias="Continent ID")

    @property
    def country_iso_code(self):
        return Dimension(name="ga:countryIsoCode", alias="Country ISO Code")

    @property
    def metro_id(self):
        return Dimension(name="ga:metroId", alias="Metro ID")

    @property
    def region_id(self):
        return Dimension(name="ga:regionId", alias="Region ID")

    @property
    def region_iso_code(self):
        return Dimension(name="ga:regionIsoCode", alias="Region ISO Code")

    @property
    def subcontinent_code(self):
        return Dimension(name="ga:subContenentCode", alias="Sub Continent Code")

    # System
    @property
    def flash_version(self):
        return Dimension(name="ga:flashVersion", alias="Flash Version")

    @property
    def java_enabled(self):
        return Dimension(name="ga:javaEnabled", alias="Java Support")

    @property
    def language(self):
        return Dimension(name="ga:language", alias="Language")

    @property
    def screen_colors(self):
        return Dimension(name="ga:screenColors", alias="Screen Colors")

    @property
    def source_property_display_name(self):
        return Dimension(
            name="ga:sourcePropertyDisplayName", alias="Source Property Display Name"
        )

    @property
    def source_property_tracking_id(self):
        return Dimension(
            name="ga:sourcePropertyTrackingId", alias="Source Property Tracking ID"
        )

    @property
    def screen_resolution(self):
        return Dimension(name="ga:screenResolution", alias="Screen Resolution")

    # Page Tracking
    @property
    def hostname(self):
        return Dimension(name="ga:hostname", alias="Hostname")

    @property
    def page_path(self):
        return Dimension(name="ga:pagePath", alias="Page")

    @property
    def page_path_level1(self):
        return Dimension(name="ga:pagePathLevel1", alias="Page path level 1")

    @property
    def page_path_level2(self):
        return Dimension(name="ga:pagePathLevel2", alias="Page path level 2")

    @property
    def page_path_level3(self):
        return Dimension(name="ga:pagePathLevel3", alias="Page path level 3")

    @property
    def page_path_level4(self):
        return Dimension(name="ga:pagePathLevel4", alias="Page path level 4")

    @property
    def page_title(self):
        return Dimension(name="ga:pageTitle", alias="Page Title")

    @property
    def landing_page_path(self):
        return Dimension(name="ga:landingPagePath", alias="Landing Page")

    @property
    def second_page_path(self):
        return Dimension(name="ga:secondPagePath", alias="Second Page")

    @property
    def exit_page_path(self):
        return Dimension(name="ga:exitPagePath", alias="Exit Page")

    @property
    def previous_page_path(self):
        return Dimension(name="ga:previousPagePath", alias="Previous Page Path")

    @property
    def page_depth(self):
        return Dimension(name="ga:pageDepth", alias="Page Depth")

    # Time
    @property
    def date(self):
        return Dimension(name="ga:date", alias="Date")

    @property
    def year(self):
        return Dimension(name="ga:year", alias="Year")

    @property
    def month(self):
        return Dimension(name="ga:month", alias="Month of the Year")

    @property
    def week(self):
        return Dimension(name="ga:week", alias="Week of the Year")

    @property
    def day(self):
        return Dimension(name="ga:day", alias="Day of the Month")

    @property
    def hour(self):
        return Dimension(name="ga:hour", alias="Hour")

    @property
    def minute(self):
        return Dimension(name="ga:minute", alias="Minute")

    @property
    def nth_month(self):
        return Dimension(name="ga:nthMonth", alias="Month Index")

    @property
    def nth_week(self):
        return Dimension(name="ga:nthWeek", alias="Week Index")

    @property
    def nth_day(self):
        return Dimension(name="ga:nthDay", alias="Day Index")

    @property
    def nth_minute(self):
        return Dimension(name="ga:nthMinute", alias="Minute Index")

    @property
    def day_of_week(self):
        return Dimension(name="ga:dayOfWeek", alias="Day of Week")

    @property
    def day_of_week_name(self):
        return Dimension(name="ga:dayOfWeekName", alias="Day of Week Name")

    @property
    def date_hour(self):
        return Dimension(name="ga:dateHour", alias="Hour of Day")

    @property
    def date_hour_minute(self):
        return Dimension(name="ga:dateHourMinute", alias="Dat Hour and Minute")

    @property
    def year_month(self):
        return Dimension(name="ga:yearMonth", alias="Month of Year")

    @property
    def year_week(self):
        return Dimension(name="ga:yearWeek", alias="Week of Year")

    @property
    def iso_week(self):
        return Dimension(name="ga:isoWeek", alias="ISO Week of the Year")

    @property
    def iso_year(self):
        return Dimension(name="ga:isoYear", alias="ISO Year")

    @property
    def iso_year_iso_week(self):
        return Dimension(name="ga:isoYearIsoWeek", alias="ISO Week of ISO Year")

    @property
    def nth_hour(self):
        return Dimension(name="ga:nthHour", alias="Hour Index")

    # Audience
    @property
    def user_age_bracket(self):
        return Dimension(name="ga:userAgeBracket", alias="Age")

    @property
    def user_gender(self):
        return Dimension(name="ga:userGender", alias="Gender")

    @property
    def interest_other_category(self):
        return Dimension(name="ga:interestOtherCategory", alias="Other Category")

    @property
    def interest_affinity_category(self):
        return Dimension(
            name="ga:interestAffinityCategory", alias="Affinity Category (reach)"
        )

    @property
    def interest_in_market_category(self):
        return Dimension(name="ga:interestInMarketCategory", alias="In-Market Segment")


dimensions = Dimensions()
