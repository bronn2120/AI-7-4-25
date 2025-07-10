<template>
  <div>
    <MainBanner></MainBanner>
    <BoxesArea></BoxesArea>
    <HostingServices></HostingServices>
    <ServicesArea></ServicesArea>
    <OurFeatures></OurFeatures>
    <OurTeam></OurTeam>
    <FunFacts></FunFacts>
    <OurWorks></OurWorks>
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
import MainBanner from "./it-startup/MainBanner";
import BoxesArea from "./it-startup/BoxesArea";
import HostingServices from "./it-startup/HostingServices";
import ServicesArea from "./it-startup/ServicesArea";
import OurFeatures from "./it-startup/OurFeatures";
import OurTeam from "./it-startup/OurTeam";
import FunFacts from "./it-startup/FunFacts";
import OurWorks from "./it-startup/OurWorks";
import PricingPlan from "./it-startup/PricingPlan";
import ClientsFeedback from "./it-startup/ClientsFeedback";
import PartnerImage from "./it-startup/PartnerImage";
import OurBlog from "./it-startup/OurBlog";

export default {
  name: "ITStartup",
  components: {
    MainBanner,
    BoxesArea,
    HostingServices,
    ServicesArea,
    OurFeatures,
    OurTeam,
    FunFacts,
    OurWorks,
    PricingPlan,
    ClientsFeedback,
    PartnerImage,
    OurBlog,
  },
};
</script>