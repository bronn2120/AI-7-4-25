<template>
    <footer class="footer-area bg-f7fafd">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <div class="logo">
                            <router-link to="/">
                                <img src="../../assets/img/logo.png" alt="logo" />
                            </router-link>
                        </div>
                        <p>Quis ipsum suspendisse ultrices gravida. Risus commodo viverra maecenas accumsan lacus vel facilisis.</p>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget pl-5">
                        <h3>Company</h3>
                        <ul class="list">
                            <li><a href="#">About Us</a></li>
                            <li><a href="#">Services</a></li>
                            <li><a href="#">Features</a></li>
                            <li><a href="#">Our Pricing</a></li>
                            <li><a href="#">Latest News</a></li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h3>Support</h3>
                        <ul class="list">
                            <li><a href="#">FAQ's</a></li>
                            <li><a href="#">Privacy Policy</a></li>
                            <li><a href="#">Terms & Condition</a></li>
                            <li><a href="#">Community</a></li>
                            <li><a href="#">Contact Us</a></li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="single-footer-widget">
                        <h3>Address</h3>
                        
                        <ul class="footer-contact-info">
                            <li><vue-feather type="map-pin"></vue-feather> 27 Division St, New York, NY 10002, USA</li>
                            <li><vue-feather type="mail"></vue-feather> Email: <a href="#">pasona@gmail.com</a></li>
                            <li><vue-feather type="phone-call"></vue-feather> Phone: <a href="#">+ (321) 984 754</a></li>
                        </ul>
                        <ul class="social-links">
                            <li><a href="#" class="facebook"><vue-feather type="facebook"></vue-feather></a></li>
                            <li><a href="#" class="twitter"><vue-feather type="twitter"></vue-feather></a></li>
                            <li><a href="#" class="instagram"><vue-feather type="instagram"></vue-feather></a></li>
                            <li><a href="#" class="linkedin"><vue-feather type="linkedin"></vue-feather></a></li>
                        </ul>
                    </div>
                </div>

                <div class="col-lg-12 col-md-12">
                    <div class="copyright-area">
                        <p>Copyright &copy; {{currentYear}} Pasona. All Rights Reserved</p>
                    </div>
                </div>
            </div>
        </div>

        <img src="../../assets/img/map.png" class="map" alt="map">
        <div class="shape1"><img src="../../assets/img/shape1.png" alt="shape"></div>
        <div class="shape8 rotateme"><img src="../../assets/img/shape2.svg" alt="shape"></div>

        
        <div 
            @click="scrollToTop()" 
            :class="['back-to-top-btn', {'go-top': isTop}]"
        >
            <vue-feather type="arrow-up"></vue-feather>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'MainFooter',
    data (){
        return {
            isTop: false,
            currentYear: new Date().getFullYear(),
        }
    },
    methods: {
        scrollToTop() {
            window.scrollTo(0, 0);
        },
    },
    mounted(){
        const that = this
        window.addEventListener('scroll', () => {
            let scrollPos = window.scrollY
            if(scrollPos >= 100){
                that.isTop = true
            } else {
                that.isTop = false
            }
        })
    }
}
</script>