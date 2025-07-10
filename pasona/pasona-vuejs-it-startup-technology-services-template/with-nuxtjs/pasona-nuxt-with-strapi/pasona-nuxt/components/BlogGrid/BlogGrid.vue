<template>
  <div class="blog-area ptb-80">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6" v-for="blog in blogs" :key="blog.id">
          <div class="single-blog-post">
            <div class="blog-image">
              <NuxtLink :to="`/blog-details/${blog.attributes.slug}`">
                <img
                  :src="blog.attributes.image.data.attributes.url"
                  alt="image"
                />
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

        <div class="col-lg-12 col-md-12">
          <div class="pagination-area">
            <nav aria-label="Page navigation">
              <ul class="pagination justify-content-center">
                <li class="page-item">
                  <a class="page-link" href="#">Prev</a>
                </li>
                <li class="page-item active">
                  <a class="page-link" href="#">1</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                  <a class="page-link" href="#">Next</a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "BlogGrid",
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