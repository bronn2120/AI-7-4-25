<template>
  <div>
    <BigdataAnalyticsMainBanner />
    <BigdataAnalyticsWhatWeDo />
    <BigdataAnalyticsDiscover />
    <BigdataAnalyticsServices />
    <BigdataAnalyticsTeam />
    <BigdataAnalyticsFunFacts />
    <BigdataAnalyticsFeedback />
    <BigdataAnalyticsIndustries />
    <BigdataAnalyticsOurRecentStory />
    <BigdataAnalyticsStartYourFreeTrial />
  </div>
</template>

<script>
import BigdataAnalyticsMainBanner from '~/components/BigdataAnalytics/MainBanner.vue';
import BigdataAnalyticsWhatWeDo from '~/components/BigdataAnalytics/WhatWeDo.vue';
import BigdataAnalyticsDiscover from '~/components/BigdataAnalytics/Discover.vue';
import BigdataAnalyticsServices from '~/components/BigdataAnalytics/Services.vue';
import BigdataAnalyticsTeam from '~/components/BigdataAnalytics/Team.vue';
import BigdataAnalyticsFunFacts from '~/components/BigdataAnalytics/FunFacts.vue';
import BigdataAnalyticsFeedback from '~/components/BigdataAnalytics/Feedback.vue';
import BigdataAnalyticsIndustries from '~/components/BigdataAnalytics/Industries.vue';
import BigdataAnalyticsOurRecentStory from '~/components/BigdataAnalytics/OurRecentStory.vue';
import BigdataAnalyticsStartYourFreeTrial from '~/components/BigdataAnalytics/StartYourFreeTrial.vue';

export default {
  name: 'HomePage',
  components: {
    BigdataAnalyticsMainBanner,
    BigdataAnalyticsWhatWeDo,
    BigdataAnalyticsDiscover,
    BigdataAnalyticsServices,
    BigdataAnalyticsTeam,
    BigdataAnalyticsFunFacts,
    BigdataAnalyticsFeedback,
    BigdataAnalyticsIndustries,
    BigdataAnalyticsOurRecentStory,
    BigdataAnalyticsStartYourFreeTrial
  }
};
</script>