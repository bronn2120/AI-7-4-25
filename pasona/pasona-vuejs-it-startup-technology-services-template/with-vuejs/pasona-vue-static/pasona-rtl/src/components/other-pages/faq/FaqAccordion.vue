<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>FAQ</h2>
          </div>
        </div>
      </div>

      <div class="shape1">
        <img src="../../../assets/img/shape1.png" alt="shape" />
      </div>
      <div class="shape2 rotateme">
        <img src="../../../assets/img/shape2.svg" alt="shape" />
      </div>
      <div class="shape3">
        <img src="../../../assets/img/shape3.svg" alt="shape" />
      </div>
      <div class="shape4">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape5">
        <img src="../../../assets/img/shape5.png" alt="shape" />
      </div>
      <div class="shape6 rotateme">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape7">
        <img src="../../../assets/img/shape4.svg" alt="shape" />
      </div>
      <div class="shape8 rotateme">
        <img src="../../../assets/img/shape2.svg" alt="shape" />
      </div>
    </div>
    <!-- End Page Title -->

    <!-- Start FAQ Area -->
    <div class="faq-area ptb-80">
      <div class="container">
        <div class="faq-accordion">
          <AccordionSlot>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  How many time zones are there in all

                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>
                  Given a 24-hour day and 360 degrees of longitude around the
                  Earth
                </p>
              </template>
            </accordion-item>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  How long is a day and year on Venus?
                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>
                  Venus takes 224.7 Earth days to complete one orbit around the
                  Sun.
                </p>
              </template>
            </accordion-item>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  What animal smells like popcorn?
                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>Binturongs smell like popcorn.</p>
              </template>
            </accordion-item>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  How many time zones are there in all

                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>
                  Given a 24-hour day and 360 degrees of longitude around the
                  Earth
                </p>
              </template>
            </accordion-item>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  How long is a day and year on Venus?
                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>
                  Venus takes 224.7 Earth days to complete one orbit around the
                  Sun.
                </p>
              </template>
            </accordion-item>
            <accordion-item>
              <template v-slot:accordion-trigger>
                <button class="accordion-button">
                  What animal smells like popcorn?
                  <div class="button">
                    <i class="bx bx-plus"></i>
                  </div>
                </button>
              </template>
              <template v-slot:accordion-content>
                <p>Binturongs smell like popcorn.</p>
              </template>
            </accordion-item>
          </AccordionSlot>
        </div>

        <div class="faq-contact">
          <h3>Ask Your Question</h3>
          <form>
            <div class="row">
              <div class="col-lg-6 col-md-6">
                <div class="form-group">
                  <input type="text" placeholder="Name" class="form-control" />
                </div>
              </div>

              <div class="col-lg-6 col-md-6">
                <div class="form-group">
                  <input
                    type="email"
                    placeholder="Email"
                    class="form-control"
                  />
                </div>
              </div>

              <div class="col-lg-12 col-md-12">
                <div class="form-group">
                  <input
                    type="text"
                    placeholder="Subject"
                    class="form-control"
                  />
                </div>
              </div>

              <div class="col-lg-12 col-md-12">
                <div class="form-group">
                  <textarea
                    name="message"
                    cols="30"
                    rows="6"
                    placeholder="Message"
                    class="form-control"
                  ></textarea>
                </div>
              </div>

              <div class="col-lg-12 col-md-12">
                <button class="btn btn-primary" type="submit">
                  Submit Now!
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <!-- End FAQ Area -->
  </div>
</template>

<script>
import AccordionSlot from "../common/AccordionSlot";
import AccordionItem from "../common/AccordionItem";

export default {
  name: "FaqAccordion",
  components: {
    AccordionSlot,
    AccordionItem,
  },
};
</script>