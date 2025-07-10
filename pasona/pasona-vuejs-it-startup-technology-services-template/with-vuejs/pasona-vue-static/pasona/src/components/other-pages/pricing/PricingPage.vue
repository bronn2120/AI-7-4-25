<template>
    <div>
        <!-- Start Page Title -->
        <div class="page-title-area">
            <div class="d-table">
                <div class="d-table-cell">
                    <div class="container">
                        <h2>Pricing</h2>
                    </div>
                </div>
			</div>
			
			<div class="shape1"><img src="../../../assets/img/shape1.png" alt="shape"></div>
			<div class="shape2 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
			<div class="shape3"><img src="../../../assets/img/shape3.svg" alt="shape"></div>
			<div class="shape4"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
			<div class="shape5"><img src="../../../assets/img/shape5.png" alt="shape"></div>
			<div class="shape6 rotateme"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
			<div class="shape7"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
			<div class="shape8 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
        </div>
        <!-- End Page Title -->

        <!-- Start Pricing Area -->
		<div class="pricing-area ptb-80 bg-f9f6f6">
			<div class="container">
				<div class="section-title">
					<h2>Pricing Plans</h2>
					<div class="bar"></div>
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
				</div>

				<div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="pricing-table">
                            <div class="pricing-header">
                                <h3>Basic Plan</h3>
                            </div>
                            
                            <div class="price">
                                <span><sup>$</sup>15.00 <span>/Mon</span></span>
                            </div>
                            
                            <div class="pricing-features">
                                <ul>
                                    <li class="active">5 GB Bandwidth</li>
                                    <li class="active">Highest Speed</li>
                                    <li class="active">1 GB Storage</li>
                                    <li class="active">Unlimited Website</li>
                                    <li class="active">Unlimited Users</li>
                                    <li class="active">24x7 Great Support</li>
                                    <li>Data Security and Backups</li>
                                    <li>Monthly Reports and Analytics</li>
                                </ul>
                            </div>
                            
                            <div class="pricing-footer">
                                <a href="#" class="btn btn-primary">Select Plan</a>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-4 col-md-6 col-sm-6">
                        <div class="pricing-table active-plan">
                            <div class="pricing-header">
                                <h3>Advanced Plan</h3>
                            </div>
                            
                            <div class="price">
                                <span><sup>$</sup>35.00 <span>/Mon</span></span>
                            </div>
                            
                            <div class="pricing-features">
                                <ul>
                                    <li class="active">10 GB Bandwidth</li>
                                    <li class="active">Highest Speed</li>
                                    <li class="active">3 GB Storage</li>
                                    <li class="active">Unlimited Website</li>
                                    <li class="active">Unlimited Users</li>
                                    <li class="active">24x7 Great Support</li>
                                    <li class="active">Data Security and Backups</li>
                                    <li>Monthly Reports and Analytics</li>
                                </ul>
                            </div>
                            
                            <div class="pricing-footer">
                                <a href="#" class="btn btn-primary">Select Plan</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6 offset-lg-0 offset-md-3 offset-sm-3">
                        <div class="pricing-table">
                            <div class="pricing-header">
                                <h3>Expert Plan</h3>
                            </div>
                            
                            <div class="price">
                                <span><sup>$</sup>65.00 <span>/Mon</span></span>
                            </div>
                            
                            <div class="pricing-features">
                                <ul>
                                    <li class="active">15 GB Bandwidth</li>
                                    <li class="active">Highest Speed</li>
                                    <li class="active">5 GB Storage</li>
                                    <li class="active">Unlimited Website</li>
                                    <li class="active">Unlimited Users</li>
                                    <li class="active">24x7 Great Support</li>
                                    <li class="active">Data Security and Backups</li>
                                    <li class="active">Monthly Reports and Analytics</li>
                                </ul>
                            </div>
                            
                            <div class="pricing-footer">
                                <a href="#" class="btn btn-primary">Select Plan</a>
                            </div>
                        </div>
                    </div>
				</div>
			</div>

			<div class="shape8 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
			<div class="shape2 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
			<div class="shape7"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
			<div class="shape4"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
		</div>
		<!-- End Pricing Area -->

        <!-- Start Pricing Two Area -->
        <div class="pricing-area ptb-80">
            <div class="container">
                <div class="section-title">
                    <h2>Our Pricing Plan</h2>
                    <div class="bar"></div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
                
                <div class="pricing-tab bg-color">
                    <div class="tabs">
                        <ul class="tabs__header">
                            <li 
                                class="tabs__header-item" 
                                v-for="tab in tabs" 
                                v-on:click="selectTab (tab.id)" 
                                v-bind:class="{ 'active': activeTab == tab.id }"
                                :key="tab.id"
                            >
                                {{tab.title}}
                            </li>
                        </ul>
                    </div>
                    <div class="tabs__container">
                        <div 
                            class="tabs__list"
                            ref='tabsList'
                        >
                            <div 
                                class="tabs__list-tab"
                                v-for="tab in tabs"
                                v-bind:class="{ 'active': activeTab == tab.id }"
                                :key="tab.id"
                            >
                                <div class="row justify-content-center">
                                    <div 
                                        class="col-lg-4 col-md-6 col-sm-6"
                                        v-for="pricing in tab.pricingBox"
                                        :key="pricing.id"
                                    >
                                        <div class="pricing-box">
                                            <div class="pricing-header">
                                                <h3>{{pricing.title}}</h3>
                                                <p>{{pricing.desc}}</p>
                                            </div>

                                            <div class="price">
                                                ${{pricing.price}} <span>/{{pricing.period}}</span>
                                            </div>

                                            <div class="buy-btn">
                                                <a href="#" class="btn btn-primary">Get Started Free</a>
                                            </div>

                                            <ul class="pricing-features">
                                                <li
                                                    v-for="features in pricing.featuresList"
                                                    :key="features.id"
                                                >
                                                    <vue-feather type='check'></vue-feather> 
                                                    {{features.list}}
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="shape2 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
            <div class="shape3"><img src="../../../assets/img/shape3.svg" alt="shape"></div>
            <div class="shape4"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
            <div class="shape6 rotateme"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
            <div class="shape7"><img src="../../../assets/img/shape4.svg" alt="shape"></div>
            <div class="shape8 rotateme"><img src="../../../assets/img/shape2.svg" alt="shape"></div>
        </div>
        <!-- End Pricing Two Area -->
    </div>
