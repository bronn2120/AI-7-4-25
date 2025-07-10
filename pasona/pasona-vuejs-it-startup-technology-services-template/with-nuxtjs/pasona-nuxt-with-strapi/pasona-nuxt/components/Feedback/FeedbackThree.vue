<template>
  <div class="ml-feedback-area ptb-80">
    <div class="container">
      <div class="section-title">
        <span class="sub-title">Testimonials</span>
        <h2>Our Clients Feedback</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="ml-feedback-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-ml-feedback-item">
              <div class="client-info">
                <img :src="slide.image" alt="image" />
                <h3>{{ slide.name }}</h3>
                <span>{{ slide.position }}</span>
              </div>
              <p>{{ slide.description }}</p>
              <div class="rating">
                <StarIcon></StarIcon>
                <StarIcon></StarIcon>
                <StarIcon></StarIcon>
                <StarIcon></StarIcon>
                <StarIcon></StarIcon>
              </div>
            </div>
          </slide>

          <template #addons>
            <Pagination />
          </template>
        </carousel>
      </div>
    </div>

    <div class="user-shape1">
      <img src="~/assets/img/agency-image/user1.png" alt="image" />
    </div>
    <div class="user-shape2">
      <img src="~/assets/img/agency-image/user2.png" alt="image" />
    </div>
    <div class="user-shape3">
      <img src="~/assets/img/agency-image/user3.png" alt="image" />
    </div>
    <div class="user-shape4">
      <img src="~/assets/img/agency-image/user4.png" alt="image" />
    </div>
    <div class="user-shape5">
      <img src="~/assets/img/agency-image/user5.png" alt="image" />
    </div>
    <div class="user-shape6">
      <img src="~/assets/img/agency-image/user6.png" alt="image" />
    </div>
  </div>
</template>
    
<script>
import { defineComponent } from "vue";
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

import image1 from "~/assets/img/client-image/1.jpg";
import image2 from "~/assets/img/client-image/2.jpg";
import image3 from "~/assets/img/client-image/3.jpg";

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
        image: image1,
        name: "Sarah Taylor",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
      {
        id: 2,
        image: image2,
        name: "Steven Smith",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
      {
        id: 3,
        image: image3,
        name: "James Eva",
        position: "CEO at Envato",
        description:
          "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid ullam harum sit. Accusantium veritatis dolore ducimus illum, cumque excepturi, autem rerum illo amet placeat odit corporis!",
      },
    ],
  }),
});
</script>