<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Team</h2>
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

    <!-- Start Team Area -->
    <div class="team-area ptb-80 bg-f9f6f6">
      <div class="container">
        <div class="row justify-content-center" v-if="content">
          <div
            class="col-lg-4 col-md-6 col-sm-6"
            v-for="team in content.teams"
            :key="team.id"
          >
            <div class="single-team">
              <div class="team-image">
                <img :src="team.image.data.attributes.url" alt="image" />
              </div>

              <div class="team-content">
                <div class="team-info">
                  <h3>{{ team.name }}</h3>
                  <span>{{ team.designation }}</span>
                </div>

                <ul>
                  <li v-for="social in team.socialLink" :key="social.id">
                    <a :href="social.link">
                      <vue-feather :type="social.icon"></vue-feather>
                    </a>
                  </li>
                </ul>

                <p>{{ team.shortDesc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Team Area -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TeamPage",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/ourawesometeam?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>