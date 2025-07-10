<template>
  <footer class="footer-area bg-f7fafd">
    <div class="container">
      <div class="row" v-if="footer">
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <div class="logo">
              <router-link to="/">
                <img :src="footer.logo.data.attributes.url" alt="logo" />
              </router-link>
            </div>
            <p>
              {{ footer.shortDesc }}
            </p>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget pl-5">
            <h3>{{ footer.title }}</h3>
            <ul class="list">
              <li v-for="company in footer.companyLists" :key="company.id">
                <NuxtLink :to="company.link">
                  {{ company.title }}
                </NuxtLink>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>{{ footer.titleTwo }}</h3>
            <ul class="list">
              <li v-for="support in footer.supportLists" :key="support.id">
                <NuxtLink :to="support.link">
                  {{ support.title }}
                </NuxtLink>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>{{ footer.titleThree }}</h3>

            <ul class="footer-contact-info">
              <li>
                <vue-feather type="map-pin"></vue-feather>
                {{ footer.address }}
              </li>
              <li>
                <vue-feather type="mail"></vue-feather> Email:
                <a :href="`mailto:${footer.email}`">
                  {{ footer.email }}
                </a>
              </li>
              <li>
                <vue-feather type="phone-call"></vue-feather> Phone:
                <a :href="`tel:${footer.phone}`">
                  {{ footer.phone }}
                </a>
              </li>
            </ul>
            <ul class="social-links">
              <li v-for="social in footer.socialLink" :key="social.id">
                <a class="facebook" :href="social.link">
                  <vue-feather :type="social.icon"></vue-feather>
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-12 col-md-12">
          <div class="copyright-area">
            <p>
              Copyright &copy; {{ currentYear }} Pasona. All Rights Reserved
            </p>
          </div>
        </div>
      </div>
    </div>

    <img src="../../assets/img/map.png" class="map" alt="map" />
    <div class="shape1">
      <img src="../../assets/img/shape1.png" alt="shape" />
    </div>
    <div class="shape8 rotateme">
      <img src="../../assets/img/shape2.svg" alt="shape" />
    </div>

    <div
      @click="scrollToTop()"
      :class="['back-to-top-btn', { 'go-top': isTop }]"
    >
      <vue-feather type="arrow-up"></vue-feather>
    </div>
  </footer>
</template>

<script>
import axios from "axios";

export default {
  name: "MainFooter",
  data() {
    return {
      isTop: false,
      currentYear: new Date().getFullYear(),
      footer: null,
    };
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
    const that = this;
    window.addEventListener("scroll", () => {
      let scrollPos = window.scrollY;
      if (scrollPos >= 100) {
        that.isTop = true;
      } else {
        that.isTop = false;
      }
    });
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/footer?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.footer = attributes;
  },
};
</script>