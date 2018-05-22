"""Google Analytics Reporting API v4 Dimensions."""

from easy_gar.api import Dimension


class ReportingDimension(Dimension):
    """Analytics Dimension class."""

    def __init__(self, name, alias="", histogram_buckets=None):
        """Init Dimension object."""
        super().__init__(name, alias)
        self.histogram_buckets = (
            [histogram_buckets] if histogram_buckets else []
        )

    def __repr__(self):
        """Repr string for class."""
        return (
            f"{self.__class__.__name__}('{self.name}', "
            f"'{self.histogram_buckets}')"
        )

    def __call__(self):
        """Return dictionary to be used in API requests."""
        return {"name": self.name, "histogramBuckets": self.histogram_buckets}


class Dimensions:
    """Analytics dimensions for use with the API objects."""

    # Users
    @property
    def user_type(self):
        return ReportingDimension(name="ga:userType", alias="User Type")

    @property
    def session_count(self):
        return ReportingDimension(
            name="ga:sessionCount", alias="Count of Sessions"
        )

    @property
    def days_since_last_session(self):
        return ReportingDimension(
            name="ga:daysSinceLastSession", alias="Days Since Last Session"
        )

    @property
    def user_defined_value(self):
        return ReportingDimension(
            name="ga:userDefinedValue", alias="User Defined Value"
        )

    @property
    def user_bucket(self):
        return ReportingDimension(name="ga:userBucket", alias="User Bucket")

    # Sessions
    @property
    def session_duration_bucket(self):
        return ReportingDimension(
            name="ga:sessionDurationBucket", alias="Session Duration"
        )

    # Traffic Sources
    @property
    def referral_path(self):
        return ReportingDimension(
            name="ga:referralPath", alias="Referral Path"
        )

    @property
    def full_referrer(self):
        return ReportingDimension(
            name="ga:fullReferrer", alias="Full Referrer"
        )

    @property
    def campaign(self):
        return ReportingDimension(name="ga:campaign", alias="Campaign")

    @property
    def source(self):
        return ReportingDimension(name="ga:source", alias="Source")

    @property
    def medium(self):
        return ReportingDimension(name="ga:medium", alias="Medium")

    @property
    def source_medium(self):
        return ReportingDimension(
            name="ga:sourceMedium", alias="Source / Medium"
        )

    @property
    def keyword(self):
        return ReportingDimension(name="ga:keyword", alias="Keyword")

    @property
    def ad_content(self):
        return ReportingDimension(name="ga:adContent", alias="Ad Content")

    @property
    def social_network(self):
        return ReportingDimension(
            name="ga:socialNetwork", alias="Social Network"
        )

    @property
    def has_social_source_referral(self):
        return ReportingDimension(
            name="ga:hasSocialSourceReferral", alias="Social Source Referral"
        )

    @property
    def campaign_code(self):
        return ReportingDimension(
            name="ga:campaignCode", alias="Campaign Code"
        )

    # AdWords
    @property
    def ad_group(self):
        return ReportingDimension(name="ga:adGroup", alias="AdWords Ad Group")

    @property
    def ad_slot(self):
        return ReportingDimension(name="ga:adSlot", alias="AdWord Ad Slot")

    @property
    def ad_distribution_network(self):
        return ReportingDimension(
            name="ga:adDistributionNetwork", alias="Ad Distribution Network"
        )

    @property
    def ad_match_type(self):
        return ReportingDimension(
            name="ga:adMatchType", alias="Query Match Type"
        )

    @property
    def ad_keyword_match_type(self):
        return ReportingDimension(
            name="ga:adKeywordMatchType", alias="Keyword Match Type"
        )

    @property
    def ad_matched_query(self):
        return ReportingDimension(
            name="ga:adMatchedQuery", alias="Search Query"
        )

    @property
    def ad_placement_domain(self):
        return ReportingDimension(
            name="ga:adPlacementDomain", alias="Placement Domain"
        )

    @property
    def ad_placement_url(self):
        return ReportingDimension(
            name="ga:adPlacementUrl", alias="Placement URL"
        )

    @property
    def ad_format(self):
        return ReportingDimension(name="ga:adFormat", alias="Ad Format")

    @property
    def ad_targeting_type(self):
        return ReportingDimension(
            name="ga:adTargetingType", alias="Targeting Type"
        )

    @property
    def ad_targeting_option(self):
        return ReportingDimension(
            name="ga:adTargetingOption", alias="Placement Type"
        )

    @property
    def ad_display_url(self):
        return ReportingDimension(name="ga:adDisplayUrl", alias="Display URL")

    @property
    def ad_destination_url(self):
        return ReportingDimension(
            name="ga:adDestinationUrl", alias="Destination URL"
        )

    @property
    def adwords_customer_id(self):
        return ReportingDimension(
            name="ga:adwordsCustomerID", alias="AdWords Customer ID"
        )

    @property
    def adwords_campaign_id(self):
        return ReportingDimension(
            name="ga:adwordsCampaignID", alias="AdWords Campaign ID"
        )

    @property
    def adwords_ad_group_id(self):
        return ReportingDimension(
            name="ga:adwordsAdGroupID", alias="AdWords Ad Group ID"
        )

    @property
    def adwords_creative_id(self):
        return ReportingDimension(
            name="ga:adwordsCreativeID", alias="AdWords Creative ID"
        )

    @property
    def adwords_criterial_id(self):
        return ReportingDimension(
            name="ga:adwordsCriterialsID", alias="AdWord Criteria ID"
        )

    @property
    def ad_query_word_count(self):
        return ReportingDimension(
            name="ga:adQueryWordCount", alias="Query Word Count"
        )

    @property
    def is_true_video_view_ad(self):
        return ReportingDimension(
            name="ga:isTrueViewVideoAd", alias="TrueView Video Ad"
        )

    # Goal Conversions
    @property
    def goal_completion_location(self):
        return ReportingDimension(
            name="ga:goalCompletionLocation", alias="Goal Completion Location"
        )

    @property
    def goal_previous_step1(self):
        return ReportingDimension(
            name="ga:goalPreviousStep1", alias="Goal Previous Step - 1"
        )

    @property
    def goal_previous_step2(self):
        return ReportingDimension(
            name="ga:goalPreviousStep2", alias="Goal Previous Step - 2"
        )

    @property
    def goal_previous_step3(self):
        return ReportingDimension(
            name="ga:goalPreviousStep3", alias="Goal Previous Step - 3"
        )

    # Platform or Device
    @property
    def browser(self):
        return ReportingDimension(name="ga:browser", alias="Browser")

    @property
    def browser_version(self):
        return ReportingDimension(
            name="ga:browserVersion", alias="Browser Version"
        )

    @property
    def os(self):
        return ReportingDimension(
            name="ga:operatingSystem", alias="Operating System"
        )

    @property
    def os_version(self):
        return ReportingDimension(
            name="ga:operatingSystemVersion", alias="Operating System"
        )

    @property
    def mobile_branding(self):
        return ReportingDimension(
            name="ga:mobileDeviceBranding", alias="Mobile Device Branding"
        )

    @property
    def mobile_model(self):
        return ReportingDimension(
            name="ga:mobileDeviceModel", alias="Mobile Device Model"
        )

    @property
    def mobile_input_selector(self):
        return ReportingDimension(
            name="ga:mobileInputSelector", alias="Mobile Input Selector"
        )

    @property
    def mobile_device_info(self):
        return ReportingDimension(
            name="ga:mobileDeviceInfo", alias="Mobile Device Info"
        )

    @property
    def mobile_marketing_name(self):
        return ReportingDimension(
            name="ga:mobileDeviceMarketingName",
            alias="Mobile Device Marketing Name",
        )

    @property
    def device_category(self):
        return ReportingDimension(
            name="ga:deviceCategory", alias="Device Category"
        )

    @property
    def browser_size(self):
        return ReportingDimension(name="ga:browserSize", alias="Browser Size")

    @property
    def data_source(self):
        return ReportingDimension(name="ga:dataSource", alias="Data Source")

    # Geo Network
    @property
    def continent(self):
        return ReportingDimension(name="ga:continent", alias="Continent")

    @property
    def subcontinent(self):
        return ReportingDimension(
            name="ga:subContinent", alias="Sub Continent"
        )

    @property
    def country(self):
        return ReportingDimension(name="ga:country", alias="Country")

    @property
    def region(self):
        return ReportingDimension(name="ga:region", alias="Region")

    @property
    def metro(self):
        return ReportingDimension(name="ga:metro", alias="Metro")

    @property
    def city(self):
        return ReportingDimension(name="ga:city", alias="City")

    @property
    def latitude(self):
        return ReportingDimension(name="ga:latitude", alias="Latitude")

    @property
    def longitude(self):
        return ReportingDimension(name="ga:longitude", alias="Longitude")

    @property
    def network_domain(self):
        return ReportingDimension(
            name="ga:networkDomain", alias="Network Domain"
        )

    @property
    def network_location(self):
        return ReportingDimension(
            name="ga:networkLocation", alias="Service Provider"
        )

    @property
    def city_id(self):
        return ReportingDimension(name="ga:cityId", alias="City ID")

    @property
    def continent_id(self):
        return ReportingDimension(name="ga:continentId", alias="Continent ID")

    @property
    def country_iso_code(self):
        return ReportingDimension(
            name="ga:countryIsoCode", alias="Country ISO Code"
        )

    @property
    def metro_id(self):
        return ReportingDimension(name="ga:metroId", alias="Metro ID")

    @property
    def region_id(self):
        return ReportingDimension(name="ga:regionId", alias="Region ID")

    @property
    def region_iso_code(self):
        return ReportingDimension(
            name="ga:regionIsoCode", alias="Region ISO Code"
        )

    @property
    def subcontinent_code(self):
        return ReportingDimension(
            name="ga:subContenentCode", alias="Sub Continent Code"
        )

    # System
    @property
    def flash_version(self):
        return ReportingDimension(
            name="ga:flashVersion", alias="Flash Version"
        )

    @property
    def java_enabled(self):
        return ReportingDimension(name="ga:javaEnabled", alias="Java Support")

    @property
    def language(self):
        return ReportingDimension(name="ga:language", alias="Language")

    @property
    def screen_colors(self):
        return ReportingDimension(
            name="ga:screenColors", alias="Screen Colors"
        )

    @property
    def source_property_display_name(self):
        return ReportingDimension(
            name="ga:sourcePropertyDisplayName",
            alias="Source Property Display Name",
        )

    @property
    def source_property_tracking_id(self):
        return ReportingDimension(
            name="ga:sourcePropertyTrackingId",
            alias="Source Property Tracking ID",
        )

    @property
    def screen_resolution(self):
        return ReportingDimension(
            name="ga:screenResolution", alias="Screen Resolution"
        )

    # Page Tracking
    @property
    def hostname(self):
        return ReportingDimension(name="ga:hostname", alias="Hostname")

    @property
    def page_path(self):
        return ReportingDimension(name="ga:pagePath", alias="Page")

    @property
    def page_path_level1(self):
        return ReportingDimension(
            name="ga:pagePathLevel1", alias="Page path level 1"
        )

    @property
    def page_path_level2(self):
        return ReportingDimension(
            name="ga:pagePathLevel2", alias="Page path level 2"
        )

    @property
    def page_path_level3(self):
        return ReportingDimension(
            name="ga:pagePathLevel3", alias="Page path level 3"
        )

    @property
    def page_path_level4(self):
        return ReportingDimension(
            name="ga:pagePathLevel4", alias="Page path level 4"
        )

    @property
    def page_title(self):
        return ReportingDimension(name="ga:pageTitle", alias="Page Title")

    @property
    def landing_page_path(self):
        return ReportingDimension(
            name="ga:landingPagePath", alias="Landing Page"
        )

    @property
    def second_page_path(self):
        return ReportingDimension(
            name="ga:secondPagePath", alias="Second Page"
        )

    @property
    def exit_page_path(self):
        return ReportingDimension(name="ga:exitPagePath", alias="Exit Page")

    @property
    def previous_page_path(self):
        return ReportingDimension(
            name="ga:previousPagePath", alias="Previous Page Path"
        )

    @property
    def page_depth(self):
        return ReportingDimension(name="ga:pageDepth", alias="Page Depth")

    # Time
    @property
    def date(self):
        return ReportingDimension(name="ga:date", alias="Date")

    @property
    def year(self):
        return ReportingDimension(name="ga:year", alias="Year")

    @property
    def month(self):
        return ReportingDimension(name="ga:month", alias="Month of the Year")

    @property
    def week(self):
        return ReportingDimension(name="ga:week", alias="Week of the Year")

    @property
    def day(self):
        return ReportingDimension(name="ga:day", alias="Day of the Month")

    @property
    def hour(self):
        return ReportingDimension(name="ga:hour", alias="Hour")

    @property
    def minute(self):
        return ReportingDimension(name="ga:minute", alias="Minute")

    @property
    def nth_month(self):
        return ReportingDimension(name="ga:nthMonth", alias="Month Index")

    @property
    def nth_week(self):
        return ReportingDimension(name="ga:nthWeek", alias="Week Index")

    @property
    def nth_day(self):
        return ReportingDimension(name="ga:nthDay", alias="Day Index")

    @property
    def nth_minute(self):
        return ReportingDimension(name="ga:nthMinute", alias="Minute Index")

    @property
    def day_of_week(self):
        return ReportingDimension(name="ga:dayOfWeek", alias="Day of Week")

    @property
    def day_of_week_name(self):
        return ReportingDimension(
            name="ga:dayOfWeekName", alias="Day of Week Name"
        )

    @property
    def date_hour(self):
        return ReportingDimension(name="ga:dateHour", alias="Hour of Day")

    @property
    def date_hour_minute(self):
        return ReportingDimension(
            name="ga:dateHourMinute", alias="Dat Hour and Minute"
        )

    @property
    def year_month(self):
        return ReportingDimension(name="ga:yearMonth", alias="Month of Year")

    @property
    def year_week(self):
        return ReportingDimension(name="ga:yearWeek", alias="Week of Year")

    @property
    def iso_week(self):
        return ReportingDimension(
            name="ga:isoWeek", alias="ISO Week of the Year"
        )

    @property
    def iso_year(self):
        return ReportingDimension(name="ga:isoYear", alias="ISO Year")

    @property
    def iso_year_iso_week(self):
        return ReportingDimension(
            name="ga:isoYearIsoWeek", alias="ISO Week of ISO Year"
        )

    @property
    def nth_hour(self):
        return ReportingDimension(name="ga:nthHour", alias="Hour Index")

    # Audience
    @property
    def user_age_bracket(self):
        return ReportingDimension(name="ga:userAgeBracket", alias="Age")

    @property
    def user_gender(self):
        return ReportingDimension(name="ga:userGender", alias="Gender")

    @property
    def interest_other_category(self):
        return ReportingDimension(
            name="ga:interestOtherCategory", alias="Other Category"
        )

    @property
    def interest_affinity_category(self):
        return ReportingDimension(
            name="ga:interestAffinityCategory",
            alias="Affinity Category (reach)",
        )

    @property
    def interest_in_market_category(self):
        return ReportingDimension(
            name="ga:interestInMarketCategory", alias="In-Market Segment"
        )
