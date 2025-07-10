<template>
  <div>
    <MainBanner></MainBanner>
    <BoxesArea></BoxesArea>
    <FeaturesArea></FeaturesArea>
    <OurFeatures></OurFeatures>
    <OurServices></OurServices>
    <OurTeam></OurTeam>
    <FunFacts></FunFacts>
    <PricingPlan></PricingPlan>
    <ClientsFeedback></ClientsFeedback>

    <!-- Start Ready To Talk Area -->
    <div class="ready-to-talk">
      <div class="container">
        <h3>Ready to talk?</h3>
        <p>Our team is here to answer your question about Pasona</p>
        <a href="#" class="btn btn-primary">Contact Us</a>
        <span><a href="#">Or, get started now with a free trial</a></span>
      </div>
    </div>
    <!-- End Ready To Talk Area -->

    <PartnerImage></PartnerImage>
    <OurBlog></OurBlog>
  </div>
</template>

<script>
import MainBanner from "./developer/MainBanner";
import BoxesArea from "./developer/BoxesArea";
import FeaturesArea from "./developer/FeaturesArea";
import OurFeatures from "./developer/OurFeatures";
import OurServices from "./developer/OurServices";
import OurTeam from "./developer/OurTeam";
import FunFacts from "./developer/FunFacts";
import PricingPlan from "./developer/PricingPlan";
import ClientsFeedback from "./developer/ClientsFeedback";
import PartnerImage from "./developer/PartnerImage";
import OurBlog from "./developer/OurBlog";

export default {
  name: "DeveloperPage",
  components: {
    MainBanner,
    BoxesArea,
    FeaturesArea,
    OurFeatures,
    OurServices,
    OurTeam,
    FunFacts,
    PricingPlan,
    ClientsFeedback,
    PartnerImage,
    OurBlog,
  },
};
</script>