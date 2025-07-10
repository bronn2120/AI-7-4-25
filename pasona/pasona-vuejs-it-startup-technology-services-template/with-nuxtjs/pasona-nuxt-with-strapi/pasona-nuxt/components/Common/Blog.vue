<template>
  <div class="blog-area ptb-80">
    <div class="container">
      <div class="section-title" v-if="blog">
        <h2>{{ blog.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ blog.shortDesc }}
        </p>
      </div>

      <CommonBlogItems />
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
  name: "Blog",
  setup() {
    const blog = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/ourblog?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        blog.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      blog,
    };
  },
});
</script>