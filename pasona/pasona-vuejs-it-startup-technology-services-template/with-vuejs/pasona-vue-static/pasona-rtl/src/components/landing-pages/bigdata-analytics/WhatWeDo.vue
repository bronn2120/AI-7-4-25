<template>
    <div class="what-we-do-area ptb-80">
			<div class="container">
				<div class="section-title">
					<h2>What We Do</h2>
					<div class="bar"></div>
					<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
				</div>

				<div class="row">
					<div class="col-lg-4 col-md-6 col-sm-6">
						<div class="single-what-we-do-box">
							<div class="icon">
                                <i class="flaticon-monitor"></i>
                            </div>
                            <h3><router-link to="/service-details">Research</router-link></h3>
                            <p>Lorem ipsum dolor sit consectetur, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            <router-link to="/service-details" class="link">Market Research</router-link>
                            <router-link to="/service-details" class="link">Investment Research</router-link>
                            <router-link to="/service-details" class="read-more-btn">
                                    <vue-feather type="arrow-right"></vue-feather>Read More</router-link>
						</div>
                    </div>
                    
                    <div class="col-lg-4 col-md-6 col-sm-6">
						<div class="single-what-we-do-box">
							<div class="icon">
                                <i class="flaticon-idea"></i>
                            </div>
                            <h3><router-link to="/service-details">Analytics</router-link></h3>
                            <p>Lorem ipsum dolor sit consectetur, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            <router-link to="/service-details" class="link">Data Analytics</router-link>
                            <router-link to="/service-details" class="link">Business Intelligence</router-link>
                            <router-link to="/service-details" class="read-more-btn"><vue-feather type="arrow-right"></vue-feather>Read More</router-link>
						</div>
                    </div>

                    <div class="col-lg-4 col-md-6 col-sm-6 offset-lg-0 offset-md-3 offset-sm-3">
						<div class="single-what-we-do-box">
							<div class="icon">
                                <i class="flaticon-software"></i>
                            </div>
                            <h3><router-link to="/service-details">Technology</router-link></h3>
                            <p>Lorem ipsum dolor sit consectetur, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
                            <router-link to="/service-details" class="link">Intelligence Automation</router-link>
                            <router-link to="/service-details" class="link">Quality Engineering</router-link>
                            <router-link to="/service-details" class="read-more-btn"><vue-feather type="arrow-right"></vue-feather>Read More</router-link>
						</div>
					</div>
				</div>
			</div>
		</div>
</template>

<script>
export default {
    name: 'WhatWeDo'
}
</script>