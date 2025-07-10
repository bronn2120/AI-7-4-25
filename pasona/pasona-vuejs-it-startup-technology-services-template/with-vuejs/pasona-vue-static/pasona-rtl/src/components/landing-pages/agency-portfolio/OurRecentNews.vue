<template>
  <div class="blog-area ptb-80">
    <div class="container">
      <div class="section-title style-two">
        <h2>Our Recent <span>News</span></h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="blog-slides">
        <carousel
          :autoplay="5000"
          :settings="settings"
          :breakpoints="breakpoints"
          pause-autoplay-on-hover
        >
          <slide v-for="slide in carouselItems" :key="slide.id">
            <div class="single-blog-item">
              <div class="post-image">
                <a href="#">
                  <img :src="slide.image" alt="image" />
                </a>
              </div>

              <div class="post-content">
                <ul class="post-meta">
                  <li>By <a href="#">Admin</a></li>
                  <li>{{ slide.date }}</li>
                </ul>
                <h3>
                  <a href="#">{{ slide.title }}</a>
                </h3>
              </div>
            </div>
          </slide>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "OurRecentNews",
  components: {
    Carousel,
    Slide,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    carouselItems: [
      {
        id: 1,
        image: require("../../../assets/img/blog-image/1.jpg"),
        date: "20 February 2022",
        title: "The security risks of changing package owners",
      },
      {
        id: 2,
        image: require("../../../assets/img/blog-image/2.jpg"),
        date: "21 February 2022",
        title: "Tips to Protecting Your Business and Family",
      },
      {
        id: 3,
        image: require("../../../assets/img/blog-image/3.jpg"),
        date: "22 February 2022",
        title: "Protect Your Workplace from Cyber Attacks",
      },
      {
        id: 4,
        image: require("../../../assets/img/blog-image/4.jpg"),
        date: "23 February 2022",
        title: "Four New WordPress.com Color Schemes",
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      768: {
        itemsToShow: 2,
        snapAlign: "center",
      },
      992: {
        itemsToShow: 3,
        snapAlign: "center",
      },
    },
  }),
});
</script>