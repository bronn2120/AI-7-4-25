<template>
  <div class="repair-partner-area bg-f9fafb">
    <div class="container">
      <div class="partner-slides">
        <carousel
          :autoplay="5000"
          :wrap-around="true"
          :settings="settings"
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
        </carousel>
      </div>
    </div>
  </div>
</template>


<script>
import { defineComponent } from "vue";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

import image1 from '../../../assets/img/partner-img/partner-1.png'
import image2 from '../../../assets/img/partner-img/partner-2.png'
import image3 from '../../../assets/img/partner-img/partner-3.png'
import image4 from '../../../assets/img/partner-img/partner-4.png'
import image5 from '../../../assets/img/partner-img/partner-5.png'
import image6 from '../../../assets/img/partner-img/partner-6.png'
import image7 from '../../../assets/img/partner-img/partner-7.png'
import imageHover1 from '../../../assets/img/partner-img/partner-hover1.png'
import imageHover2 from '../../../assets/img/partner-img/partner-hover2.png'
import imageHover3 from '../../../assets/img/partner-img/partner-hover3.png'
import imageHover4 from '../../../assets/img/partner-img/partner-hover4.png'
import imageHover5 from '../../../assets/img/partner-img/partner-hover5.png'
import imageHover6 from '../../../assets/img/partner-img/partner-hover6.png'
import imageHover7 from '../../../assets/img/partner-img/partner-hover7.png'

export default defineComponent({
  name: "PartnerTwo",
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
        imageHover: imageHover1,
      },
      {
        id: 2,
        image: image2,
        imageHover: imageHover2,
      },
      {
        id: 3,
        image: image3,
        imageHover: imageHover3,
      },
      {
        id: 4,
        image: image4,
        imageHover: imageHover4,
      },
      {
        id: 5,
        image: image5,
        imageHover: imageHover5,
      },
      {
        id: 6,
        image: image6,
        imageHover: imageHover6,
      },
      {
        id: 7,
        image: image7,
        imageHover: imageHover7,
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