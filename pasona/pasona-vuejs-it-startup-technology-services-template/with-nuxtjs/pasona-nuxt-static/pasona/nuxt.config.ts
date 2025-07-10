// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    pageTransition: {
      name: 'fade',
      mode: 'out-in'
    },
    layoutTransition: {
      name: 'slide',
      mode: 'out-in'
    }
  },
  css: [
    "/assets/css/animate.css",
    'bootstrap/dist/css/bootstrap.min.css',
    "/assets/css/flaticon.css",
    "/assets/css/boxicons.min.css",
    "/assets/css/main.scss",
    "/assets/css/it-startup.scss",
    "/assets/css/developer.scss",
    "/assets/css/web-hosting.scss",
    "/assets/css/iot.scss",
    "/assets/css/machine-learning.scss",
    "/assets/css/digital-agency.scss",
    "/assets/css/agency-portfolio.scss",
    "/assets/css/bigdata-analytics.scss",
    "/assets/css/shop.scss",
    "/assets/css/products-details.scss",
    "/assets/css/cart.scss",
    "/assets/css/checkout.scss",
    "/assets/css/repair-center.scss",
    "/assets/css/features.scss",
    "/assets/css/service-details.scss",
    "/assets/css/feature-details.scss",
    "/assets/css/feedback.scss",
    "/assets/css/projects.scss",
    "/assets/css/project-details.scss",
    "/assets/css/team.scss",
    "/assets/css/coming-soon.scss",
    "/assets/css/blog.scss",
    "/assets/css/blog-details.scss",
    "/assets/css/contact.scss",
    "/assets/css/responsive.scss",
  ],
  modules: [
    '@bootstrap-vue-next/nuxt',
    'nuxt-feather-icons',
    'vue3-carousel-nuxt',
    '@pinia/nuxt',
  ],
  carousel: {
    prefix: 'MyPrefix'
  }
})
