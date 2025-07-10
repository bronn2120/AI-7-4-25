<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Project Details</h2>
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

    <!-- Start Project Details Area -->
    <div class="project-details-area ptb-80">
      <div class="container">
        <div class="row" v-if="details !== null">
          <div class="col-lg-6 col-md-6 col-sm-6">
            <div class="project-details-image">
              <img
                :src="details[0].attributes.image.data.attributes.url"
                alt="work"
              />
            </div>
          </div>

          <div class="col-lg-12 col-md-12">
            <div class="project-details-desc">
              <h3>{{ details[0].attributes.title }}</h3>

              <span v-html="details[0].attributes.richText"></span>

              <div class="project-details-information">
                <div class="single-info-box">
                  <h4>Happy Client</h4>
                  <p>John Doe</p>
                </div>

                <div class="single-info-box">
                  <h4>Category</h4>
                  <p>Portfolio, Personal</p>
                </div>

                <div class="single-info-box">
                  <h4>Date</h4>
                  <p>February 28, 2019</p>
                </div>

                <div class="single-info-box">
                  <h4>Share</h4>
                  <ul>
                    <li>
                      <a href="#"
                        ><vue-feather type="facebook"></vue-feather
                      ></a>
                    </li>
                    <li>
                      <a href="#"><vue-feather type="twitter"></vue-feather></a>
                    </li>
                    <li>
                      <a href="#"
                        ><vue-feather type="instagram"></vue-feather
                      ></a>
                    </li>
                    <li>
                      <a href="#"
                        ><vue-feather type="linkedin"></vue-feather
                      ></a>
                    </li>
                  </ul>
                </div>

                <div class="single-info-box">
                  <a href="#" class="btn btn-primary">Live Preview</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProjectDetails",
  data() {
    return {
      details: null,
    };
  },
  created: async function () {
    const { slug } = this.$route.params;
    const reaponse = await axios.get(
      `http://localhost:1337/api/projects?filters[slug][$eq]=${slug}&populate=*`,
      { params: { slug } }
    );
    this.details = reaponse.data.data;
  },
};
</script>