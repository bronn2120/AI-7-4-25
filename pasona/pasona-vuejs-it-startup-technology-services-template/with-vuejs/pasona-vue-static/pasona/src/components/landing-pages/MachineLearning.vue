<template>
  <div>
    <MainBanner></MainBanner>
    <PartnerImage></PartnerImage>
    <OurFeaturedSolutions></OurFeaturedSolutions>
    <AboutUs></AboutUs>
    <OurServices></OurServices>
    <FunFacts></FunFacts>
    <OurProjects></OurProjects>
    <PricingPlan></PricingPlan>
    <ClientsFeedback></ClientsFeedback>
    <OurBlog></OurBlog>
    <FreeTrial></FreeTrial>
  </div>
</template>

<script>
import MainBanner from "./machine-learning/MainBanner";
import PartnerImage from "./machine-learning/PartnerImage";
import OurFeaturedSolutions from "./machine-learning/OurFeaturedSolutions";
import AboutUs from "./machine-learning/AboutUs";
import OurServices from "./machine-learning/OurServices";
import FunFacts from "./machine-learning/FunFacts";
import OurProjects from "./machine-learning/OurProjects";
import PricingPlan from "./machine-learning/PricingPlan";
import ClientsFeedback from "./machine-learning/ClientsFeedback";
import OurBlog from "./machine-learning/OurBlog";
import FreeTrial from "./machine-learning/FreeTrial";

export default {
  name: "MachineLearning",
  components: {
    MainBanner,
    PartnerImage,
    OurFeaturedSolutions,
    AboutUs,
    OurServices,
    FunFacts,
    OurProjects,
    PricingPlan,
    ClientsFeedback,
    OurBlog,
    FreeTrial,
  },
};
</script>