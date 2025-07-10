import type { Schema, Attribute } from '@strapi/strapi';

export interface AboutInnersAboutInner extends Schema.Component {
  collectionName: 'components_about_inners_about_inners';
  info: {
    displayName: 'about-inner';
    icon: 'arrowRight';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    desc: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Lorem ipsum dolor sit amet, con se ctetur adipiscing elit. In sagittis eg esta ante, sed viverra nunc tinci dunt nec elei fend et tiram.'>;
  };
}

export interface AccordionItemsAccordionItem extends Schema.Component {
  collectionName: 'components_accordion_items_accordion_items';
  info: {
    displayName: 'accordion-item';
    icon: 'arrowRight';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    description: Attribute.Text &
      Attribute.Required &
      Attribute.DefaultTo<'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. incididunt ut labore et dolore magna aliqua.'>;
  };
}

export interface BoxItemsBoxItem extends Schema.Component {
  collectionName: 'components_box_items_box_items';
  info: {
    displayName: 'box-item';
    icon: 'arrowRight';
    description: '';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    shortDesc: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Lorem ipsum dolor sit amet elit, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna.'>;
    icon: Attribute.String & Attribute.Required;
    bgClass: Attribute.String;
  };
}

export interface FeatureItemsFeatureItem extends Schema.Component {
  collectionName: 'components_feature_items_feature_items';
  info: {
    displayName: 'feature-item';
    icon: 'arrowRight';
    description: '';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    icon: Attribute.String & Attribute.Required;
    description: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Lorem ipsum dolor amet, adipiscing, sed do eiusmod tempor incididunt ut labore dolore magna aliqua.'>;
    bgClass: Attribute.String;
  };
}

export interface FeedbackItemsFeedbackItem extends Schema.Component {
  collectionName: 'components_feedback_items_feedback_items';
  info: {
    displayName: 'feedback-item';
    icon: 'arrowRight';
  };
  attributes: {
    image: Attribute.Media & Attribute.Required;
    name: Attribute.String & Attribute.Required;
    designation: Attribute.String & Attribute.Required;
    description: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'>;
  };
}

export interface FooterListsFooterList extends Schema.Component {
  collectionName: 'components_footer_lists_footer_lists';
  info: {
    displayName: 'footer-list';
    icon: 'arrowRight';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    link: Attribute.String & Attribute.Required;
  };
}

export interface FunfactsItemsFunfactsItem extends Schema.Component {
  collectionName: 'components_funfacts_items_funfacts_items';
  info: {
    displayName: 'funfacts-item';
    icon: 'arrowRight';
  };
  attributes: {
    number: Attribute.String & Attribute.Required;
    title: Attribute.String & Attribute.Required;
  };
}

export interface PartnerItemsPartnerItem extends Schema.Component {
  collectionName: 'components_partner_items_partner_items';
  info: {
    displayName: 'partner-item';
    icon: 'arrowRight';
  };
  attributes: {
    image: Attribute.Media & Attribute.Required;
    hoverImage: Attribute.Media & Attribute.Required;
  };
}

export interface PricingFeaturesPricingFeature extends Schema.Component {
  collectionName: 'components_pricing_features_pricing_features';
  info: {
    displayName: 'pricing-feature';
    icon: 'arrowRight';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    className: Attribute.String;
  };
}

export interface PricingItemsPricingItem extends Schema.Component {
  collectionName: 'components_pricing_items_pricing_items';
  info: {
    displayName: 'pricing-item';
    icon: 'arrowRight';
    description: '';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    price: Attribute.String & Attribute.Required;
    period: Attribute.String & Attribute.Required & Attribute.DefaultTo<'Mon'>;
    pricingFeature: Attribute.Component<
      'pricing-features.pricing-feature',
      true
    > &
      Attribute.Required;
    btnText: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Select Plan'>;
    btnLink: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'/contact'>;
  };
}

export interface ServicesListsServicesList extends Schema.Component {
  collectionName: 'components_services_lists_services_lists';
  info: {
    displayName: 'services-list';
    icon: 'arrowRight';
  };
  attributes: {
    title: Attribute.String & Attribute.Required;
    icon: Attribute.String & Attribute.Required;
  };
}

export interface SocialLinksSocialLink extends Schema.Component {
  collectionName: 'components_social_links_social_links';
  info: {
    displayName: 'social-link';
    icon: 'arrowRight';
  };
  attributes: {
    link: Attribute.String & Attribute.Required;
    icon: Attribute.String & Attribute.Required;
  };
}

export interface TeamItemsTeamItem extends Schema.Component {
  collectionName: 'components_team_items_team_items';
  info: {
    displayName: 'team-item';
    icon: 'arrowRight';
    description: '';
  };
  attributes: {
    image: Attribute.Media & Attribute.Required;
    name: Attribute.String & Attribute.Required;
    designation: Attribute.String & Attribute.Required;
    socialLink: Attribute.Component<'social-links.social-link', true> &
      Attribute.Required;
    shortDesc: Attribute.String &
      Attribute.Required &
      Attribute.DefaultTo<'Risus commodo viverra maecenas accumsan lacus vel facilisis quis ipsum.'>;
  };
}

declare module '@strapi/types' {
  export module Shared {
    export interface Components {
      'about-inners.about-inner': AboutInnersAboutInner;
      'accordion-items.accordion-item': AccordionItemsAccordionItem;
      'box-items.box-item': BoxItemsBoxItem;
      'feature-items.feature-item': FeatureItemsFeatureItem;
      'feedback-items.feedback-item': FeedbackItemsFeedbackItem;
      'footer-lists.footer-list': FooterListsFooterList;
      'funfacts-items.funfacts-item': FunfactsItemsFunfactsItem;
      'partner-items.partner-item': PartnerItemsPartnerItem;
      'pricing-features.pricing-feature': PricingFeaturesPricingFeature;
      'pricing-items.pricing-item': PricingItemsPricingItem;
      'services-lists.services-list': ServicesListsServicesList;
      'social-links.social-link': SocialLinksSocialLink;
      'team-items.team-item': TeamItemsTeamItem;
    }
  }
}
