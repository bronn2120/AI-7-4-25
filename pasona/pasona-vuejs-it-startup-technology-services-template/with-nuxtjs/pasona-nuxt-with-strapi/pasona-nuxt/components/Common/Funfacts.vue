<template>
  <div class="funfacts-area ptb-80">
    <div class="container" v-if="content">
      <div class="section-title">
        <h2>{{ content.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ content.description }}
        </p>
      </div>

      <div class="row">
        <div
          class="col-lg-3 col-md-3 col-6 col-sm-3"
          v-for="funfact in content.funfactItems"
          :key="funfact.id"
        >
          <div class="funfact">
            <h3>
              <span>{{ funfact.number }}</span>
              +
            </h3>
            <p>{{ funfact.title }}</p>
          </div>
        </div>
      </div>

      <div class="contact-cta-box">
        <h3>{{ content.ctaTitle }}</h3>
        <p>{{ content.ctaShortDesc }}</p>
        <NuxtLink :to="content.btnLink" class="btn btn-primary">
          {{ content.btnText }}
        </NuxtLink>
      </div>

      <div class="map-bg">
        <img src="~/assets/img/map.png" alt="map" />
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
  description: string;
  ctaTitle: string;
  ctaShortDesc: string;
  btnText: string;
  btnLink: string;
  funfactItems: {
    id: number;
    number: string;
    title: string;
  }[];
}

export default defineComponent({
  name: "Funfacts",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/funfact?populate=deep"
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