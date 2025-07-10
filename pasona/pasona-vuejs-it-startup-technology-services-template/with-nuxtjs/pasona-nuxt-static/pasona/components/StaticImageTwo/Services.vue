<template>
  <!-- Start Cloud Hosting Services -->
  <div class="services-area ptb-80 bg-f7fafd">
    <div class="container">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-lg-6 col-md-12 services-content">
          <div class="section-title">
            <h2>Cloud Hosting Services</h2>
            <div class="bar"></div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>

          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <DatabaseIcon></DatabaseIcon> Cloud databases
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><GlobeIcon></GlobeIcon> Website hosting</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><FileIcon></FileIcon> File storage</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box">
                <TrendingUpIcon></TrendingUpIcon> Forex trading
              </div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><FolderIcon></FolderIcon> File backups</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><MonitorIcon></MonitorIcon> Remote desktop</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><MailIcon></MailIcon> Email servers</div>
            </div>

            <div class="col-lg-6 col-md-6 col-sm-6">
              <div class="box"><CloudIcon></CloudIcon> Hybrid cloud</div>
            </div>
          </div>
        </div>

        <div class="col-lg-6 col-md-12 services-right-image single-right-image">
          <img
            src="~/assets/img/services-right-image/cercle-shape.png"
            class="bg-image rotateme"
            alt="shape"
          />

          <img
            src="~/assets/img/services-right-image/main-pic.png"
            alt="main-pic"
          />
        </div>
      </div>
    </div>
  </div>
  <!-- End Cloud Hosting Services -->
</template>

<script>
export default {
  name: "Services",
};
</script>