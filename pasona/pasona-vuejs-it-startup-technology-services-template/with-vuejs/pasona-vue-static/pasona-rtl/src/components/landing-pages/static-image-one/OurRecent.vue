<template>
  <div class="works-area ptb-80 bg-f7fafd">
    <div class="container">
      <div class="section-title">
        <h2>Our Recent Works</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </div>

    <div class="works-slides">
      <carousel
        :autoplay="5000"
        :settings="settings"
        :breakpoints="breakpoints"
        pause-autoplay-on-hover
      >
        <slide v-for="slide in carouselItems" :key="slide.id">
          <div class="single-works">
            <img :src="slide.image" alt="image" />

            <a href="#" class="icon"
              ><vue-feather type="settings"></vue-feather
            ></a>

            <div class="works-content">
              <h3>
                <a href="#">{{ slide.title }}</a>
              </h3>
              <p>{{ slide.desc }}</p>
            </div>
          </div>
        </slide>

        <template #addons> </template>
      </carousel>
    </div>

    <div class="shape8 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape7">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape4">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "OurRecent",
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
        image: require("../../../assets/img/works-image/1.jpg"),
        title: "Incredible infrastructure",
        desc: "Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
      },
      {
        id: 2,
        image: require("../../../assets/img/works-image/2.jpg"),
        title: "Incredible infrastructure",
        desc: "Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
      },
      {
        id: 3,
        image: require("../../../assets/img/works-image/3.jpg"),
        title: "Incredible infrastructure",
        desc: "Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
      },
      {
        id: 4,
        image: require("../../../assets/img/works-image/4.jpg"),
        title: "Incredible infrastructure",
        desc: "Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
      },
      {
        id: 5,
        image: require("../../../assets/img/works-image/5.jpg"),
        title: "Incredible infrastructure",
        desc: "Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      768: {
        itemsToShow: 2,
        snapAlign: "center",
      },
      1200: {
        itemsToShow: 3,
        snapAlign: "center",
      },
      1500: {
        itemsToShow: 4,
        snapAlign: "center",
      },
    },
  }),
});
</script>