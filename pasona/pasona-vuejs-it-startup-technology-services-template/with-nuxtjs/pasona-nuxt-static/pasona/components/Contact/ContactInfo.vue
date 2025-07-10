<template>
  <div class="contact-info-area ptb-80">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-6 col-sm-6">
          <div class="contact-info-box">
            <div class="icon">
              <MailIcon></MailIcon>
            </div>
            <h3>Mail Here</h3>
            <p><a href="#">admin@pasona.com</a></p>
            <p><a href="#">info@pasona.com</a></p>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 col-sm-6">
          <div class="contact-info-box">
            <div class="icon">
              <MapPinIcon></MapPinIcon>
            </div>
            <h3>Visit Here</h3>
            <p>27 Division St, New York, NY 10002, United States of America</p>
          </div>
        </div>

        <div
          class="col-lg-4 col-md-6 col-sm-6 offset-lg-0 offset-md-3 offset-sm-3"
        >
          <div class="contact-info-box">
            <div class="icon">
              <PhoneIcon></PhoneIcon>
            </div>
            <h3>Call Here</h3>
            <p><a href="#">+123 456 7890</a></p>
            <p><a href="#">+241 452 4526</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactInfo",
};
</script>