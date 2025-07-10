<template>
  <div>
    <BigdataAnalyticsMainBanner />
    <BigdataAnalyticsWhatWeDo />
    <BigdataAnalyticsDiscover />
    <BigdataAnalyticsServices />
    <BigdataAnalyticsTeam />
    <BigdataAnalyticsFunFacts />
    <BigdataAnalyticsFeedback />
    <BigdataAnalyticsIndustries />
    <BigdataAnalyticsOurRecentStory />
    <BigdataAnalyticsStartYourFreeTrial />

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
export default {
  name: 'BigdataAnalytics',
  computed: {
    showChatButton() {
      return this.$route.path !== '/support';
    }
  }
};
</script>

<style scoped>
.floating-chat-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #007bff; /* Matches Pasona blue theme */
  color: white;
  padding: 12px 24px; /* Slightly larger for better touch targets */
  border-radius: 50px;
  text-decoration: none;
  box-shadow: 0 6px 12px rgba(0, 123, 255, 0.3); /* Softer shadow for modern look */
  z-index: 1000;
  font-size: 1.1rem;
  font-family: Arial, sans-serif; /* Matches your existing font */
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease; /* Added transform for hover effect */
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.floating-chat-button:hover {
  background-color: #0056b3; /* Darker blue on hover */
  transform: translateY(-2px); /* Slight lift on hover */
}

.floating-chat-button:focus {
  outline: 3px solid #0056b3;
  outline-offset: 2px;
  background-color: #0056b3; /* Focus state matches hover */
}

.floating-chat-button span {
  display: inline-block;
  text-align: center;
  font-weight: 500; /* Slightly bold for emphasis */
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