<template>
  <div class="row justify-content-center">
    <div
      class="col-lg-4 col-md-6"
      v-for="blog in blogs.slice(0, 3)"
      :key="blog.id"
    >
      <div class="single-blog-post">
        <div class="blog-image">
          <NuxtLink :to="`/blog-details/${blog.attributes.slug}`">
            <img :src="blog.attributes.image.data.attributes.url" alt="image" />
          </NuxtLink>

          <div class="date">
            <CalendarIcon></CalendarIcon>
            {{ formatPublishedDate(blog.attributes.publishedAt) }}
          </div>
        </div>

        <div class="blog-post-content">
          <h3>
            <NuxtLink :to="`/blog-details/${blog.attributes.slug}`">
              {{ blog.attributes.title }}
            </NuxtLink>
          </h3>

          <span>
            By:
            <NuxtLink to="/blog-grid">
              {{ blog.attributes.author }}
            </NuxtLink>
          </span>

          <p>
            {{ blog.attributes.description }}
          </p>

          <NuxtLink
            :to="`/blog-details/${blog.attributes.slug}`"
            class="read-more-btn"
          >
            {{ blog.attributes.btnText }}
            <ArrowRightIcon></ArrowRightIcon>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "BlogItems",
  setup() {
    const blogs = ref<
      Array<{
        id: number;
        attributes: any;
        title: string;
        author: string;
        description: string;
        btnText: string;
        slug: string;
        image: {
          data: {
            attributes: {
              url: string;
            };
          }[];
        };
      }>
    >([]);

    const formatPublishedDate = (dateString: string) => {
      const options = { month: "long", day: "numeric", year: "numeric" };
      const formattedDate = new Date(dateString).toLocaleDateString(
        undefined,
        options as Intl.DateTimeFormatOptions
      );
      return formattedDate;
    };

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/blogs?populate=deep"
        );
        const { data } = response.data;

        blogs.value = data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      blogs,
      formatPublishedDate,
    };
  },
});
</script>