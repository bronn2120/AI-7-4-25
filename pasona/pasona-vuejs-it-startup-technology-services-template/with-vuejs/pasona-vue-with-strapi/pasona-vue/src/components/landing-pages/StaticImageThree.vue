<template>
  <div>
    <MainBanner></MainBanner>
    <BoxesArea></BoxesArea>
    <DomainSearch></DomainSearch>
    <WhyChooseUs></WhyChooseUs>
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
    <HostingFeatures></HostingFeatures>
    <OurBlog></OurBlog>
    <CTAArea></CTAArea>
  </div>
</template>

<script>
import MainBanner from "./static-image-three/MainBanner";
import BoxesArea from "./static-image-three/BoxesArea";
import DomainSearch from "./static-image-three/DomainSearch";
import WhyChooseUs from "./static-image-three/WhyChooseUs";
import PricingPlan from "./static-image-three/PricingPlan";
import ClientsFeedback from "./static-image-three/ClientsFeedback";
import PartnerImage from "./static-image-three/PartnerImage";
import HostingFeatures from "./static-image-three/HostingFeatures";
import OurBlog from "./static-image-three/OurBlog";
import CTAArea from "./static-image-three/CTAArea";

export default {
  name: "BigdataAnalytics",
  components: {
    MainBanner,
    BoxesArea,
    DomainSearch,
    WhyChooseUs,
    PricingPlan,
    ClientsFeedback,
    PartnerImage,
    HostingFeatures,
    OurBlog,
    CTAArea,
  },
};
</script>