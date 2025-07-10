<template>
  <div class="feedback-area ptb-80">
    <div class="container">
      <div class="section-title">
        <h2>What users Saying</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="testimonials-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-feedback-item">
              <div class="client-info align-items-center">
                <div class="image">
                  <img :src="slide.image" alt="image" />
                </div>

                <div class="title">
                  <h3>{{ slide.name }}</h3>
                  <span>{{ slide.position }}</span>
                </div>
              </div>

              <p>
                {{ slide.description }}
              </p>
            </div>
          </slide>

          <template #addons>
            <Pagination />
          </template>
        </carousel>
      </div>
    </div>

    <div class="shape1"><img src="~/assets/img/shape1.png" alt="shape" /></div>
    <div class="shape2 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape4"><img src="~/assets/img/shape4.svg" alt="shape" /></div>
    <div class="shape5"><img src="~/assets/img/shape5.png" alt="shape" /></div>
    <div class="shape6 rotateme">
      <img src="~/assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape7"><img src="~/assets/img/shape4.svg" alt="shape" /></div>
    <div class="shape8 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
  </div>
</template>
  
  <script lang="ts">
import { defineComponent } from "vue";
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

import image1 from "~/assets/img/client-image/1.jpg";
import image2 from "~/assets/img/client-image/2.jpg";
import image3 from "~/assets/img/client-image/3.jpg";
import image4 from "~/assets/img/client-image/4.jpg";
import image5 from "~/assets/img/client-image/5.jpg";

export default defineComponent({
  name: "Feedback",
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
        name: "John Lucy",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 2,
        image: image2,
        name: "John Smith",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 3,
        image: image3,
        name: "Maxwel Warner",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 4,
        image: image4,
        name: "Ross Taylor",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
      {
        id: 5,
        image: image5,
        name: "James Anderson",
        position: "Web Developer",
        description:
          "Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      },
    ],
  }),
});
</script>