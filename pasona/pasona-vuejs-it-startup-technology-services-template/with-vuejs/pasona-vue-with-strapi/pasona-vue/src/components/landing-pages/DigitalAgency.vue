<template>
  <div>
    <MainBanner></MainBanner>
    <OurFeaturedSolutions></OurFeaturedSolutions>
    <AboutUs></AboutUs>
    <OurServices></OurServices>
    <FunFacts></FunFacts>
    <OurProjects></OurProjects>
    <PricingPlan></PricingPlan>
    <ClientsFeedback></ClientsFeedback>
    <OurBlog></OurBlog>

    <!-- Start CTA Area -->
    <div class="agency-cta-area ptb-80">
      <div class="container">
        <div class="agency-cta-content">
          <h2>Do you have any projects?</h2>
          <a href="#" class="btn btn-gradient">Contact Us</a>
        </div>
      </div>
    </div>
    <!-- End CTA Area -->
  </div>
</template>

<script>
import MainBanner from "./digital-agency/MainBanner";
import OurFeaturedSolutions from "./digital-agency/OurFeaturedSolutions";
import AboutUs from "./digital-agency/AboutUs";
import OurServices from "./digital-agency/OurServices";
import FunFacts from "./digital-agency/FunFacts";
import OurProjects from "./digital-agency/OurProjects";
import PricingPlan from "./digital-agency/PricingPlan";
import ClientsFeedback from "./digital-agency/ClientsFeedback";
import OurBlog from "./digital-agency/OurBlog";

export default {
  name: "DigitalAgency",
  components: {
    MainBanner,
    OurFeaturedSolutions,
    AboutUs,
    OurServices,
    FunFacts,
    OurProjects,
    PricingPlan,
    ClientsFeedback,
    OurBlog,
  },
};
</script>