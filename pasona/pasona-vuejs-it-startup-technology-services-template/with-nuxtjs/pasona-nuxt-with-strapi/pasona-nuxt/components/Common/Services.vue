<template>
  <div class="services-area ptb-80 bg-f7fafd">
    <div class="container">
      <div
        class="row h-100 justify-content-center align-items-center"
        v-if="cloudhosting"
      >
        <div class="col-lg-6 col-md-12 services-content">
          <div class="section-title">
            <h2>{{ cloudhosting.heading }}</h2>
            <div class="bar"></div>
            <p>
              {{ cloudhosting.description }}
            </p>
          </div>

          <div class="row">
            <div
              class="col-lg-6 col-md-6 col-sm-6"
              v-for="service in cloudhosting.services"
              :key="service.id"
            >
              <div class="box">
                <i :class="service.icon"></i>
                {{ service.title }}
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-12 services-right-image">
          <img
            src="~/assets/img/services-right-image/book-self.png"
            alt="book-self"
          />
          <img src="~/assets/img/services-right-image/box.png" alt="box" />
          <img src="~/assets/img/services-right-image/chair.png" alt="chair" />
          <img src="~/assets/img/services-right-image/cloud.png" alt="cloud" />
          <img src="~/assets/img/services-right-image/cup.png" alt="cup" />
          <img
            src="~/assets/img/services-right-image/flower-top.png"
            alt="flower"
          />
          <img
            src="~/assets/img/services-right-image/head-phone.png"
            alt="head-phone"
          />
          <img
            src="~/assets/img/services-right-image/monitor.png"
            alt="monitor"
          />
          <img src="~/assets/img/services-right-image/mug.png" alt="mug" />
          <img src="~/assets/img/services-right-image/table.png" alt="table" />
          <img
            src="~/assets/img/services-right-image/tissue.png"
            alt="tissue"
          />
          <img
            src="~/assets/img/services-right-image/water-bottle.png"
            alt="water-bottle"
          />
          <img src="~/assets/img/services-right-image/wifi.png" alt="wifi" />
          <img
            src="~/assets/img/services-right-image/cercle-shape.png"
            class="bg-image rotateme"
            alt="shape"
          />

          <img :src="cloudhosting.image.data.attributes.url" alt="main-pic" />
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
  description: string;
  services: {
    id: number;
    title: string;
    icon: string;
  }[];
  image: {
    data: {
      attributes: {
        url: string;
      };
    }[];
  };
}

export default defineComponent({
  name: "Services",
  setup() {
    const cloudhosting = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/cloudhostingservice?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        cloudhosting.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      cloudhosting,
    };
  },
});
</script>