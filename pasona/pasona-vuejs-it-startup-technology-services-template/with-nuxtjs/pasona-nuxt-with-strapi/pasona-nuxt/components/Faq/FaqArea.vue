<template>
  <div class="faq-area ptb-80">
    <div class="container">
      <div class="faq-accordion">
        <BAccordion>
          <BAccordionItem title="How many time zones are there in all?" visible>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
          <BAccordionItem title="Is Smart Lock required for instant apps?">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
          <BAccordionItem
            title="Can I have multiple activities in a single feature?"
          >
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
          <BAccordionItem title="Can I share resources between features?">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
          <BAccordionItem title="Is multidex supported for instant apps?">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
          <BAccordionItem title="Can I share resources between features?">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
              incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit
              amet, consectetur adipiscing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. incididunt ut labore
              et dolore magna aliqua.
            </p>
          </BAccordionItem>
        </BAccordion>
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
                <input type="email" placeholder="Email" class="form-control" />
              </div>
            </div>

            <div class="col-lg-12 col-md-12">
              <div class="form-group">
                <input type="text" placeholder="Subject" class="form-control" />
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
              <button class="btn btn-primary" type="submit">Submit Now!</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FaqArea",
};
</script>