"""Google Analytics Multi-channel Funnels API v3 Dimensions."""

from easy_gar.api import Dimension


class MCFDimension(Dimension):
    """Multi-Channel Funnel Dimensions class."""
    pass


class Dimensions:
    """Multi-Channel Funnel Dimensions for use with API object."""

    @property
    def basic_channel_grouping_path(self):
        return MCFDimension(
            name="mcf:basicChannelGroupingPath",
            alias="Basic Channel Grouping Path",
        )

    @property
    def source_path(self):
        return MCFDimension(name="mcf:sourcePath", alias="Source Path")

    @property
    def medium_path(self):
        return MCFDimension(name="mcf:mediumPath", alias="Medium Path")

    @property
    def source_medium_path(self):
        return MCFDimension(
            name="mcf:sourceMediumPath", alias="Source/Medium Path"
        )

    @property
    def campaign_path(self):
        return MCFDimension(name="mcf:campaignPath", alias="Campaign Path")

    @property
    def keyword_path(self):
        return MCFDimension(name="mcf:keywordPath", alias="Keyword Path")

    @property
    def adwords_ad_content_path(self):
        return MCFDimension(
            name="mcf:adwordsAdContentPath", alias="AdWords Ad Content Path"
        )

    @property
    def adwords_ad_group_id_path(self):
        return MCFDimension(
            name="mcf:adwordsAdGroupIDPath", alias="AdWords Ad Group ID Path"
        )

    @property
    def adwords_ad_group_path(self):
        return MCFDimension(
            name="mcf:adwordsAdGroupPath", alias="AdWords Ad Group Path"
        )

    @property
    def adwords_campaign_id_path(self):
        return MCFDimension(
            name="mcf:adwordsCampaignIDPath", alias="AdWords Campaign ID Path"
        )

    @property
    def adwords_campaign_path(self):
        return MCFDimension(
            name="mcf:adwordsCampaignPath", alias="AdWords Campaign Path"
        )

    @property
    def adwords_creative_id_path(self):
        return MCFDimension(
            name="mcf:adwordsCreativeIDPath", alias="AdWords Creative ID Path"
        )

    @property
    def adwords_criterial_path(self):
        return MCFDimension(
            name="mcf:adwordsCriteriaIDPath", alias="Adwords Criteria ID Path"
        )

    @property
    def adwords_customer_id_path(self):
        return MCFDimension(
            name="mcf:adwordsCustomerIDPath", alias="AdWords Customer ID Path"
        )

    @property
    def adwords_destination_url_path(self):
        return MCFDimension(
            name="mcf:adwordsDestinationUrlPath",
            alias="AdWords Destination URL Path",
        )

    @property
    def adwords_display_url_path(self):
        return MCFDimension(
            name="mcf:adwordsDisplayUrlPath", alias="AdWords Display URL Path"
        )

    @property
    def adwords_keyword_path(self):
        return MCFDimension(
            name="mcf:adwordsKeywordPath", alias="AdWords Keyword Path"
        )

    @property
    def adwords_matched_search_query_path(self):
        return MCFDimension(
            name="mcf:adwordsMatchedSearchQueryPath",
            alias="AdWords Matched Search Query Path",
        )

    @property
    def adwords_placement_domain_path(self):
        return MCFDimension(
            name="mcf:adwordsPlacementDomainPath",
            alias="AdWords Placement Domain Path",
        )

    @property
    def adwords_placement_url_path(self):
        return MCFDimension(
            name="mcf:adwordsPlacementUrlPath",
            alias="AdWords Placement URL Path",
        )

    @property
    def conversion_date(self):
        return MCFDimension(name="mcf:conversionDate", alias="Conversion Date")

    @property
    def conversion_goal_number(self):
        return MCFDimension(
            name="mcf:conversionGoalNumber", alias="Conversion Goal Number"
        )

    @property
    def conversion_type(self):
        return MCFDimension(name="mcf:conversionType", alias="Conversion Type")

    @property
    def dcm_ad(self):
        return MCFDimension(name="mcf:dcmAd", alias="DCM Ad Name")

    @property
    def dcm_ad_path(self):
        return MCFDimension(name="mcf:dcmAdType", alias="DCM Ad Type")

    @property
    def dcm_advertiser(self):
        return MCFDimension(
            name="mcf:dcmAdvertiser", alias="DCM Advertiser Name"
        )

    @property
    def dcm_advertiser_path(self):
        return MCFDimension(
            name="mcf:dcmAdvertiserPath", alias="DCM Advertiser Path"
        )

    @property
    def dcm_campaign(self):
        return MCFDimension(name="mcf:dcmCampaign", alias="DCM Campaign Name")

    @property
    def dcm_campaign_path(self):
        return MCFDimension(
            name="mcf:dcmCampaignPath", alias="DCM Campaign Path"
        )

    @property
    def dcm_creative(self):
        return MCFDimension(name="mcf:dcmCreative", alias="DCM Creative Name")

    @property
    def dcm_creative_path(self):
        return MCFDimension(
            name="mcf:dcmCreativePath", alias="DCM Creative Path"
        )

    @property
    def dcm_creative_version(self):
        return MCFDimension(
            name="mcf:dcmCreativeVersion", alias="DCM Creative Version"
        )

    @property
    def dcm_creative_version_path(self):
        return MCFDimension(
            name="mcf:dcmCreativeVersionPath",
            alias="DCM Creative Version Path",
        )

    @property
    def dcm_network(self):
        return MCFDimension(name="mcf:dcmNetwork", alias="DCM Network")

    @property
    def dcm_placement(self):
        return MCFDimension(name="mcf:dcmPlacement", alias="DCM Placement")

    @property
    def dcm_placement_path(self):
        return MCFDimension(
            name="mcf:dcmPlacementPath", alias="DCM Placement Path"
        )

    @property
    def dcm_site(self):
        return MCFDimension(name="mcf:dcmSite", alias="DCM Site Name")

    @property
    def dcm_site_path(self):
        return MCFDimension(name="mcf:dcmSitePath", alias="DCM Site Path")

    @property
    def path_length_interactions_histogram(self):
        return MCFDimension(
            name="mcf:pathLengthInInteractionsHistogram",
            alias="Path Langth in Iteractions",
        )

    @property
    def time_lag_in_days_histogram(self):
        return MCFDimension(
            name="mcf:timeLagInDaysHistogram", alias="Time Lag in Days"
        )
