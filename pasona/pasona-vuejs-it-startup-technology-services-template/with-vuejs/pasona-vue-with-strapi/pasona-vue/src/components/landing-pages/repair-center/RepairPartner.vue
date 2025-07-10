<template>
  <div class="repair-partner-area bg-f9fafb">
    <div class="container">
      <div class="partner-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          :breakpoints="breakpoints"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-repair-partner">
              <a href="#">
                <img :src="slide.image" alt="image" />
                <img :src="slide.imageHover" alt="image" />
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
  name: "RepairPartner",
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
        image: require("../../../assets/img/partner-img/partner-1.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover1.png"),
      },
      {
        id: 2,
        image: require("../../../assets/img/partner-img/partner-2.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover2.png"),
      },
      {
        id: 3,
        image: require("../../../assets/img/partner-img/partner-3.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover3.png"),
      },
      {
        id: 4,
        image: require("../../../assets/img/partner-img/partner-4.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover4.png"),
      },
      {
        id: 5,
        image: require("../../../assets/img/partner-img/partner-5.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover5.png"),
      },
      {
        id: 6,
        image: require("../../../assets/img/partner-img/partner-6.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover6.png"),
      },
      {
        id: 1,
        image: require("../../../assets/img/partner-img/partner-7.png"),
        imageHover: require("../../../assets/img/partner-img/partner-hover7.png"),
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 2,
        snapAlign: "center",
      },
      576: {
        itemsToShow: 3,
        snapAlign: "center",
      },
      768: {
        itemsToShow: 5,
        snapAlign: "center",
      },
      1200: {
        itemsToShow: 5,
        snapAlign: "center",
      },
    },
  }),
});
</script>