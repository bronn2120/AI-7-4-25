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

    <WorksSlides></WorksSlides>

    <div class="shape8 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="../../../assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape7">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
    <div class="shape4">
      <img src="../../../assets/img/shape4.svg" alt="shape" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";
import WorksSlides from "./WorksSlides.vue";

export default defineComponent({
  name: "OurWorks",
  components: {
    WorksSlides,
  },
  data() {
    return {
      work: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/ourrecentwork?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.work = attributes;
  },
});
</script>