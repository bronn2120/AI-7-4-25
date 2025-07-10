<template>
  <div class="agency-portfolio-partner-area ptb-80">
    <div class="container">
      <div class="agency-portfolio-partner-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrap-around="true"
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

import image1 from "~/assets/img/agency-portfolio-partner-image/img1.png";
import image2 from "~/assets/img/agency-portfolio-partner-image/img2.png";
import image3 from "~/assets/img/agency-portfolio-partner-image/img3.png";
import image4 from "~/assets/img/agency-portfolio-partner-image/img4.png";
import image5 from "~/assets/img/agency-portfolio-partner-image/img5.png";
import image6 from "~/assets/img/agency-portfolio-partner-image/img6.png";

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
        image: image1,
      },
      {
        id: 2,
        image: image2,
      },
      {
        id: 3,
        image: image3,
      },
      {
        id: 4,
        image: image4,
      },
      {
        id: 5,
        image: image5,
      },
      {
        id: 6,
        image: image6,
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      576: {
        itemsToShow: 2,
        snapAlign: "left",
      },
      768: {
        itemsToShow: 4,
        snapAlign: "left",
      },
      992: {
        itemsToShow: 5,
        snapAlign: "center",
      },
    },
  }),
});
</script>