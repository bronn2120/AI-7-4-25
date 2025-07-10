<template>
  <div class="boxes-area">
    <div class="container">
      <div class="row" v-if="content">
        <div
          class="col-lg-3 col-md-6 col-sm-6"
          v-for="box in content.boxes"
          :key="box.id"
        >
          <div :class="['single-box', box.bgClass]">
            <div class="icon">
              <i :class="box.icon"></i>
            </div>
            <h3>{{ box.title }}</h3>
            <p>
              {{ box.shortDesc }}
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
  boxes: {
    id: number;
    title: string;
    icon: string;
    shortDesc: string;
    bgClass: string;
  }[];
}

export default defineComponent({
  name: "BoxesArea",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/boxescontent?populate=deep"
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