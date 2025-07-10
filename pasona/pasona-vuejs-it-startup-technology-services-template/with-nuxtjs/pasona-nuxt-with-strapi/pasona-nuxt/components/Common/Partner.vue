<template>
  <div class="partner-area partner-section">
    <div class="container" v-if="content">
      <h5>{{ content.title }}</h5>

      <div class="partner-inner">
        <div class="row">
          <div
            class="col-lg-2 col-md-3 col-6 col-sm-4"
            v-for="partner in content.partnerItem"
            :key="partner.id"
          >
            <a href="#">
              <img :src="partner.image.data.attributes.url" alt="partner" />
              <img
                :src="partner.hoverImage.data.attributes.url"
                alt="partner"
              />
            </a>
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
  title: string;
  partnerItem: {
    id: number;
    image: {
      data: {
        attributes: {
          url: string;
        };
      }[];
    };
    hoverImage: {
      data: {
        attributes: {
          url: string;
        };
      }[];
    };
  }[];
}

export default defineComponent({
  name: "Partner",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/partner?populate=deep"
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