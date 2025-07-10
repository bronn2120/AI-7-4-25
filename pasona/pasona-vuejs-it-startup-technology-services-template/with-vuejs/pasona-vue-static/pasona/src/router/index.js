import { createWebHistory, createRouter } from "vue-router";

// All Pages
import ITStartup from "../components/landing-pages/ITStartup";
import DeveloperPage from "../components/landing-pages/DeveloperPage";
import WebHosting from "../components/landing-pages/WebHosting";
import RepairCenter from "../components/landing-pages/RepairCenter";
import IotPage from "../components/landing-pages/IotPage";
import AiMachineLearning from "../components/landing-pages/AiMachineLearning";
import MachineLearning from "../components/landing-pages/MachineLearning";
import DigitalAgency from "../components/landing-pages/DigitalAgency";
import AgencyPortfolio from "../components/landing-pages/AgencyPortfolio";
import BigdataAnalytics from "../components/landing-pages/BigdataAnalytics";
import StaticImageOne from "../components/landing-pages/StaticImageOne";
import StaticImageTwo from "../components/landing-pages/StaticImageTwo";
import StaticImageThree from "../components/landing-pages/StaticImageThree";
import AboutStyleOne from "../components/other-pages/about/AboutStyleOne";
import AboutStyleTwo from "../components/other-pages/about/AboutStyleTwo";
import AboutStyleThree from "../components/other-pages/about/AboutStyleThree";
import FeaturesPage from "../components/other-pages/features/FeaturesPage";
import FeatureDetails from "../components/other-pages/features/FeatureDetails";
import ServicesOne from "../components/other-pages/services/ServicesOne";
import ServicesTwo from "../components/other-pages/services/ServicesTwo";
import ServicesThree from "../components/other-pages/services/ServicesThree";
import ServicesFour from "../components/other-pages/services/ServicesFour";
import ServicesFive from "../components/other-pages/services/ServicesFive";
import ServiceDetails from "../components/other-pages/services/ServiceDetails";
import FeedbackPage from "../components/other-pages/feedback/FeedbackPage";
import ProjectStyleOne from "../components/other-pages/projects/ProjectStyleOne";
import ProjectStyleTwo from "../components/other-pages/projects/ProjectStyleTwo";
import ProjectDetails from "../components/other-pages/projects/ProjectDetails";
import TeamPage from "../components/other-pages/team/TeamPage";
import PricingPage from "../components/other-pages/pricing/PricingPage";
import FaqAccordion from "../components/other-pages/faq/FaqAccordion";
import NotFound from "../components/other-pages/not-found/NotFound";
import ComingSoon from "../components/other-pages/coming-soon/ComingSoon";
import BlogGrid from "../components/other-pages/blog/BlogGrid";
import BlogRightSidebar from "../components/other-pages/blog/BlogRightSidebar";
import BlogGridTwo from "../components/other-pages/blog/BlogGridTwo";
import BlogRightSidebarTwo from "../components/other-pages/blog/BlogRightSidebarTwo";
import BlogGridThree from "../components/other-pages/blog/BlogGridThree";
import BlogRightSidebarThree from "../components/other-pages/blog/BlogRightSidebarThree";
import BlogDetails from "../components/other-pages/blog/BlogDetails";
import ContactPage from "../components/other-pages/contact/ContactPage";
import ShopPage from "../components/other-pages/product/ShopPage";
import CartPage from "../components/other-pages/product/CartPage";
import CheckoutPage from "../components/other-pages/product/CheckoutPage";
import ItemDetails from "../components/other-pages/product/ItemDetails";

const routes = [
  { path: "/", component: ITStartup },
  { path: "/developer", component: DeveloperPage },
  { path: "/web-hosting", component: WebHosting },
  { path: "/repair-center", component: RepairCenter },
  { path: "/iot", component: IotPage },
  { path: "/ai-machine-learning", component: AiMachineLearning },
  { path: "/machine-learning", component: MachineLearning },
  { path: "/digital-agency", component: DigitalAgency },
  { path: "/agency-portfolio", component: AgencyPortfolio },
  { path: "/bigdata-analytics", component: BigdataAnalytics },
  { path: "/static-image-one", component: StaticImageOne },
  { path: "/static-image-two", component: StaticImageTwo },
  { path: "/static-image-three", component: StaticImageThree },
  { path: "/about-style-one", component: AboutStyleOne },
  { path: "/about-style-two", component: AboutStyleTwo },
  { path: "/about-style-three", component: AboutStyleThree },
  { path: "/features", component: FeaturesPage },
  { path: "/feature-details", component: FeatureDetails },
  { path: "/service-style-one", component: ServicesOne },
  { path: "/service-style-two", component: ServicesTwo },
  { path: "/service-style-three", component: ServicesThree },
  { path: "/service-style-four", component: ServicesFour },
  { path: "/service-style-five", component: ServicesFive },
  { path: "/service-details", component: ServiceDetails },
  { path: "/feedback", component: FeedbackPage },
  { path: "/project-style-one", component: ProjectStyleOne },
  { path: "/project-style-two", component: ProjectStyleTwo },
  { path: "/project-details", component: ProjectDetails },
  { path: "/team", component: TeamPage },
  { path: "/pricing", component: PricingPage },
  { path: "/faq", component: FaqAccordion },
  { path: "/coming-soon", component: ComingSoon },
  { path: "/not-found", component: NotFound },
  { path: "/blog-grid", component: BlogGrid },
  { path: "/blog-right-sidebar", component: BlogRightSidebar },
  { path: "/blog-grid-two", component: BlogGridTwo },
  { path: "/blog-right-sidebar-two", component: BlogRightSidebarTwo },
  { path: "/blog-grid-three", component: BlogGridThree },
  { path: "/blog-right-sidebar-three", component: BlogRightSidebarThree },
  { path: "/blog-details", component: BlogDetails },
  { path: "/contact", component: ContactPage },
  { path: "/shop", component: ShopPage },
  { path: "/cart", component: CartPage },
  { path: "/checkout", component: CheckoutPage },
  { path: "/details", component: ItemDetails },
];

const router = createRouter({
  history: createWebHistory("/pasona/"),
  base: process.env.NODE_ENV === "production" ? "/pasona/" : "/",
  linkExactActiveClass: "active",
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

export default router;
