<template>
  <div class="boxes-area">
    <div class="container">
      <div class="row" v-if="content">
        <div
          class="col-lg-3 col-md-6 col-sm-6"
          v-for="box in content.boxes"
          :key="box.id"
        >
          <div :class="['single-box', box.bgClass]">
            <div class="icon">
              <vue-feather :type="box.icon"></vue-feather>
            </div>
            <h3>{{ box.title }}</h3>
            <p>
              {{ box.shortDesc }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BoxesArea",
  data() {
    return {
      content: null,
    };
  },
  created: async function () {
    const response = await axios.get(
      "http://localhost:1337/api/boxescontent?populate=deep"
    );
    const {
      data: { attributes },
    } = response.data;
    this.content = attributes;
  },
};
</script>