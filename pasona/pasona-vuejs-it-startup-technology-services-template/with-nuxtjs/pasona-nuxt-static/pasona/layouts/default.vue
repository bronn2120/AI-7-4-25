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
    <Header v-else></Header>
    <PreLoader v-if="isLoading" />
    <NuxtPage />
    <div
      v-if="currentUrl == '/not-found' || currentUrl == '/coming-soon'"
    ></div>
    <Footer v-else></Footer>
  </div>
</template>

<script>
import Header from "./Header.vue";
import HeaderTwo from "./HeaderTwo.vue";
import HeaderThree from "./HeaderThree.vue";
import HeaderFour from "./HeaderFour.vue";
import HeaderFive from "./HeaderFive.vue";
import Footer from "./Footer.vue";
import PreLoader from "./PreLoader.vue";

export default {
  name: "app",
  components: {
    Header,
    HeaderTwo,
    HeaderThree,
    HeaderFour,
    HeaderFive,
    Footer,
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