<template>
  <div class="main-banner">
    <div class="d-table">
      <div class="d-table-cell">
        <div class="container">
          <div
            class="row h-100 justify-content-center align-items-center"
            v-if="banner"
          >
            <div class="col-lg-5">
              <div class="hero-content">
                <h1>{{ banner.heading }}</h1>
                <p>
                  {{ banner.description }}
                </p>

                <NuxtLink :to="banner.btnLink" class="btn btn-primary">
                  {{ banner.btnText }}
                </NuxtLink>
              </div>
            </div>

            <div class="col-lg-6 offset-lg-1">
              <div class="banner-image">
                <img src="~/assets/img/banner-image/man.png" alt="man" />
                <img src="~/assets/img/banner-image/code.png" alt="code" />
                <img src="~/assets/img/banner-image/carpet.png" alt="carpet" />
                <img src="~/assets/img/banner-image/bin.png" alt="bin" />
                <img src="~/assets/img/banner-image/book.png" alt="book" />
                <img
                  src="~/assets/img/banner-image/dekstop.png"
                  alt="dekstop"
                />
                <img src="~/assets/img/banner-image/dot.png" alt="dot" />
                <img
                  src="~/assets/img/banner-image/flower-top-big.png"
                  alt="flower-top-big"
                />
                <img
                  src="~/assets/img/banner-image/flower-top.png"
                  alt="flower-top"
                />
                <img
                  src="~/assets/img/banner-image/keyboard.png"
                  alt="keyboard"
                />
                <img src="~/assets/img/banner-image/pen.png" alt="pen" />
                <img src="~/assets/img/banner-image/table.png" alt="table" />
                <img
                  src="~/assets/img/banner-image/tea-cup.png"
                  alt="tea-cup"
                />
                <img
                  src="~/assets/img/banner-image/headphone.png"
                  alt="headphone"
                />

                <img :src="banner.image.data.attributes.url" alt="main-pic" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="shape1">
      <img src="~/assets/img/shape1.png" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape3"><img src="~/assets/img/shape3.svg" alt="shape" /></div>
    <div class="shape4"><img src="~/assets/img/shape4.svg" alt="shape" /></div>
    <div class="shape5"><img src="~/assets/img/shape5.png" alt="shape" /></div>
    <div class="shape6 rotateme">
      <img src="~/assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape7">
      <img src="~/assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape8 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
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
  btnText: string;
  btnLink: string;
  image: {
    data: {
      attributes: {
        url: string;
      };
    }[];
  };
}

export default defineComponent({
  name: "MainBanner",
  setup() {
    const banner = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/bannerdefaulthomepage?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        banner.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      banner,
    };
  },
});
</script>