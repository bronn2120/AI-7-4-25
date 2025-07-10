module.exports = ({ env }) => ({
  upload: {
    // Update your cloudinary credentials here
    config: {
      provider: "cloudinary",
      providerOptions: {
        cloud_name: "......",
        api_key: "...........",
        api_secret: "..........",
      },
      actionOptions: {
        upload: {},
        delete: {},
      },
    },
  },
  // ...

  "strapi-plugin-populate-deep": {
    config: {
      defaultDepth: 3,
    },
  },
});