<template>
  <div class="feedback-area ptb-80 bg-f7fafd">
    <div class="container" v-if="content">
      <div class="section-title">
        <h2>{{ content.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ content.shortDesc }}
        </p>
      </div>

      <div class="feedback-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :wrapAround="true"
          pause-autoplay-on-hover
        >
          <slide v-for="feedback in content.feedbackItems" :key="feedback.id">
            <div class="item">
              <div class="single-feedback">
                <div class="client-img">
                  <img :src="feedback.image.data.attributes.url" alt="image" />
                </div>

                <h3>{{ feedback.name }}</h3>
                <span>{{ feedback.designation }}</span>
                <p>{{ feedback.description }}</p>
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
import axios from "axios";
import { Carousel, Slide, Navigation } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "ClientsFeedback",
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
    content: null,
  }),
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/whatuserssaying?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
});
</script>