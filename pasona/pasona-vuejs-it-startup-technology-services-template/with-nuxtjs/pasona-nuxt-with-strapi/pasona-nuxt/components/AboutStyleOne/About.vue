<template>
  <div class="about-area ptb-80">
    <div class="container" v-if="about">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-12">
          <div class="about-image">
            <img :src="about.image.data.attributes.url" alt="image" />
          </div>
        </div>

        <div class="col-lg-6 col-md-12">
          <div class="about-content">
            <div class="section-title">
              <h2>{{ about.heading }}</h2>
              <div class="bar"></div>
              <p>
                {{ about.shortDesc }}
              </p>
            </div>

            <p>
              {{ about.description }}
            </p>

            <p>
              {{ about.descriptionTwo }}
            </p>
          </div>
        </div>
      </div>

      <div class="about-inner-area">
        <div class="row justify-content-center">
          <div
            class="col-lg-4 col-md-6 col-sm-6"
            v-for="abouts in about.aboutInner"
            :key="abouts.id"
          >
            <div class="about-text">
              <h3>{{ abouts.title }}</h3>
              <p>
                {{ abouts.desc }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

interface Data {
  attributes: any;
  heading: string;
  shortDesc: string;
  description: string;
  descriptionTwo: string;
  aboutInner: {
    id: number;
    title: string;
    desc: string;
  }[];
}

export default defineComponent({
  name: "About",
  setup() {
    const about = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/aboutus?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        about.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      about,
    };
  },
});
</script>