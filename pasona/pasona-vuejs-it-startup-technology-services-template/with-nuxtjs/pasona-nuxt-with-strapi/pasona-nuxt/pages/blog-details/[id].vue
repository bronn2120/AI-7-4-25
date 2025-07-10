<template>
  <div>
    <CommonPageTitle :pageTitle="details?.attributes?.title" />
    <BlogDetails v-bind:blogDetails="details" />
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

interface Dentist {
  id: number;
  attributes: {
    title: string;
  };
}

export default defineComponent({
  setup() {
    const details = ref<Dentist | null>(null);
    const route = useRoute();

    onMounted(async () => {
      const slug = route.params.id;
      if (slug) {
        try {
          const response = await axios.get(
            `http://localhost:1337/api/blogs/${slug}`
          );

          details.value = response.data.data;
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      } else {
        console.error("Slug parameter is undefined");
      }
    });

    return {
      details,
    };
  },
});
</script>