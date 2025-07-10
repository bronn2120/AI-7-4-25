<template>
  <div>
    <MainBanner></MainBanner>
    <PartnerImage></PartnerImage>
    <OurServices></OurServices>
    <CtaIot></CtaIot>
    <FunFacts></FunFacts>
    <OurFeatures></OurFeatures>
    <FeaturesTwo></FeaturesTwo>
    <OurTeam></OurTeam>
    <ClientsFeedback></ClientsFeedback>
    <WhyChooseUs></WhyChooseUs>
    <OurBlog></OurBlog>
  </div>
</template>

<script>
import MainBanner from "./iot/MainBanner";
import PartnerImage from "./iot/PartnerImage";
import OurServices from "./iot/OurServices";
import CtaIot from "./iot/CtaIot";
import FunFacts from "./iot/FunFacts";
import OurFeatures from "./iot/OurFeatures";
import FeaturesTwo from "./iot/FeaturesTwo";
import OurTeam from "./iot/OurTeam";
import ClientsFeedback from "./iot/ClientsFeedback";
import WhyChooseUs from "./iot/WhyChooseUs";
import OurBlog from "./iot/OurBlog";

export default {
  name: "IotPage",
  components: {
    MainBanner,
    PartnerImage,
    OurServices,
    CtaIot,
    FunFacts,
    OurFeatures,
    FeaturesTwo,
    OurTeam,
    ClientsFeedback,
    WhyChooseUs,
    OurBlog,
  },
};
</script>