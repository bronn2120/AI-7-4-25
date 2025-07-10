<template>
  <div class="team-area ptb-80 bg-f9f6f6" v-if="content">
    <div class="container">
      <div class="section-title">
        <h2>{{ content.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ content.shortDesc }}
        </p>
      </div>
    </div>

    <div class="team-slides">
      <carousel
        :autoplay="5000"
        :settings="settings"
        :wrapAround="true"
        :breakpoints="breakpoints"
        pause-autoplay-on-hover
      >
        <slide v-for="slide in content.teams" :key="slide.id">
          <div class="single-team">
            <div class="team-image">
              <img :src="slide.image.data.attributes.url" alt="image" />
            </div>

            <div class="team-content">
              <div class="team-info">
                <h3>{{ slide.name }}</h3>
                <span>{{ slide.designation }}</span>
              </div>

              <ul>
                <li v-for="social in slide.socialLink" :key="social.id">
                  <a :href="social.link">
                    <i :class="social.icon"></i>
                  </a>
                </li>
              </ul>

              <p>{{ slide.shortDesc }}</p>
            </div>
          </div>
        </slide>

        <template #addons>
          <Pagination />
        </template>
      </carousel>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

interface Data {
  attributes: any;
  heading: string;
  shortDesc: string;
  teams: {
    id: number;
    name: string;
    designation: string;
    shortDesc: string;
    image: {
      data: {
        attributes: {
          url: string;
        };
      }[];
    };
  }[];
  socialLink: {
    id: number;
    link: string;
    icon: string;
  }[];
}

export default defineComponent({
  name: "OurTeam",
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
        itemsToShow: 3,
        snapAlign: "center",
      },
      1200: {
        itemsToShow: 5,
        snapAlign: "center",
      },
      1500: {
        itemsToShow: 5,
        snapAlign: "center",
      },
    },
  }),
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/ourawesometeam?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        content.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      content,
    };
  },
});
</script>