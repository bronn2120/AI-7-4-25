<template>
  <div>
    <HeaderTwo v-if="currentUrl == '/web-hosting'"></HeaderTwo>
    <HeaderTwo v-else-if="currentUrl == '/static-image-three'"></HeaderTwo>
    <HeaderThree v-else-if="currentUrl == '/machine-learning'"></HeaderThree>
    <HeaderThree v-else-if="currentUrl == '/agency-portfolio'"></HeaderThree>
    <HeaderFour v-else-if="currentUrl == '/digital-agency'"></HeaderFour>
    <HeaderFive v-else-if="currentUrl == '/bigdata-analytics'"></HeaderFive>
    <div v-else-if="currentUrl == '/not-found' || currentUrl == '/coming-soon'"></div>
    <Header v-else></Header>
    <PreLoader v-if="isLoading" />
    <NuxtPage />
    <div v-if="currentUrl == '/not-found' || currentUrl == '/coming-soon'"></div>
    <Footer v-else></Footer>

    <!-- Floating Chat Button -->
    <router-link
      v-if="showChatButton"
      to="/support"
      class="floating-chat-button"
      role="button"
      aria-label="Open support chat with ixome.ai"
    >
      <span>Chat with Us</span>
    </router-link>
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
import { useRoute } from 'vue-router';

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
  computed: {
    showChatButton() {
      return this.$route.path !== '/support';
    }
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

<style scoped>
.floating-chat-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #007bff; /* Matches Pasona blue theme */
  color: white;
  padding: 12px 24px;
  border-radius: 50px;
  text-decoration: none;
  box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3);
  z-index: 1000;
  font-size: 1.1rem;
  font-family: Arial, sans-serif;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.floating-chat-button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.floating-chat-button:focus {
  outline: 3px solid #0056b3;
  outline-offset: 2px;
  background-color: #0056b3;
}

.floating-chat-button span {
  display: inline-block;
  text-align: center;
  font-weight: 500;
}

@media (max-width: 768px) {
  .floating-chat-button {
    bottom: 10px;
    right: 10px;
    padding: 10px 18px;
    font-size: 1rem;
  }
}
</style>