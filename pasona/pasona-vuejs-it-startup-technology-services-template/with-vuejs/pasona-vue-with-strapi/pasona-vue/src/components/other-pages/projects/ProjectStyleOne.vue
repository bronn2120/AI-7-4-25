<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Project</h2>
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

    <!-- Start Works Area -->
    <div class="works-area ptb-80">
      <div class="container">
        <div class="row justify-content-center">
          <div
            class="col-lg-4 col-md-6"
            v-for="project in projects"
            :key="project.id"
          >
            <div class="single-works">
              <img
                :src="project.attributes.image.data.attributes.url"
                alt="image"
              />

              <router-link
                :to="`/project-details/${project.attributes.slug}`"
                class="icon"
              >
                <i class="bx bx-cog"></i>
              </router-link>

              <div class="works-content">
                <h3>
                  <router-link
                    :to="`/project-details/${project.attributes.slug}`"
                  >
                    {{ project.attributes.title }}
                  </router-link>
                </h3>
                <p>{{ project.attributes.description }}</p>
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
    <!-- End Works Area -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProjectStyleOne",
  data() {
    return {
      projects: [],
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/projects?populate=deep"
    );
    this.projects = response.data.data;
  },
};
</script>