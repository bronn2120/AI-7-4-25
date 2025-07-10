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

          <NuxtLink
            :to="`/project-details/${project.attributes.slug}`"
            class="icon"
          >
            <i class="bx bx-cog"></i>
          </NuxtLink>

          <div class="works-content">
            <h3>
              <NuxtLink :to="`/project-details/${project.attributes.slug}`">
                {{ project.attributes.title }}
              </NuxtLink>
            </h3>
            <p>{{ project.attributes.description }}</p>
          </div>
        </div>
      </slide>

      <template #addons> </template>
    </carousel>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "WorksSlides",
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
        snapAlign: "left",
      },
      1200: {
        itemsToShow: 3,
        snapAlign: "center",
      },
      1500: {
        itemsToShow: 4,
        snapAlign: "left",
      },
    },
  }),
  setup() {
    const projects = ref<
      Array<{
        id: number;
        attributes: any;
        title: string;
        description: string;
        slug: string;
        image: {
          data: {
            attributes: {
              url: string;
            };
          }[];
        };
      }>
    >([]);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/projects?populate=deep"
        );
        const { data } = response.data;

        projects.value = data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      projects,
    };
  },
});
</script>