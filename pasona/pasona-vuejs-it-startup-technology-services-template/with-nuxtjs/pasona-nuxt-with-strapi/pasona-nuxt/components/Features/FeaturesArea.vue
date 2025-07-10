<template>
  <div class="features-area ptb-80 bg-f9f6f6">
    <div class="container" v-if="content">
      <div class="section-title">
        <h2>{{ content.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ content.shortDesc }}
        </p>
      </div>

      <div class="row">
        <div
          class="col-lg-6 col-md-6 col-sm-6"
          v-for="feature in content.features"
          :key="feature.id"
        >
          <div class="single-features">
            <div :class="['icon', feature.bgClass]">
              <i :class="feature.icon"></i>
            </div>

            <h3>{{ feature.title }}</h3>
            <p>
              {{ feature.description }}
            </p>
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
  features: {
    id: number;
    title: string;
    icon: string;
    description: string;
    bgClass: string;
  }[];
}

export default defineComponent({
  name: "FeaturesArea",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/ourfeature?populate=deep"
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