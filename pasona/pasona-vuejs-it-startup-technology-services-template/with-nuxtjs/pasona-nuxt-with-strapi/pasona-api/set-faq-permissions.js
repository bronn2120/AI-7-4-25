const Strapi = require('@strapi/strapi');

async function setPermissions() {
  const strapi = await Strapi().load();
  const publicRole = await strapi.query('plugin::users-permissions.role').findOne({ where: { type: 'public' } });
  await strapi.query('plugin::users-permissions.permission').create({
    data: {
      action: 'api::faq.faq.find',
      role: publicRole.id
    }
  });
  await strapi.query('plugin::users-permissions.permission').create({
    data: {
      action: 'api::faq.faq.findOne',
      role: publicRole.id
    }
  });
  console.log('FAQ permissions set for public access');
  process.exit();
}

setPermissions();
