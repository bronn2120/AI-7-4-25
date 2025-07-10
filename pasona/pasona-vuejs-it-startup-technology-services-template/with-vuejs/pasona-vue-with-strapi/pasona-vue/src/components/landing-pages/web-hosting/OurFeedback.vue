<template>
  <div class="feedback-area ptb-80 bg-f7fafd">
    <div class="container">
      <div class="section-title">
        <h2>What users Saying</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="feedback-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="item">
              <div class="single-feedback">
                <div class="client-img">
                  <img :src="slide.image" alt="image" />
                </div>

                <h3>{{ slide.name }}</h3>
                <span>{{ slide.position }}</span>
                <p>{{ slide.description }}</p>
              </div>
            </div>
          </slide>

          <template #addons>
            <navigation>
              <template #next>
                <vue-feather type="arrow-right"></vue-feather>
              </template>
              <template #prev>
                <vue-feather type="arrow-left"></vue-feather>
              </template>
            </navigation>
          </template>
        </carousel>
      </div>
    </div>

    <div class="shape1">
      <img src="../../../assets/img/shape1.png" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape4">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape5">
      <img src="../../../assets/img/shape5.png" alt="shape" />
    </div>
    <div class="shape6 rotateme">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape7">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape8 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide, Navigation } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "OurFeedback",
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
        image: require("../../../assets/img/client-image/1.jpg"),
        name: "John Lucy",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 2,
        image: require("../../../assets/img/client-image/2.jpg"),
        name: "John Smith",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 3,
        image: require("../../../assets/img/client-image/3.jpg"),
        name: "Maxwel Warner",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 4,
        image: require("../../../assets/img/client-image/4.jpg"),
        name: "Ross Taylor",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 5,
        image: require("../../../assets/img/client-image/5.jpg"),
        name: "James Anderson",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
    ],
  }),
});
</script>