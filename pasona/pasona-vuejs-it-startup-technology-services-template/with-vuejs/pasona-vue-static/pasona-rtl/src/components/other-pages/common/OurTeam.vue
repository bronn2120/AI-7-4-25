<template>
  <div class="team-area ptb-80 bg-f9f6f6">
    <div class="container">
      <div class="section-title">
        <h2>Our Awesome Team</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
    </div>

    <div class="team-slides">
      <carousel
        :autoplay="5000"
        :settings="settings"
        :breakpoints="breakpoints"
        pause-autoplay-on-hover
      >
        <slide v-for="slide in carouselItems" :key="slide.id">
          <div class="single-team">
            <div class="team-image">
              <img :src="slide.image" alt="image" />
            </div>

            <div class="team-content">
              <div class="team-info">
                <h3>{{ slide.name }}</h3>
                <span>{{ slide.position }}</span>
              </div>

              <ul>
                <li>
                  <a href="#"><vue-feather type="facebook"></vue-feather></a>
                </li>
                <li>
                  <a href="#"><vue-feather type="twitter"></vue-feather></a>
                </li>
                <li>
                  <a href="#"><vue-feather type="linkedin"></vue-feather></a>
                </li>
                <li>
                  <a href="#"><vue-feather type="gitlab"></vue-feather></a>
                </li>
              </ul>

              <p>{{ slide.desc }}</p>
            </div>
          </div>
        </slide>

        <template #addons>
          <Pagination />
        </template>
      </carousel>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Slide, Pagination } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "OurTeam",
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
        image: require("../../../assets/img/team-image/1.jpg"),
        name: "Josh Buttler",
        position: "CEO & Founder",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 2,
        image: require("../../../assets/img/team-image/2.jpg"),
        name: "Alex Maxwel",
        position: "Marketing Manager",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 3,
        image: require("../../../assets/img/team-image/3.jpg"),
        name: "Janny Cotller",
        position: "Web Developer",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 4,
        image: require("../../../assets/img/team-image/4.jpg"),
        name: "Jason Statham",
        position: "UX/UI Designer",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 5,
        image: require("../../../assets/img/team-image/5.jpg"),
        name: "Corey Anderson",
        position: "Project Manager",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 6,
        image: require("../../../assets/img/team-image/1.jpg"),
        name: "Josh Buttler",
        position: "CEO & Founder",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 7,
        image: require("../../../assets/img/team-image/2.jpg"),
        name: "Alex Maxwel",
        position: "Marketing Manager",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 8,
        image: require("../../../assets/img/team-image/3.jpg"),
        name: "Janny Cotller",
        position: "Web Developer",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 9,
        image: require("../../../assets/img/team-image/4.jpg"),
        name: "Jason Statham",
        position: "UX/UI Designer",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
      {
        id: 10,
        image: require("../../../assets/img/team-image/5.jpg"),
        name: "Corey Anderson",
        position: "Project Manager",
        desc: "Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.",
      },
    ],
    breakpoints: {
      0: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      576: {
        itemsToShow: 2,
        snapAlign: "center",
      },
      768: {
        itemsToShow: 3,
        snapAlign: "center",
      },
      1200: {
        itemsToShow: 5,
        snapAlign: "center",
      },
      1500: {
        itemsToShow: 5,
        snapAlign: "center",
      },
    },
  }),
});
</script>