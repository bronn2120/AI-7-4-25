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
    <ReadyToTalk></ReadyToTalk>
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
import ReadyToTalk from "./it-startup/ReadyToTalk";
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
    ReadyToTalk,
    PartnerImage,
    OurBlog,
  },
};
</script>