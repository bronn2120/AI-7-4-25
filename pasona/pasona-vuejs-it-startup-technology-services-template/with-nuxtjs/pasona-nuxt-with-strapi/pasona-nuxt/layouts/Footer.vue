<template>
  <div class="footer-area bg-f7fafd">
    <div class="container">
      <div class="row" v-if="footer">
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <div class="logo">
              <NuxtLink to="/">
                <img v-if="footerLogoUrl" :src="footerLogoUrl" alt="ixome.ai logo" />
                <img v-else src="~/assets/img/logo.png" alt="ixome.ai default logo" />
              </NuxtLink>
            </div>
            <p>{{ footer.shortDesc || "Site footer description" }}</p>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget pl-5">
            <h3>{{ footer.title || "Company" }}</h3>
            <ul class="list">
              <li v-for="company in footer.companyLists || []" :key="company.id">
                <NuxtLink v-if="isInternalLink(company.link)" :to="mapInternalLink(company.link)" class="footer-link">{{ company.title }}</NuxtLink>
                <a v-else :href="company.link" target="_blank" class="footer-link">{{ company.title }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>{{ footer.titleTwo || "Support" }}</h3>
            <ul class="list">
              <li v-for="support in footer.supportLists || []" :key="support.id">
                <NuxtLink v-if="isInternalLink(support.link)" :to="mapInternalLink(support.link)" class="footer-link">{{ support.title }}</NuxtLink>
                <a v-else :href="support.link" target="_blank" class="footer-link">{{ support.title }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>{{ footer.titleThree || "Contact" }}</h3>
            <ul class="footer-contact-info">
              <li><MapPinIcon aria-label="Location"></MapPinIcon>{{ footer.address || "123 Example St" }}</li>
              <li><MailIcon aria-label="Email"></MailIcon>Email: <a :href="`mailto:${footer.email || 'contact@example.com'}`">{{ footer.email || "contact@example.com" }}</a></li>
              <li><PhoneCallIcon aria-label="Phone"></PhoneCallIcon>Phone: <a :href="`tel:${footer.phone || '123-456-7890'}`">{{ footer.phone || "123-456-7890" }}</a></li>
            </ul>
            <ul class="social-links">
              <li v-for="social in footer.socialLink || []" :key="social.id">
                <a class="facebook" :href="parseSocialLink(social.link)" target="_blank" :aria-label="social.title || 'Social Media'"><i :class="social.icon || 'fab fa-facebook'"></i></a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-lg-12 col-md-12">
          <div class="copyright-area">
            <p>Copyright ©{{ currentYear }} Pasona. All Rights Reserved</p>
          </div>
        </div>
      </div>
    </div>
    <img src="~/assets/img/map.png" class="map" alt="map" />
    <div class="shape1"><img src="~/assets/img/shape1.png" alt="shape" /></div>
    <div class="shape8 rotateme"><img src="~/assets/img/shape2.svg" alt="shape" /></div>
    <div :class="['go-top', { active: isTop }]" @click="scrollToTop()" role="button" aria-label="Scroll to top">
      <ArrowUpIcon></ArrowUpIcon>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "Footer",
  setup() {
    const isTop = ref(false);
    const currentYear = ref(new Date().getFullYear());
    const footer = ref(null);
    const footerLogoUrl = ref<string | null>(null);
    const STRAPI_BASE_URL = "http://localhost:1337"; // Strapi base URL

    const scrollToTop = () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    const isInternalLink = (link: string) => {
      return link && (link.startsWith("/") || link === "ixome.ai");
    };

    const mapInternalLink = (link: string) => {
      if (link === "ixome.ai") {
        return "/";
      }
      return link;
    };

    const parseSocialLink = (link: string) => {
      try {
        const parsed = JSON.parse(link.replace("socialLink: ", ""));
        return parsed.link || "https://facebook.com";
      } catch {
        return link || "https://facebook.com";
      }
    };

    onMounted(async () => {
      window.addEventListener("scroll", () => {
        let scrollPos = window.scrollY;
        isTop.value = scrollPos >= 100;
      });

      try {
        const timestamp = new Date().getTime();
        const footerResponse = await axios.get(`${STRAPI_BASE_URL}/api/footer?populate=deep&_=${timestamp}`);
        const footerAttributes = footerResponse.data.data?.attributes;
        footer.value = footerAttributes || {};

        // If footer doesn't have a logo, fetch it from /api/sitelogo
        if (!footerAttributes?.logo?.data?.attributes?.url) {
          const sitelogoResponse = await axios.get(`${STRAPI_BASE_URL}/api/sitelogo?populate=deep&_=${timestamp}`);
          const sitelogoAttributes = sitelogoResponse.data.data?.attributes;
          const relativeUrl = sitelogoAttributes?.SHT?.data?.attributes?.url || null;
          footerLogoUrl.value = relativeUrl ? `${STRAPI_BASE_URL}${relativeUrl}` : null;
        } else {
          const relativeUrl = footerAttributes?.logo?.data?.attributes?.url || null;
          footerLogoUrl.value = relativeUrl ? `${STRAPI_BASE_URL}${relativeUrl}` : null;
        }
      } catch (error) {
        console.error("Error fetching footer data:", error);
      }
    });

    return {
      isTop,
      currentYear,
      footer,
      footerLogoUrl,
      scrollToTop,
      isInternalLink,
      mapInternalLink,
      parseSocialLink,
    };
  },
});
</script>

<style scoped>
.footer-link {
  text-decoration: none;
  color: #333;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #007bff; /* Matches Pasona blue theme */
}

.go-top {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.go-top:hover {
  background-color: #0056b3; /* Darker blue on hover */
}
</style>