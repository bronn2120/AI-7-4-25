<template>
  <div class="boxes-area">
    <div class="container">
      <div class="boxes-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :breakpoints="breakpoints"
          :wrapAround="true"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div :class="slide.class">
              <div class="icon">
                <DeveloperFeatherIcon :name="slide.icon"></DeveloperFeatherIcon>
              </div>
              <h3>{{ slide.title }}</h3>
              <p>{{ slide.desc }}</p>
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

export default defineComponent({
  name: "BoxesArea",
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
        class: "single-box",
        icon: "airplay",
        title: "Fully Customizable",
        desc: "Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.",
      },
      {
        id: 2,
        class: "single-box bg-f78acb",
        icon: "pen-tool",
        title: "Professional Tools",
        desc: "Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.",
      },
      {
        id: 3,
        class: "single-box bg-c679e3",
        icon: "pie-chart",
        title: "Marketing",
        desc: "Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.",
      },
      {
        id: 4,
        class: "single-box bg-eb6b3d",
        icon: "server",
        title: "Easy To Use",
        desc: "Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.",
      },
      {
        id: 5,
        class: "single-box bg-eb6b3d",
        icon: "target",
        title: "App Integration",
        desc: "Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.",
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
        itemsToShow: 2,
        snapAlign: "left",
      },
      992: {
        itemsToShow: 4,
        snapAlign: "left",
      },
    },
  }),
});
</script>