<template>
    <div class="industries-serve-area ptb-80">
        <div class="container">
            <div class="section-title">
                <h2>Industries We Serve</h2>
                <div class="bar"></div>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>

            <div class="row">
                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-buildings'></i>
                        </div>
                        Manufacturing
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-building-house'></i>
                        </div>
                        Healthcare
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-car'></i>
                        </div>
                        Automobile
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-credit-card'></i>
                        </div>
                        Banking
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-building'></i>
                        </div>
                        Real Estate
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bxs-plane-alt'></i>
                        </div>
                        Logistics
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-group'></i>
                        </div>
                        Insurance
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>

                <div class="col-lg-3 col-6 col-sm-6 col-md-4">
                    <div class="single-industries-serve-box">
                        <div class="icon">
                            <i class='bx bx-bitcoin'></i>
                        </div>
                        Capital Markets
                        <NuxtLink to="/service-details" class="link-btn"></NuxtLink>
                    </div>
                </div>
            </div>
        </div>

        <div class="analytics-shape2"><img src="~/assets/img/bigdata-analytics/vector.png" alt="image"></div>
    </div>
</template>

<script>
export default {
    name: 'Industries'
}
</script>