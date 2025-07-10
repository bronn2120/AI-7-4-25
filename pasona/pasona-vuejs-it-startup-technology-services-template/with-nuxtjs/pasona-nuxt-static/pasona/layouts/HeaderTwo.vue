<template>
  <header
    id="header"
    :class="['headroom navbar-style-two', { 'is-sticky': isSticky }]"
  >
    <div class="startp-nav">
      <div class="container">
        <nav class="navbar navbar-expand-md navbar-light">
          <NuxtLink class="navbar-brand" to="/">
            <img src="~/assets/img/logo.png" alt="logo" />
          </NuxtLink>

          <b-navbar-toggle target="navbarSupportedContent"></b-navbar-toggle>

          <b-collapse
            class="collapse navbar-collapse mean-menu"
            id="navbarSupportedContent"
            is-nav
          >
            <ul class="navbar-nav nav ml-auto">
              <li class="nav-item">
                <a href="#" class="nav-link">
                  Home <ChevronDownIcon></ChevronDownIcon>
                </a>

                <ul class="dropdown_menu">
                  <li class="nav-item">
                    <NuxtLink to="/" class="nav-link" exact>
                      IT Startup
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/developer" class="nav-link">
                      Developers
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/web-hosting" class="nav-link">
                      Web Hosting
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/repair-center" class="nav-link">
                      Repair Center
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/iot" class="nav-link">IoT</NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/ai-machine-learning" class="nav-link">
                      AI & Machine Learning
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/machine-learning" class="nav-link">
                      Machine Learning
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/digital-agency" class="nav-link">
                      Digital Agency
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/agency-portfolio" class="nav-link">
                      Agency Portfolio
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <NuxtLink to="/bigdata-analytics" class="nav-link">
                      Bigdata Analytics
                    </NuxtLink>
                  </li>
                  <li class="nav-item">
                    <a href="#" class="nav-link">
                      Home Static Image
                      <ChevronDownIcon></ChevronDownIcon>
                    </a>
                    <ul class="dropdown_menu">
                      <li class="nav-item">
                        <NuxtLink to="/static-image-one" class="nav-link">
                          Static Image 1
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/static-image-two" class="nav-link">
                          Static Image 2
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/static-image-three" class="nav-link">
                          Static Image 3
                        </NuxtLink>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>

              <li class="nav-item">
                <a href="#" class="nav-link">
                  About
                  <ChevronDownIcon></ChevronDownIcon>
                </a>
                <ul class="dropdown_menu">
                  <li class="nav-item">
                    <NuxtLink to="/about-style-one" class="nav-link">
                      About Style 1
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/about-style-two" class="nav-link">
                      About Style 2
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/about-style-three" class="nav-link">
                      About Style 3
                    </NuxtLink>
                  </li>
                </ul>
              </li>

              <li class="nav-item">
                <NuxtLink to="/shop" class="nav-link">Shop</NuxtLink>
              </li>

              <li class="nav-item">
                <a href="#" class="nav-link">
                  Pages
                  <ChevronDownIcon></ChevronDownIcon>
                </a>
                <ul class="dropdown_menu">
                  <li class="nav-item">
                    <a href="#" class="nav-link">
                      Features
                      <ChevronDownIcon></ChevronDownIcon>
                    </a>
                    <ul class="dropdown_menu">
                      <li class="nav-item">
                        <NuxtLink to="/features" class="nav-link">
                          Features
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/feature-details" class="nav-link">
                          Features Details
                        </NuxtLink>
                      </li>
                    </ul>
                  </li>

                  <li class="nav-item">
                    <a href="#" class="nav-link">
                      Services
                      <ChevronDownIcon></ChevronDownIcon>
                    </a>
                    <ul class="dropdown_menu">
                      <li class="nav-item">
                        <NuxtLink to="/service-style-one" class="nav-link">
                          Services Style 1
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/service-style-two" class="nav-link">
                          Services Style 2
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/service-style-three" class="nav-link">
                          Services Style 3
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/service-style-four" class="nav-link">
                          Services Style 4
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/service-style-five" class="nav-link">
                          Services Style 5
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/service-details" class="nav-link">
                          Services Details
                        </NuxtLink>
                      </li>
                    </ul>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/feedback" class="nav-link">
                      Feedback
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <a href="#" class="nav-link">
                      Project
                      <ChevronDownIcon></ChevronDownIcon>
                    </a>
                    <ul class="dropdown_menu">
                      <li class="nav-item">
                        <NuxtLink to="/project-style-one" class="nav-link">
                          Project Style 1
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/project-style-two" class="nav-link">
                          Project Style 2
                        </NuxtLink>
                      </li>

                      <li class="nav-item">
                        <NuxtLink to="/project-details" class="nav-link">
                          Project Details
                        </NuxtLink>
                      </li>
                    </ul>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/team" class="nav-link">Team</NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/pricing" class="nav-link">Pricing</NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/faq" class="nav-link">FAQ</NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/coming-soon" class="nav-link">
                      Coming Soon
                    </NuxtLink>
                  </li>
                </ul>
              </li>

              <li class="nav-item">
                <a href="#" class="nav-link">
                  Blog
                  <ChevronDownIcon></ChevronDownIcon>
                </a>
                <ul class="dropdown_menu">
                  <li class="nav-item">
                    <NuxtLink to="/blog-grid" class="nav-link">
                      Blog Grid
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-right-sidebar" class="nav-link">
                      Blog Right Sidebar
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-grid-two" class="nav-link">
                      Blog Grid 2
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-right-sidebar-two" class="nav-link">
                      Blog Right Sidebar 2
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-grid-three" class="nav-link">
                      Blog Grid 3
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-right-sidebar-three" class="nav-link">
                      Blog Right Sidebar 3
                    </NuxtLink>
                  </li>

                  <li class="nav-item">
                    <NuxtLink to="/blog-details" class="nav-link">
                      Blog Details
                    </NuxtLink>
                  </li>
                </ul>
              </li>

              <li class="nav-item">
                <NuxtLink to="/contact" class="nav-link">Contact</NuxtLink>
              </li>
            </ul>
          </b-collapse>

          <div class="others-option">
            <NuxtLink to="/cart" class="cart-wrapper-btn">
              <ShoppingCartIcon></ShoppingCartIcon>
              <span>{{ cartStore.productsTotal }}</span>
            </NuxtLink>
            <a href="#" class="btn btn-light">Support</a>
            <a href="#" class="btn btn-primary">Login</a>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { useCartStore } from "~/store/cart.js";

export default defineComponent({
  name: "Header",
  setup() {
    const isSticky = ref(false);
    const cartStore = useCartStore();

    onMounted(() => {
      window.addEventListener("scroll", () => {
        let scrollPos = window.scrollY;
        isSticky.value = scrollPos >= 100;
      });
    });

    return {
      isSticky,
      cartStore,
    };
  },
});
</script>