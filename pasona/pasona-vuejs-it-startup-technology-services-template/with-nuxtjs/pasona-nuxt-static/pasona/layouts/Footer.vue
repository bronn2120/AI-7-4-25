<template>
  <footer class="footer-area bg-f7fafd">
    <div class="container">
      <div class="row">
        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <div class="logo">
              <NuxtLink to="/">
                <img src="~/assets/img/logo.png" alt="logo" />
              </NuxtLink>
            </div>
            <p>
              Quis ipsum suspendisse ultrices gravida. Risus commodo viverra
              maecenas accumsan lacus vel facilisis.
            </p>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget pl-5">
            <h3>Company</h3>
            <ul class="list">
              <li><NuxtLink to="/about-style-one">About Us</NuxtLink></li>
              <li><NuxtLink to="/service-style-one">Services</NuxtLink></li>
              <li><NuxtLink to="/features">Features</NuxtLink></li>
              <li><NuxtLink to="/pricing">Our Pricing</NuxtLink></li>
              <li><NuxtLink to="/blog-grid">Latest News</NuxtLink></li>
            </ul>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>Support</h3>
            <ul class="list">
              <li><NuxtLink to="/faq">FAQ's</NuxtLink></li>
              <li><NuxtLink to="/project-style-one">Project</NuxtLink></li>
              <li><NuxtLink to="/feedback">Feedback</NuxtLink></li>
              <li><NuxtLink to="/team">Team</NuxtLink></li>
              <li><NuxtLink to="/contact">Contact Us</NuxtLink></li>
            </ul>
          </div>
        </div>

        <div class="col-lg-3 col-md-6 col-sm-6">
          <div class="single-footer-widget">
            <h3>Address</h3>

            <ul class="footer-contact-info">
              <li>
                <MapPinIcon></MapPinIcon> 27 Division St, New York, NY 10002,
                USA
              </li>
              <li>
                <MailIcon></MailIcon> Email:
                <a href="mailto:pasona@gmail.com">pasona@gmail.com</a>
              </li>
              <li>
                <PhoneCallIcon></PhoneCallIcon> Phone:
                <a href="tel:321984754">+ (321) 984 754</a>
              </li>
            </ul>
            <ul class="social-links">
              <li>
                <a class="facebook" href="https://facebook.com/">
                  <FacebookIcon></FacebookIcon>
                </a>
              </li>
              <li>
                <a class="twitter" href="https://twitter.com/">
                  <TwitterIcon></TwitterIcon>
                </a>
              </li>
              <li>
                <a class="linkedin" href="https://linkedin.com/">
                  <LinkedinIcon></LinkedinIcon>
                </a>
              </li>
              <li>
                <a class="instagram" href="https://www.instagram.com/">
                  <GitlabIcon></GitlabIcon>
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div class="col-lg-12 col-md-12">
          <div class="copyright-area">
            <p>Copyright &copy;{{ currentYear }} Pasona. All Rights Reserved</p>
          </div>
        </div>
      </div>
    </div>

    <img src="~/assets/img/map.png" class="map" alt="map" />
    <div class="shape1"><img src="~/assets/img/shape1.png" alt="shape" /></div>
    <div class="shape8 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>

    <div :class="['go-top', { active: isTop }]" @click="scrollToTop()">
      <ArrowUpIcon></ArrowUpIcon>
    </div>
  </footer>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Footer",
  data() {
    return {
      isTop: false,
      currentYear: new Date().getFullYear(),
    };
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
    window.addEventListener("scroll", () => {
      let scrollPos = window.scrollY;
      if (scrollPos >= 100) {
        this.isTop = true;
      } else {
        this.isTop = false;
      }
    });
  },
});
</script>