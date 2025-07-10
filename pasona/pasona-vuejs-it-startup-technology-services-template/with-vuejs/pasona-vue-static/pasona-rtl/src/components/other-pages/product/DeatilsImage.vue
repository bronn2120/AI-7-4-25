<template>
  <div>
    <ul class="slickslide">
      <carousel :autoplay="5000" :settings="settings" pause-autoplay-on-hover>
        <slide v-for="slide in carouselItems" :key="slide.id">
          <li>
            <img :src="slide.image" alt="img" />
          </li>
        </slide>
      </carousel>
    </ul>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "DeatilsImage",
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
        image: require("../../../assets/img/shop-image/1.jpg"),
      },
      {
        id: 2,
        image: require("../../../assets/img/shop-image/1.jpg"),
      },
      {
        id: 3,
        image: require("../../../assets/img/shop-image/1.jpg"),
      },
      {
        id: 4,
        image: require("../../../assets/img/shop-image/1.jpg"),
      },
      {
        id: 5,
        image: require("../../../assets/img/shop-image/1.jpg"),
      },
    ],
  }),
});
</script>