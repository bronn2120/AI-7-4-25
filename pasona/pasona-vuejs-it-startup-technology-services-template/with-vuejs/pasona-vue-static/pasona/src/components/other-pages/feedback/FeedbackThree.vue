<template>
  <div class="ml-feedback-area ptb-80">
    <div class="container">
      <div class="section-title">
        <h2>Our Clients Feedback</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="ml-feedback-slides">
        <carousel :autoplay="5000" :settings="settings" pause-autoplay-on-hover>
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-ml-feedback-item">
              <div class="client-info">
                <img :src="slide.image" alt="image" />
                <h3>{{ slide.name }}</h3>
                <span>{{ slide.position }}</span>
              </div>
              <p>{{ slide.description }}</p>
              <div class="rating">
                <vue-feather type="star"></vue-feather>
                <vue-feather type="star"></vue-feather>
                <vue-feather type="star"></vue-feather>
                <vue-feather type="star"></vue-feather>
                <vue-feather type="star"></vue-feather>
              </div>
            </div>
          </slide>

          <template #addons>
            <Pagination />
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
    <div class="shape3">
      <img src="../../../assets/img/shape3.svg" alt="shape" />
    </div>
    <div class="shape4">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
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
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "FeedbackThree",
  components: {
    Carousel,
    Slide,
    Pagination,
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
        name: "Sarah Taylor",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
      {
        id: 2,
        image: require("../../../assets/img/client-image/2.jpg"),
        name: "Steven Smith",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
      {
        id: 3,
        image: require("../../../assets/img/client-image/3.jpg"),
        name: "James Eva",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
    ],
  }),
});
</script>