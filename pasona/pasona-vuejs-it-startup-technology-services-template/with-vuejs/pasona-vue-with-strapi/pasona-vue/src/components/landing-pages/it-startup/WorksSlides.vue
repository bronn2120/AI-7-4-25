<template>
  <div class="works-slides">
    <carousel
      :autoplay="5000"
      :settings="settings"
      :wrapAround="true"
      :breakpoints="breakpoints"
      pause-autoplay-on-hover
    >
      <slide v-for="project in projects" :key="project.id">
        <div class="single-works">
          <img
            :src="project.attributes.image.data.attributes.url"
            alt="image"
          />

          <router-link
            :to="`/project-details/${project.attributes.slug}`"
            class="icon"
          >
            <vue-feather type="settings"></vue-feather
          ></router-link>

          <div class="works-content">
            <h3>
              <router-link :to="`/project-details/${project.attributes.slug}`">
                {{ project.attributes.title }}
              </router-link>
            </h3>
            <p>{{ project.attributes.description }}</p>
          </div>
        </div>
      </slide>

      <template #addons> </template>
    </carousel>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "OurWorks",
  components: {
    Carousel,
    Slide,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
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
    projects: [],
  }),

  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/projects?populate=*"
    );
    this.projects = response.data.data;
  },
});
</script>