<template>
  <div class="features-area ptb-80 bg-f7fafd">
    <div class="container" v-if="content">
      <div class="section-title">
        <h2>{{ content.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ content.shortDesc }}
        </p>
      </div>

      <div class="row">
        <div
          class="col-lg-6 col-md-6 col-sm-6"
          v-for="feature in content.features"
          :key="feature.id"
        >
          <div class="single-features">
            <div :class="['icon', feature.bgClass]">
              <vue-feather :type="feature.icon"></vue-feather>
            </div>

            <h3>{{ feature.title }}</h3>
            <p>
              {{ feature.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OurFeatures",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/ourfeature?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>