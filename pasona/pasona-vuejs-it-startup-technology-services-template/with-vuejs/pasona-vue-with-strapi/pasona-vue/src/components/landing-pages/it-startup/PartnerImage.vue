<template>
  <div class="partner-area partner-section">
    <div class="container" v-if="content">
      <h5>{{ content.title }}</h5>

      <div class="partner-inner">
        <div class="row">
          <div
            class="col-lg-2 col-md-3 col-6 col-sm-4"
            v-for="partner in content.partnerItem"
            :key="partner.id"
          >
            <a href="#">
              <img :src="partner.image.data.attributes.url" alt="partner" />
              <img
                :src="partner.hoverImage.data.attributes.url"
                alt="partner"
              />
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PartnerImage",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/partner?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>