</template>

<script>
export default {
    name: 'PricingPage',
    data () {
        return {
            activeTab: 1,
            offsetRight: 0,
            tabs: [
                {
                    id: 1,
                    title: 'Monthly Plan',
                    pricingBox: [
                        {
                            id: 1,
                            title: 'Free',
                            desc: 'Get your business up and running',
                            price: '0',
                            period: 'm',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 1000 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                        {
                            id: 2,
                            title: 'Free',
                            desc: 'Get your business up and running',
                            price: '149',
                            period: 'm',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 3300 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                        {
                            id: 3,
                            title: 'Free',
                            desc: 'Get your business up and running',
                            price: '179',
                            period: 'm',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 10000 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                    ],
                },
                {
                    id: 2,
                    title: 'Yearly Plan',
                    pricingBox: [
                        {
                            id: 1,
                            title: 'Free',
                            desc: 'Get your business up and running',
                            price: '0',
                            period: 'y',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 1000 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                        {
                            id: 2,
                            title: 'Pro',
                            desc: 'Get your business up and running',
                            price: '249',
                            period: 'y',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 3300 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                        {
                            id: 3,
                            title: 'Premium',
                            desc: 'Get your business up and running',
                            price: '279 ',
                            period: 'y',
                            featuresList: [
                                {
                                    id: 1,
                                    list: 'Drag & Drop Builder',
                                },
                                {
                                    id: 2,
                                    list: 'Lead Generation & Sales',
                                },
                                {
                                    id: 3,
                                    list: 'Boot & Digital Assistants',
                                },
                                {
                                    id: 4,
                                    list: 'Customer Service',
                                },
                                {
                                    id: 5,
                                    list: 'Up to 10000 Subscribers',
                                },
                                {
                                    id: 6,
                                    list: 'Unlimited Broadcasts',
                                },
                                {
                                    id: 7,
                                    list: 'Landing Pages & Web Widgets',
                                },
                            ],
                        },
                    ],
                },
            ]
        }
    },
    methods: {
        selectTab (id) {
            let tabsList = this.$refs.tabsList
            this.activeTab = id
            this.offsetRight = tabsList.clientWidth * (id - 1)
            tabsList.style.right = this.offsetRight + 'px'
        }
    },
    mounted () {
        let tabsList = this.$refs.tabsList
        tabsList.style.right = this.offsetRight + 'px'
    }
}
</script>