<template>
  <div class="works-area ptb-80 bg-f7fafd">
    <div class="container">
      <div class="section-title" v-if="work">
        <h2>{{ work.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ work.shortDesc }}
        </p>
      </div>
    </div>

    <IndexWorksSlides />

    <div class="shape8 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape7">
      <img src="~/assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape4">
      <img src="~/assets/img/shape4.svg" alt="shape" />
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
}

export default defineComponent({
  name: "BoxesArea",
  setup() {
    const work = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/ourrecentwork?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        work.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      work,
    };
  },
});
</script>