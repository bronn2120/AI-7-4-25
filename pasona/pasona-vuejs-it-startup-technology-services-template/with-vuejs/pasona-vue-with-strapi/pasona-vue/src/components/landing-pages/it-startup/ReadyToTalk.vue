<template>
  <div class="ready-to-talk">
    <div class="container" v-if="content">
      <h3>{{ content.heading }}</h3>
      <p>{{ content.shortDesc }}</p>
      <router-link :to="content.btnLink" class="btn btn-primary">
        {{ content.btnText }}
      </router-link>
      <span>
        <router-link :to="content.btnLink">
          {{ content.ctaText }}
        </router-link>
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ReadyToTalk",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/readytotalk?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>