<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Pricing</h2>
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

    <!-- Start Pricing Area -->
    <div class="pricing-area ptb-80 bg-f9f6f6">
      <div class="container" v-if="content">
        <div class="section-title">
          <h2>{{ content.heading }}</h2>
          <div class="bar"></div>
          <p>
            {{ content.shortDesc }}
          </p>
        </div>

        <div class="row justify-content-center">
          <div
            class="col-lg-4 col-md-6 col-sm-6"
            v-for="pricing in content.pricingItems"
            :key="pricing.id"
          >
            <div class="pricing-table">
              <div class="pricing-header">
                <h3>{{ pricing.title }}</h3>
              </div>

              <div class="price">
                <span>
                  <sup>$</sup>
                  {{ pricing.price }}
                  <span>/{{ pricing.period }}</span>
                </span>
              </div>

              <div class="pricing-features">
                <ul>
                  <li
                    v-for="feature in pricing.pricingFeature"
                    :key="feature.id"
                    :class="feature.className"
                  >
                    {{ feature.title }}
                  </li>
                </ul>
              </div>

              <div class="pricing-footer">
                <NuxtLink :to="pricing.btnLink" class="btn btn-primary">
                  {{ pricing.btnText }}
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>

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
    <!-- End Pricing Area -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PricingPage",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/pricingplan?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>