<template>
  <div>
    <MainBanner></MainBanner>
    <BoxesArea></BoxesArea>
    <OurServices></OurServices>
    <ServicesArea></ServicesArea>
    <OurFeatures></OurFeatures>
    <OurTeam></OurTeam>
    <FunFacts></FunFacts>
    <OurRecent></OurRecent>
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
import MainBanner from "./static-image-one/MainBanner";
import BoxesArea from "./static-image-one/BoxesArea";
import OurServices from "./static-image-one/OurServices";
import ServicesArea from "./static-image-one/ServicesArea";
import OurFeatures from "./static-image-one/OurFeatures";
import OurTeam from "./static-image-one/OurTeam";
import FunFacts from "./static-image-one/FunFacts";
import OurRecent from "./static-image-one/OurRecent";
import PricingPlan from "./static-image-one/PricingPlan";
import ClientsFeedback from "./static-image-one/ClientsFeedback";
import PartnerImage from "./static-image-one/PartnerImage";
import OurBlog from "./static-image-one/OurBlog";

export default {
  name: "BigdataAnalytics",
  components: {
    MainBanner,
    BoxesArea,
    OurServices,
    ServicesArea,
    OurFeatures,
    OurTeam,
    FunFacts,
    OurRecent,
    PricingPlan,
    ClientsFeedback,
    PartnerImage,
    OurBlog,
  },
};
</script>