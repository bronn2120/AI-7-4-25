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
import MainBanner from "./ai-machine-learning/MainBanner";
import PartnerImage from "./ai-machine-learning/PartnerImage";
import OurFeaturedSolutions from "./ai-machine-learning/OurFeaturedSolutions";
import AboutUs from "./ai-machine-learning/AboutUs";
import OurServices from "./ai-machine-learning/OurServices";
import FunFacts from "./ai-machine-learning/FunFacts";
import OurProjects from "./ai-machine-learning/OurProjects";
import PricingPlan from "./ai-machine-learning/PricingPlan";
import ClientsFeedback from "./ai-machine-learning/ClientsFeedback";
import OurBlog from "./ai-machine-learning/OurBlog";
import FreeTrial from "./ai-machine-learning/FreeTrial";

export default {
  name: "AiMachineLearning",
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