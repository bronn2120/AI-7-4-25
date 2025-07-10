<template>
  <div class="row justify-content-center">
    <div
      class="col-lg-4 col-md-6"
      v-for="blog in blogs.slice(0, 3)"
      :key="blog.id"
    >
      <div class="single-blog-post">
        <div class="blog-image">
          <router-link :to="`/blog-details/${blog.attributes.slug}`">
            <img :src="blog.attributes.image.data.attributes.url" alt="image" />
          </router-link>

          <div class="date">
            <CalendarIcon></CalendarIcon>
            {{ formatPublishedDate(blog.attributes.publishedAt) }}
          </div>
        </div>

        <div class="blog-post-content">
          <h3>
            <router-link :to="`/blog-details/${blog.attributes.slug}`">
              {{ blog.attributes.title }}
            </router-link>
          </h3>

          <span>
            By:
            <router-link to="/blog-grid">
              {{ blog.attributes.author }}
            </router-link>
          </span>

          <p>
            {{ blog.attributes.description }}
          </p>

          <router-link
            :to="`/blog-details/${blog.attributes.slug}`"
            class="read-more-btn"
          >
            {{ blog.attributes.btnText }}
            <ArrowRightIcon></ArrowRightIcon>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  name: "BlogItems",
  data() {
    return {
      blogs: [],
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/blogs?populate=deep"
    );
    this.blogs = response.data.data;
  },
  methods: {
    formatPublishedDate(dateString) {
      const options = { month: "long", day: "numeric", year: "numeric" };
      const formattedDate = new Date(dateString).toLocaleDateString(
        undefined,
        options
      );
      return formattedDate;
    },
  },
});
</script>