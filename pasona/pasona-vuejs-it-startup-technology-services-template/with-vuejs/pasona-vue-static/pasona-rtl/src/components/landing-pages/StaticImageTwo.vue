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
import MainBanner from "./static-image-two/MainBanner";
import BoxesArea from "./static-image-two/BoxesArea";
import FeaturesArea from "./static-image-two/FeaturesArea";
import OurFeatures from "./static-image-two/OurFeatures";
import OurServices from "./static-image-two/OurServices";
import OurTeam from "./static-image-two/OurTeam";
import FunFacts from "./static-image-two/FunFacts";
import PricingPlan from "./static-image-two/PricingPlan";
import ClientsFeedback from "./static-image-two/ClientsFeedback";
import PartnerImage from "./static-image-two/PartnerImage";
import OurBlog from "./static-image-two/OurBlog";

export default {
  name: "BigdataAnalytics",
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