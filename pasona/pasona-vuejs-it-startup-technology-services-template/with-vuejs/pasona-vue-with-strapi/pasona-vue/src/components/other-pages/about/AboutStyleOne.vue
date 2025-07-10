<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>About Us</h2>
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

    <!-- Start About Area -->
    <div class="about-area ptb-80">
      <div class="container" v-if="about">
        <div class="row align-items-center">
          <div class="col-lg-6 col-md-12">
            <div class="about-image">
              <img :src="about.image.data.attributes.url" alt="image" />
            </div>
          </div>

          <div class="col-lg-6 col-md-12">
            <div class="about-content">
              <div class="section-title">
                <h2>{{ about.heading }}</h2>
                <div class="bar"></div>
                <p>
                  {{ about.shortDesc }}
                </p>
              </div>

              <p>
                {{ about.description }}
              </p>

              <p>
                {{ about.descriptionTwo }}
              </p>
            </div>
          </div>
        </div>

        <div class="about-inner-area">
          <div class="row justify-content-center">
            <div
              class="col-lg-4 col-md-6 col-sm-6"
              v-for="abouts in about.aboutInner"
              :key="abouts.id"
            >
              <div class="about-text">
                <h3>{{ abouts.title }}</h3>
                <p>
                  {{ abouts.desc }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End About Area -->

    <OurTeam></OurTeam>
    <ReadyToTalk></ReadyToTalk>
    <PartnerImage></PartnerImage>
    <FunFacts></FunFacts>
  </div>
</template>

<script>
import OurTeam from "../common/OurTeam";
import PartnerImage from "../common/PartnerImage";
import ReadyToTalk from "../common/ReadyToTalk";
import FunFacts from "../common/FunFacts";
import axios from "axios";

export default {
  name: "AboutStyleOne",
  components: {
    OurTeam,
    PartnerImage,
    ReadyToTalk,
    FunFacts,
  },
  data() {
    return {
      about: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/aboutus?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.about = attributes;
  },
};
</script>