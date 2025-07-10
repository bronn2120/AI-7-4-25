<template>
  <div>
    <NuxtLayout>
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
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { defineComponent } from 'vue';

defineComponent({
  name: 'App',
  setup() {
    const route = useRoute();
    const showChatButton = computed(() => route.path !== '/support');

    return { showChatButton };
  },
});

useHead({
  title: "Pasona - Nuxt.js IT Startup & Technology Services Template",
  meta: [{ name: "description", content: "My amazing site." }],
});
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