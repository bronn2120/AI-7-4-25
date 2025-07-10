<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Blog Grid</h2>
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

    <!-- Start Blog Area -->
    <div class="blog-area ptb-80">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6" v-for="blog in blogs" :key="blog.id">
            <div class="single-blog-post">
              <div class="blog-image">
                <router-link :to="`/blog-details/${blog.attributes.slug}`">
                  <img
                    :src="blog.attributes.image.data.attributes.url"
                    alt="image"
                  />
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
    <!-- End Blog Area -->
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