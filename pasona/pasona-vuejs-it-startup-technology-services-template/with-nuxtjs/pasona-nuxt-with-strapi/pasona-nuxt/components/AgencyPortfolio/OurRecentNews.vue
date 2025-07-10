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
          :wrap-around="true"
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

          <template #addons>
            <Pagination />
          </template>
        </carousel>
      </div>
    </div>
  </div>
</template>
  
<script>
import { defineComponent } from "vue";
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

import image1 from "~/assets/img/blog-image/1.jpg";
import image2 from "~/assets/img/blog-image/2.jpg";
import image3 from "~/assets/img/blog-image/3.jpg";
import image4 from "~/assets/img/blog-image/4.jpg";

export default defineComponent({
  name: "OurRecentNews",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data: () => ({
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    carouselItems: [
      {
        id: 1,
        image: image1,
        date: "20 February 2022",
        title: "The security risks of changing package owners",
      },
      {
        id: 2,
        image: image2,
        date: "21 February 2022",
        title: "Tips to Protecting Your Business and Family",
      },
      {
        id: 3,
        image: image3,
        date: "22 February 2022",
        title: "Protect Your Workplace from Cyber Attacks",
      },
      {
        id: 4,
        image: image4,
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
        snapAlign: "left",
      },
      992: {
        itemsToShow: 3,
        snapAlign: "center",
      },
    },
  }),
});
</script>