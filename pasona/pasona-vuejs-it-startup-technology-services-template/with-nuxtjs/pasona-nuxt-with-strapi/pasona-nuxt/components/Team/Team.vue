<template>
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
                    <i :class="social.icon"></i>
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
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import axios from "axios";

interface Data {
  attributes: any;
  teams: {
    id: number;
    name: string;
    designation: string;
    shortDesc: string;
    image: {
      data: {
        attributes: {
          url: string;
        };
      }[];
    };
  }[];
  socialLink: {
    id: number;
    link: string;
    icon: string;
  }[];
}

export default defineComponent({
  name: "Team",
  setup() {
    const content = ref<Data | null>(null);

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://localhost:1337/api/ourawesometeam?populate=deep"
        );
        const {
          data: { attributes },
        } = response.data;

        content.value = attributes;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    });

    return {
      content,
    };
  },
});
</script>