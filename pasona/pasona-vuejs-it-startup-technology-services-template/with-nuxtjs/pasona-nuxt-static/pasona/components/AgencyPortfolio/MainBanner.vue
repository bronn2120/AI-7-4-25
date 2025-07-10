<template>
  <div class="agency-portfolio-home-slides">
    <carousel
      :autoplay="5000"
      :settings="settings"
      :wrap-around="true"
      pause-autoplay-on-hover
    >
      <slide v-for="slide in carouselItems" :key="slide.id">
        <div :class="slide.class">
          <div class="d-table">
            <div class="d-table-cell">
              <div class="container">
                <div class="portfolio-banner-content">
                  <span class="sub-title">{{ slide.subTitle }}</span>
                  <h1>{{ slide.heading }}</h1>
                  <p>{{ slide.description }}</p>
                  <a href="#" class="btn btn-secondary">Get Started</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </slide>

      <template #addons>
        <navigation>
          <template #next>
            <i class="bx bx-chevron-right"></i>
          </template>
          <template #prev>
            <i class="bx bx-chevron-left"></i>
          </template>
        </navigation>
      </template>
    </carousel>
  </div>
</template>
  
<script lang="ts">
import { defineComponent } from "vue";
import { Carousel, Slide, Navigation } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "MainBanner",
  components: {
    Carousel,
    Slide,
    Navigation,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    carouselItems: [
      {
        id: 1,
        class: "agency-portfolio-main-banner portfolio-banner-bg1",
        subTitle: "WE ARE CREATIVE",
        heading: "Digital Agency",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
      },
      {
        id: 2,
        class: "agency-portfolio-main-banner portfolio-banner-bg2",
        subTitle: "WE ARE DIGITAL",
        heading: "UX/UI Design",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
      },
      {
        id: 3,
        class: "agency-portfolio-main-banner portfolio-banner-bg3",
        subTitle: "WE ARE AGENCY",
        heading: "Digital Marketing",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
      },
    ],
  }),
});
</script>