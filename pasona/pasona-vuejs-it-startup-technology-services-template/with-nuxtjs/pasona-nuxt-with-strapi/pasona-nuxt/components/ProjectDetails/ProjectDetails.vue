<template>
  <div class="project-details-area ptb-80">
    <div class="container">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-6">
          <div class="project-details-image">
            <img
              :src="details?.attributes?.image?.data?.attributes?.url"
              alt=""
            />
          </div>
        </div>

        <div class="col-lg-12 col-md-12">
          <div class="project-details-desc">
            <h3>{{ details?.attributes?.title }}</h3>

            <span v-html="details?.attributes?.richText"></span>

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
                    <a href="https://facebook.com/" target="_blank">
                      <FacebookIcon></FacebookIcon>
                    </a>
                  </li>
                  <li>
                    <a href="https://twitter.com/" target="_blank">
                      <TwitterIcon></TwitterIcon>
                    </a>
                  </li>
                  <li>
                    <a href="https://linkedin.com/" target="_blank">
                      <LinkedinIcon></LinkedinIcon>
                    </a>
                  </li>
                  <li>
                    <a href="https://instagram.com/" class="instagram">
                      <InstagramIcon></InstagramIcon>
                    </a>
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
</template>

<script lang="ts">
import { defineComponent } from "vue";

interface DetailsType {
  attributes: {
    title: string;
    richText: string;
    image: {
      data: {
        attributes: {
          url: string;
        };
      };
    };
  };
}

export default defineComponent({
  name: "ProjectDetails",
  props: ["projectDetails"],
  data() {
    return {
      details: null as DetailsType | null,
    };
  },
  watch: {
    projectDetails: {
      handler(newVal) {
        this.details = newVal;
      },
      immediate: true,
    },
  },
});
</script>