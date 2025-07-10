<template>
  <div>
    <MainBanner></MainBanner>
    <BoxesArea></BoxesArea>
    <DomainSearch></DomainSearch>
    <WhyChooseUs></WhyChooseUs>
    <PricingPlan></PricingPlan>
    <OurFeedback></OurFeedback>

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
import MainBanner from "./web-hosting/MainBanner";
import BoxesArea from "./web-hosting/BoxesArea";
import DomainSearch from "./web-hosting/DomainSearch";
import WhyChooseUs from "./web-hosting/WhyChooseUs";
import PricingPlan from "./web-hosting/PricingPlan";
import OurFeedback from "./web-hosting/OurFeedback";
import PartnerImage from "./web-hosting/PartnerImage";
import HostingFeatures from "./web-hosting/HostingFeatures";
import OurBlog from "./web-hosting/OurBlog";
import CTAArea from "./web-hosting/CTAArea";

export default {
  name: "WebHosting",
  components: {
    MainBanner,
    BoxesArea,
    DomainSearch,
    WhyChooseUs,
    PricingPlan,
    OurFeedback,
    PartnerImage,
    HostingFeatures,
    OurBlog,
    CTAArea,
  },
};
</script>