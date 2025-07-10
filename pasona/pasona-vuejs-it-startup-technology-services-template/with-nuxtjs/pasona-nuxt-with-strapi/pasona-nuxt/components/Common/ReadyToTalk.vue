<template>
  <div class="ready-to-talk">
    <div class="container" v-if="content">
      <h3>{{ content.heading }}</h3>
      <p>{{ content.shortDesc }}</p>
      <NuxtLink :to="content.btnLink" class="btn btn-primary">
        {{ content.btnText }}
      </NuxtLink>
      <span>
        <NuxtLink :to="content.btnLink">
          {{ content.ctaText }}
        </NuxtLink>
      </span>
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
  btnText: string;
  btnLink: string;
  ctaText: string;
}

export default defineComponent({
  name: "ReadyToTalk",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/readytotalk?populate=deep"
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