<template>
  <div>
    <MainBanner></MainBanner>
    <WhatWeDo></WhatWeDo>
    <DiscoverContent></DiscoverContent>
    <OurServices></OurServices>
    <OurTeam></OurTeam>
    <FunFacts></FunFacts>
    <ClientsFeedback></ClientsFeedback>
    <IndustriesServe></IndustriesServe>
    <OurRecentStory></OurRecentStory>
    <StartYourFreeTrial></StartYourFreeTrial>
  </div>
</template>

<script>
import MainBanner from "./bigdata-analytics/MainBanner";
import WhatWeDo from "./bigdata-analytics/WhatWeDo";
import DiscoverContent from "./bigdata-analytics/DiscoverContent";
import OurServices from "./bigdata-analytics/OurServices";
import OurTeam from "./bigdata-analytics/OurTeam";
import FunFacts from "./bigdata-analytics/FunFacts";
import ClientsFeedback from "./bigdata-analytics/ClientsFeedback";
import IndustriesServe from "./bigdata-analytics/IndustriesServe";
import OurRecentStory from "./bigdata-analytics/OurRecentStory";
import StartYourFreeTrial from "./bigdata-analytics/StartYourFreeTrial";

export default {
  name: "BigdataAnalytics",
  components: {
    MainBanner,
    WhatWeDo,
    DiscoverContent,
    OurServices,
    OurTeam,
    FunFacts,
    ClientsFeedback,
    IndustriesServe,
    OurRecentStory,
    StartYourFreeTrial,
  },
};
</script>