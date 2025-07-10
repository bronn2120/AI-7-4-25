<template>
  <div>
    <MainBanner></MainBanner>
    <OurLatestProjects></OurLatestProjects>
    <AboutUs></AboutUs>
    <ClientsFeedback></ClientsFeedback>
    <PartnerImage></PartnerImage>
    <OurRecentNews></OurRecentNews>
    <CreativeInner></CreativeInner>
  </div>
</template>

<script>
import MainBanner from "./agency-portfolio/MainBanner";
import OurLatestProjects from "./agency-portfolio/OurLatestProjects";
import AboutUs from "./agency-portfolio/AboutUs";
import ClientsFeedback from "./agency-portfolio/ClientsFeedback";
import PartnerImage from "./agency-portfolio/PartnerImage";
import OurRecentNews from "./agency-portfolio/OurRecentNews";
import CreativeInner from "./agency-portfolio/CreativeInner";

export default {
  name: "AgencyPortfolio",
  components: {
    MainBanner,
    OurLatestProjects,
    AboutUs,
    ClientsFeedback,
    PartnerImage,
    OurRecentNews,
    CreativeInner,
  },
};
</script>