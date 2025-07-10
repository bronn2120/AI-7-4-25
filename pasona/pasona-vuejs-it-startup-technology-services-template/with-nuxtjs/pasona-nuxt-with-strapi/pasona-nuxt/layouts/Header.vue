<template>
  <header id="header" :class="['headroom', { 'is-sticky': isSticky }]">
    <div class="startp-nav">
      <div class="container">
        <nav class="navbar navbar-expand-md navbar-light">
          <NuxtLink class="navbar-brand" to="/">
            <img v-if="logoUrl" :src="logoUrl" alt="ixome.ai logo" />
            <img v-else src="~/assets/img/logo.png" alt="ixome.ai default logo" />
          </NuxtLink>
          <b-navbar-toggle target="navbarSupportedContent"></b-navbar-toggle>
          <b-collapse class="collapse navbar-collapse mean-menu" id="navbarSupportedContent" is-nav>
            <ul class="navbar-nav nav ml-auto">
              <li class="nav-item"><NuxtLink to="/" class="nav-link" exact>Home</NuxtLink></li>
              <li class="nav-item"><NuxtLink to="/about-style-one" class="nav-link">About</NuxtLink></li>
              <li class="nav-item"><NuxtLink to="/shop" class="nav-link">Shop</NuxtLink></li>
              <li class="nav-item">
                <a href="#" class="nav-link">Pages<ChevronDownIcon></ChevronDownIcon></a>
                <ul class="dropdown_menu">
                  <li class="nav-item">
                    <a href="#" class="nav-link">Features<ChevronDownIcon></ChevronDownIcon></a>
                    <ul class="dropdown_menu">
                      <li class="nav-item"><NuxtLink to="/features" class="nav-link">Features</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/feature-details" class="nav-link">Features Details</NuxtLink></li>
                    </ul>
                  </li>
                  <li class="nav-item">
                    <a href="#" class="nav-link">Services<ChevronDownIcon></ChevronDownIcon></a>
                    <ul class="dropdown_menu">
                      <li class="nav-item"><NuxtLink to="/service-style-one" class="nav-link">Services Style 1</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/service-style-two" class="nav-link">Services Style 2</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/service-style-three" class="nav-link">Services Style 3</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/service-style-four" class="nav-link">Services Style 4</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/service-style-five" class="nav-link">Services Style 5</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/service-details" class="nav-link">Services Details</NuxtLink></li>
                    </ul>
                  </li>
                  <li class="nav-item"><NuxtLink to="/feedback" class="nav-link">Feedback</NuxtLink></li>
                  <li class="nav-item">
                    <a href="#" class="nav-link">Project<ChevronDownIcon></ChevronDownIcon></a>
                    <ul class="dropdown_menu">
                      <li class="nav-item"><NuxtLink to="/project-style-one" class="nav-link">Project Style 1</NuxtLink></li>
                      <li class="nav-item"><NuxtLink to="/project-details/incredible-infrastructure" class="nav-link">Project Details</NuxtLink></li>
                    </ul>
                  </li>
                  <li class="nav-item"><NuxtLink to="/team" class="nav-link">Team</NuxtLink></li>
                  <li class="nav-item"><NuxtLink to="/pricing" class="nav-link">Pricing</NuxtLink></li>
                  <li class="nav-item"><NuxtLink to="/faq" class="nav-link">FAQ</NuxtLink></li>
                  <li class="nav-item"><NuxtLink to="/coming-soon" class="nav-link">Coming Soon</NuxtLink></li>
                </ul>
              </li>
              <li class="nav-item">
                <a href="#" class="nav-link">Blog<ChevronDownIcon></ChevronDownIcon></a>
                <ul class="dropdown_menu">
                  <li class="nav-item"><NuxtLink to="/blog-grid" class="nav-link">Blog Grid</NuxtLink></li>
                  <li class="nav-item"><NuxtLink to="/blog-details/the-security-risks-of-changing-package-owners" class="nav-link">Blog Details</NuxtLink></li>
                </ul>
              </li>
              <li class="nav-item"><NuxtLink to="/contact" class="nav-link">Contact</NuxtLink></li>
            </ul>
          </b-collapse>
          <div class="others-option">
            <NuxtLink to="/cart" class="cart-wrapper-btn"><ShoppingCartIcon></ShoppingCartIcon><span>{{ cartStore.productsTotal }}</span></NuxtLink>
            <NuxtLink to="/support" class="btn btn-light">Support</NuxtLink>
            <a href="#" class="btn btn-primary">Login</a>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { useCartStore } from "../store/cart";
import axios from "axios";

export default defineComponent({
  name: "Header",
  setup() {
    const isSticky = ref(false);
    const cartStore = useCartStore();
    const logoUrl = ref<string | null>(null);
    const STRAPI_BASE_URL = "http://localhost:1337"; // Strapi base URL

    onMounted(async () => {
      window.addEventListener("scroll", () => {
        let scrollPos = window.scrollY;
        isSticky.value = scrollPos >= 100;
      });

      try {
        const timestamp = new Date().getTime();
        const response = await axios.get(`${STRAPI_BASE_URL}/api/sitelogo?populate=deep&_=${timestamp}`);
        const attributes = response.data.data?.attributes;
        const relativeUrl = attributes?.SHT?.data?.attributes?.url || attributes?.Vincent || null;
        logoUrl.value = relativeUrl ? `${STRAPI_BASE_URL}${relativeUrl}` : null;
      } catch (error) {
        console.error("Error fetching logo:", error);
      }
    });

    return {
      isSticky,
      cartStore,
      logoUrl,
    };
  },
});
</script>

<style scoped>
/* Ensure the header stays on top and has a defined height */
#header {
  position: relative; /* Use relative positioning unless fixed is needed */
  z-index: 20; /* Ensure header is above other elements */
  height: 60px; /* Define a consistent height */
  padding: 10px 0; /* Add padding for spacing */
}

/* Style the navbar-brand container */
.navbar-brand {
  display: flex;
  align-items: center; /* Center the logo vertically */
  justify-content: center; /* Center the logo horizontally */
  height: 100%; /* Match the header height */
}

/* Style the logo image */
.navbar-brand img {
  max-width: 150px; /* Keep your desired width */
  max-height: 40px; /* Slightly reduce height to fit within header */
  width: auto;
  height: auto;
  display: block; /* Keep this to avoid inline spacing issues */
}

/* Ensure the navbar doesn’t overlap with content below */
.startp-nav {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Distribute space evenly */
  height: 100%;
}

/* Responsive adjustments for smaller screens */
@media (max-width: 768px) {
  .navbar-brand img {
    max-width: 120px; /* Reduce logo size on smaller screens */
    max-height: 35px;
  }
}

/* Style the Support button to match the floating chat button */
.others-option .btn-light {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.others-option .btn-light:hover {
  background-color: #0056b3;
}

.others-option .btn-light:focus {
  outline: 2px solid #0056b3;
  outline-offset: 2px;
}
</style>