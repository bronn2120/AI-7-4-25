<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Features</h2>
          </div>
        </div>
      </div>

      <div class="shape1">
        <img src="../../../assets/img/shape1.png" alt="shape" />
      </div>
      <div class="shape2 rotateme">
        <img src="../../../assets/img/shape2.svg" alt="shape" />
      </div>
      <div class="shape3">
        <img src="../../../assets/img/shape3.svg" alt="shape" />
      </div>
      <div class="shape4">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape5">
        <img src="../../../assets/img/shape5.png" alt="shape" />
      </div>
      <div class="shape6 rotateme">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape7">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape8 rotateme">
        <img src="../../../assets/img/shape2.svg" alt="shape" />
      </div>
    </div>
    <!-- End Page Title -->

    <!-- Start Features Area -->
    <div class="features-area ptb-80 bg-f9f6f6">
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
    <!-- End Features Area -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FeaturesPage",
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