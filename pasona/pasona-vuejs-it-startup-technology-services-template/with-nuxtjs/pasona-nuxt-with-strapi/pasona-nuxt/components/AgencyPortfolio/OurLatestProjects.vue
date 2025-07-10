<template>
  <div class="our-latest-projects ptb-80">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-12">
          <div class="section-title text-start">
            <h2>Our Latest <span>Projects</span></h2>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>
        </div>

        <div class="col-lg-6 col-md-12">
          <div class="shorting-menu">
            <button
              class="filter"
              :class="{ active: itemFilterKey == 'all' }"
              v-on:click="itemFilterKey = 'all'"
            >
              All
            </button>
            <button
              class="filter"
              :class="{ active: itemFilterKey == 'design' }"
              v-on:click="itemFilterKey = 'design'"
            >
              Design
            </button>
            <button
              class="filter"
              :class="{ active: itemFilterKey == 'branding' }"
              v-on:click="itemFilterKey = 'branding'"
            >
              Branding
            </button>

            <button
              :class="{ active: itemFilterKey == 'architecture' }"
              v-on:click="itemFilterKey = 'architecture'"
            >
              Architecture
            </button>

            <button
              :class="{ active: itemFilterKey == 'creative' }"
              v-on:click="itemFilterKey = 'creative'"
            >
              Creative
            </button>
          </div>
        </div>
      </div>

      <div class="projects-items">
        <div class="row justify-content-center">
          <div
            v-for="item in itemFilter"
            :key="item.id"
            class="col-lg-4 col-sm-6"
          >
            <div class="single-latest-projects">
              <img :src="item.image" alt="image" />

              <div class="content">
                <span>{{ item.category }}</span>
                <h3>{{ item.title }}</h3>
              </div>
              <a href="#" class="link-btn"></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import image1 from "~/assets/img/agency-portfolio-projects/img1.jpg";
import image2 from "~/assets/img/agency-portfolio-projects/img2.jpg";
import image3 from "~/assets/img/agency-portfolio-projects/img3.jpg";
import image4 from "~/assets/img/agency-portfolio-projects/img4.jpg";
import image5 from "~/assets/img/agency-portfolio-projects/img5.jpg";
import image6 from "~/assets/img/agency-portfolio-projects/img6.jpg";
import image7 from "~/assets/img/agency-portfolio-projects/img7.jpg";
import image8 from "~/assets/img/agency-portfolio-projects/img8.jpg";
import image9 from "~/assets/img/agency-portfolio-projects/img9.jpg";

export default {
  name: "OurLatestProjects",
  data: function () {
    return {
      itemFilterKey: "all",
      items: [
        {
          id: 1,
          image: image1,
          category: "Design",
          title: "Creative Woman",
          key: "architecture",
        },
        {
          id: 2,
          image: image2,
          category: "Camera",
          title: "Worldwide Photography",
          key: "design",
        },
        {
          id: 3,
          image: image3,
          category: "Design",
          title: "Creative Design",
          key: "creative",
        },
        {
          id: 4,
          image: image4,
          category: "Tower",
          title: "Creative Tower",
          key: "design",
        },
        {
          id: 5,
          image: image5,
          category: "Design",
          title: "Creative World",
          key: "design",
        },
        {
          id: 6,
          image: image6,
          category: "Design",
          title: "Creative Style",
          key: "architecture",
        },
        {
          id: 7,
          image: image7,
          category: "Design",
          title: "Creative Woman",
          key: "design",
        },
        {
          id: 8,
          image: image8,
          category: "Design",
          title: "Creative Woman",
          key: "branding",
        },
        {
          id: 9,
          image: image9,
          category: "Design",
          title: "Creative Woman",
          key: "creative",
        },
      ],
    };
  },
  computed: {
    itemFilter() {
      return this[this.itemFilterKey];
    },
    all() {
      return this.items;
    },
    design() {
      return this.items.filter((item) => item.key == "design");
    },
    branding() {
      return this.items.filter((item) => item.key == "branding");
    },
    architecture() {
      return this.items.filter((item) => item.key == "architecture");
    },
    creative() {
      return this.items.filter((item) => item.key == "creative");
    },
  },
};
</script>