<template>
  <!-- Start Design & Development Services -->
  <div class="services-area ptb-80">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-lg-6 col-md-12 services-left-image single-left-image">
          <img
            src="~/assets/img/services-left-image/cercle-shape.png"
            class="bg-image rotateme"
            alt="shape"
          />

          <img
            src="~/assets/img/services-left-image/main-pic.png"
            alt="main-pic"
          />
        </div>

        <div class="col-lg-6 col-md-12 services-content">
          <div class="section-title">
            <h2>What Our Software Can Do For You</h2>
            <div class="bar"></div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>

          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><LayoutIcon></LayoutIcon> Responsive design</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><CodeIcon></CodeIcon> React web development</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <SmartphoneIcon></SmartphoneIcon> Android apps development
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <CodeIcon></CodeIcon> Laravel web development
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <SmartphoneIcon></SmartphoneIcon> iOS apps development
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><PenToolIcon></PenToolIcon> UX/UI design</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <ShoppingCartIcon></ShoppingCartIcon> E-commerce development
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <CheckCircleIcon></CheckCircleIcon> Print ready design
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Design & Development Services -->
</template>

<script>
export default {
  name: "ServicesArea",
};
</script>