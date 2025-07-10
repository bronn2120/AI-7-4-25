<template>
  <div>
    <MainBanner></MainBanner>
    <RepairPartner></RepairPartner>
    <AboutUs></AboutUs>
    <OurServices></OurServices>
    <CtaRepair></CtaRepair>
    <FunFacts></FunFacts>
    <OurTeam></OurTeam>
    <ClientsFeedback></ClientsFeedback>
    <WhyChooseUs></WhyChooseUs>
    <OurBlog></OurBlog>
  </div>
</template>

<script>
import MainBanner from "./repair-center/MainBanner";
import RepairPartner from "./repair-center/RepairPartner";
import AboutUs from "./repair-center/AboutUs";
import OurServices from "./repair-center/OurServices";
import CtaRepair from "./repair-center/CtaRepair";
import FunFacts from "./repair-center/FunFacts";
import OurTeam from "./repair-center/OurTeam";
import ClientsFeedback from "./repair-center/ClientsFeedback";
import WhyChooseUs from "./repair-center/WhyChooseUs";
import OurBlog from "./repair-center/OurBlog";

export default {
  name: "RepairCenter",
  components: {
    MainBanner,
    RepairPartner,
    AboutUs,
    OurServices,
    CtaRepair,
    FunFacts,
    OurTeam,
    ClientsFeedback,
    WhyChooseUs,
    OurBlog,
  },
};
</script>