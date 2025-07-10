<template>
    <div id="header" :class="['headroom navbar-style-two', {'is-sticky': isSticky}]">
        <div class="startp-nav">
            <div class="container">
                <nav class="navbar navbar-expand-md navbar-light">
                    <router-link class="navbar-brand" to="/">
                        <img src="../../assets/img/logo.png" alt="logo" />
                    </router-link>

                    <div 
                        class="navbar-toggler"
                        @click="active = !active" :aria-pressed="active ? 'true' : 'false'"
                        v-bind:class="{ 'active': button_active_state }"
                        v-on:click="button_active_state = !button_active_state"
                    >
                        <span class="icon-bar top-bar"></span>
                        <span class="icon-bar middle-bar"></span>
                        <span class="icon-bar bottom-bar"></span>
                    </div>

                    <div class="collapse navbar-collapse" :class="{ show: active }">
                        <ul class="navbar-nav nav ml-auto">
                            <li class="nav-item">
                                <a href="#" class="nav-link">
                                    Home <vue-feather type="chevron-down"></vue-feather>
                                </a>

                                <ul class="dropdown_menu">
                                    <li class="nav-item">
                                        <router-link to="/" class="nav-link">IT Startup</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/developer" class="nav-link">Developers</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/web-hosting" class="nav-link">Web Hosting</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/repair-center" class="nav-link">Repair Center</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/iot" class="nav-link">IoT</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/ai-machine-learning" class="nav-link">AI & Machine Learning</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/machine-learning" class="nav-link">Machine Learning</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/digital-agency" class="nav-link">Digital Agency</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/agency-portfolio" class="nav-link">Agency Portfolio</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link to="/bigdata-analytics" class="nav-link">Bigdata Analytics</router-link>
                                    </li>
                                    <li class="nav-item"><a href="#" class="nav-link">Home Static Image<vue-feather type="chevron-down"></vue-feather></a>
                                        <ul class="dropdown_menu">
                                            <li class="nav-item">
                                                <router-link to="/static-image-one" class="nav-link">Static Image 1</router-link>
                                            </li>
                                            
                                            <li class="nav-item">
                                                <router-link to="/static-image-two" class="nav-link">Static Image 2</router-link>
                                            </li>
                                            
                                            <li class="nav-item">
                                                <router-link to="/static-image-three" class="nav-link">Static Image 3</router-link>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>

                            <li class="nav-item"><a href="#" class="nav-link">About <vue-feather type="chevron-down"></vue-feather></a>
                                <ul class="dropdown_menu">
                                    <li class="nav-item">
                                        <router-link to="/about-style-one" class="nav-link">About Style 1</router-link>
                                    </li>
                                    
                                    <li class="nav-item">
                                        <router-link to="/about-style-two" class="nav-link">About Style 2</router-link>
                                    </li>
                                    
                                    <li class="nav-item">
                                        <router-link to="/about-style-three" class="nav-link">About Style 3</router-link>
                                    </li>
                                </ul>
                            </li>

                            <li class="nav-item">
                                <router-link to="/shop" class="nav-link">Shop</router-link>
                            </li>
                            
                            <li class="nav-item">
                                <a href="#" class="nav-link">Pages <vue-feather type="chevron-down"></vue-feather></a>
                                <ul class="dropdown_menu">
                                    <li class="nav-item"><a href="#" class="nav-link">Features <vue-feather type="chevron-down"></vue-feather></a>
                                        <ul class="dropdown_menu">
                                            <li class="nav-item">
                                                <router-link to="/features" class="nav-link">Features</router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link to="/feature-details" class="nav-link">Features Details</router-link>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="nav-item"><a href="#" class="nav-link">Services <vue-feather type="chevron-down"></vue-feather></a>
                                        <ul class="dropdown_menu">
                                            <li class="nav-item">
                                                <router-link to="/service-style-one" class="nav-link">Services Style 1</router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link to="/service-style-two" class="nav-link">Services Style 2</router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link to="/service-style-three" class="nav-link">Services Style 3</router-link>
                                            </li>
                                            
                                            <li class="nav-item">
                                                <router-link to="/service-style-four" class="nav-link">Services Style 4</router-link>
                                            </li>
                                            
                                            <li class="nav-item">
                                                <router-link to="/service-style-five" class="nav-link">Services Style 5</router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link to="/service-details" class="nav-link">Services Details</router-link>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/feedback" class="nav-link">Feedback</router-link>
                                    </li>
                                    
                                    <li class="nav-item"><a href="#" class="nav-link">Project <vue-feather type="chevron-down"></vue-feather></a>
                                        <ul class="dropdown_menu">
                                            <li class="nav-item">
                                                <router-link to="/project-style-one" class="nav-link">Project Style 1</router-link>
                                            </li>

                                            <li class="nav-item">
                                                <router-link to="/project-style-two" class="nav-link">Project Style 2</router-link>
                                            </li>
                                            
                                            <li class="nav-item">
                                                <router-link to="/project-details" class="nav-link">Project Details</router-link>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/team" class="nav-link">Team</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/pricing" class="nav-link">Pricing</router-link>
                                    </li>
                                    
                                    <li class="nav-item">
                                        <router-link to="/faq" class="nav-link">FAQ</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/coming-soon" class="nav-link">Coming Soon</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/not-found" class="nav-link">404 Error</router-link>
                                    </li>
                                </ul>
                            </li>
                            

                            <li class="nav-item"><a href="#" class="nav-link">Blog <vue-feather type="chevron-down"></vue-feather></a>
                                <ul class="dropdown_menu">
                                    <li class="nav-item">
                                        <router-link to="/blog-grid" class="nav-link">Blog Grid</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/blog-right-sidebar" class="nav-link">Blog Right Sidebar</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/blog-grid-two" class="nav-link">Blog Grid 2</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/blog-right-sidebar-two" class="nav-link">Blog Right Sidebar 2</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/blog-grid-three" class="nav-link">Blog Grid 3</router-link>
                                    </li>

                                    <li class="nav-item">
                                        <router-link to="/blog-right-sidebar-three" class="nav-link">Blog Right Sidebar 3</router-link>
                                    </li>
                                    
                                    <li class="nav-item">
                                        <router-link to="/blog-details" class="nav-link">Blog Details</router-link>
                                    </li>
                                </ul>
                            </li>

                            <li class="nav-item">
                                <router-link to="/contact" class="nav-link">Contact</router-link>
                            </li>
                        </ul>
                    </div>

                    <div class="others-option">
                        <router-link to="/cart" class="cart-wrapper-btn">
                            <vue-feather type="shopping-cart"></vue-feather>
                            <span>{{shoppingCart.length}}</span>
                        </router-link>
                        <a href="#" class="btn btn-light">Support</a>
                        <a href="#" class="btn btn-primary">Login</a>
                    </div>
                </nav>
            </div> 
        </div>
    </div>
</template>

<script>
export default {
    name: 'HeaderTwo',
    data(){
        return {
            isSticky: false,
            active: false,
            button_active_state: false,
        }
    },
    mounted() {
        const that = this;
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY;
            // eslint-disable-next-line no-console
            if(scrollPos >= 300){
                that.isSticky = true;
            } else {
                that.isSticky = false;
            }
        })
    },
    computed: {
        shoppingCart(){
            return this.$store.state.cart;
        }
    }
}
</script>