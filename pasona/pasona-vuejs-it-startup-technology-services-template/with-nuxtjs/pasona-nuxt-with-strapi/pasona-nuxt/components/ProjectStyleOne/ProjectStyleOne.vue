<template>
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

            <NuxtLink
              :to="`/project-details/${project.attributes.slug}`"
              class="icon"
            >
              <i class="bx bx-cog"></i>
            </NuxtLink>

            <div class="works-content">
              <h3>
                <NuxtLink :to="`/project-details/${project.attributes.slug}`">
                  {{ project.attributes.title }}
                </NuxtLink>
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
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape2 rotateme">
      <img src="~/assets/img/shape2.svg" alt="shape" />
    </div>
    <div class="shape7"><img src="~/assets/img/shape4.svg" alt="shape" /></div>
    <div class="shape4"><img src="~/assets/img/shape4.svg" alt="shape" /></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "WorksSlides",
  setup() {
    const projects = ref<
      Array<{
        id: number;
        attributes: any;
        title: string;
        description: string;
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

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/projects?populate=deep"
        );
        const { data } = response.data;

        projects.value = data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      projects,
    };
  },
});
</script>