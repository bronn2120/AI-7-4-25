<template>
  <div>
    <HeaderTwo v-if="currentUrl == '/web-hosting'"></HeaderTwo>
    <HeaderTwo v-else-if="currentUrl == '/static-image-three'"></HeaderTwo>
    <HeaderThree v-else-if="currentUrl == '/machine-learning'"></HeaderThree>
    <HeaderThree v-else-if="currentUrl == '/agency-portfolio'"></HeaderThree>
    <HeaderFour v-else-if="currentUrl == '/digital-agency'"></HeaderFour>
    <HeaderFive v-else-if="currentUrl == '/bigdata-analytics'"></HeaderFive>
    <div
      v-else-if="currentUrl == '/not-found' || currentUrl == '/coming-soon'"
    ></div>
    <MainHeader v-else></MainHeader>
    <PreLoader v-if="isLoading" />
    <router-view />
    <div
      v-if="currentUrl == '/not-found' || currentUrl == '/coming-soon'"
    ></div>
    <MainFooter v-else></MainFooter>
  </div>
</template>

<script>
import MainHeader from "./components/layout/MainHeader";
import HeaderTwo from "./components/layout/HeaderTwo";
import HeaderThree from "./components/layout/HeaderThree";
import HeaderFour from "./components/layout/HeaderFour";
import HeaderFive from "./components/layout/HeaderFive";
import MainFooter from "./components/layout/MainFooter";
import PreLoader from "./components/layout/PreLoader";

export default {
  name: "app",
  components: {
    MainHeader,
    HeaderTwo,
    HeaderThree,
    HeaderFour,
    HeaderFive,
    MainFooter,
    PreLoader,
  },
  data() {
    return {
      isLoading: true,
      currentUrl: "",
    };
  },
  watch: {
    $route(pathUrl) {
      this.currentUrl = pathUrl.path;
      this.isLoading = true;
      setTimeout(() => {
        this.isLoading = false;
      }, 1500);
    },
  },
  mounted() {
    this.currentUrl = window.location.pathname;
    setTimeout(() => {
      this.isLoading = false;
    }, 2000);
  },
};
</script>
