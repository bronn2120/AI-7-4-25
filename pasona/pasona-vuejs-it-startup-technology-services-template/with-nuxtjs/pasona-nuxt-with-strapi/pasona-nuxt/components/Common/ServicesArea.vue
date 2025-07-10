<template>
  <div class="services-area ptb-80">
    <div class="container">
      <div
        class="row h-100 justify-content-center align-items-center"
        v-if="development"
      >
        <div class="col-lg-6 col-md-12 services-left-image">
          <img
            src="~/assets/img/services-left-image/big-monitor.png"
            alt="big-monitor"
          />
          <img
            src="~/assets/img/services-left-image/creative.png"
            alt="creative"
          />
          <img
            src="~/assets/img/services-left-image/developer.png"
            alt="developer"
          />
          <img
            src="~/assets/img/services-left-image/flower-top.png"
            alt="flower-top"
          />
          <img
            src="~/assets/img/services-left-image/small-monitor.png"
            alt="small-monitor"
          />
          <img
            src="~/assets/img/services-left-image/small-top.png"
            alt="small-top"
          />
          <img src="~/assets/img/services-left-image/table.png" alt="table" />
          <img src="~/assets/img/services-left-image/target.png" alt="target" />
          <img
            src="~/assets/img/services-left-image/cercle-shape.png"
            class="bg-image rotateme"
            alt="shape"
          />

          <img :src="development.image.data.attributes.url" alt="main-pic" />
        </div>

        <div class="col-lg-6 col-md-12 services-content">
          <div class="section-title">
            <h2>{{ development.heading }}</h2>
            <div class="bar"></div>
            <p>
              {{ development.description }}
            </p>
          </div>

          <div class="row">
            <div
              class="col-lg-6 col-md-6 col-sm-6"
              v-for="service in development.services"
              :key="service.id"
            >
              <div class="box">
                <i :class="service.icon"></i>
                {{ service.title }}
              </div>
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
  name: "ServicesArea",
  setup() {
    const development = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/designdevelopment?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        development.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      development,
    };
  },
});
</script>