<template>
  <div class="blog-area ptb-80">
    <div class="container">
      <div class="section-title" v-if="blog">
        <h2>{{ blog.heading }}</h2>
        <div class="bar"></div>
        <p>
          {{ blog.shortDesc }}
        </p>
      </div>

      <BlogItems></BlogItems>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BlogItems from "./BlogItems.vue";

export default {
  name: "OurBlog",
  components: {
    BlogItems,
  },
  data() {
    return {
      blog: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/ourblog?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.blog = attributes;
  },
};
</script>