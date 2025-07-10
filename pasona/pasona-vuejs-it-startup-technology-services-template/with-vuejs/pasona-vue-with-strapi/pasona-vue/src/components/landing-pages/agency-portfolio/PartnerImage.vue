<template>
  <div class="agency-portfolio-partner-area ptb-80">
    <div class="container">
      <div class="agency-portfolio-partner-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          :breakpoints="breakpoints"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-agency-portfolio-partner">
              <a href="#">
                <img :src="slide.image" alt="image" />
              </a>
            </div>
          </slide>

          <template #addons> </template>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "PartnerImage",
  components: {
    Carousel,
    Slide,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    carouselItems: [
      {
        id: 1,
        image: require("../../../assets/img/agency-portfolio-partner-image/img1.png"),
      },
      {
        id: 2,
        image: require("../../../assets/img/agency-portfolio-partner-image/img2.png"),
      },
      {
        id: 3,
        image: require("../../../assets/img/agency-portfolio-partner-image/img3.png"),
      },
      {
        id: 4,
        image: require("../../../assets/img/agency-portfolio-partner-image/img4.png"),
      },
      {
        id: 5,
        image: require("../../../assets/img/agency-portfolio-partner-image/img5.png"),
      },
      {
        id: 6,
        image: require("../../../assets/img/agency-portfolio-partner-image/img6.png"),
      },
      {
        id: 7,
        image: require("../../../assets/img/agency-portfolio-partner-image/img2.png"),
      },
      {
        id: 8,
        image: require("../../../assets/img/agency-portfolio-partner-image/img3.png"),
      },
      {
        id: 9,
        image: require("../../../assets/img/agency-portfolio-partner-image/img4.png"),
      },
      {
        id: 10,
        image: require("../../../assets/img/agency-portfolio-partner-image/img5.png"),
      },
      {
        id: 11,
        image: require("../../../assets/img/agency-portfolio-partner-image/img6.png"),
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      576: {
        itemsToShow: 2,
        snapAlign: "center",
      },
      768: {
        itemsToShow: 4,
        snapAlign: "center",
      },
      992: {
        itemsToShow: 5,
        snapAlign: "center",
      },
    },
  }),
});
</script>