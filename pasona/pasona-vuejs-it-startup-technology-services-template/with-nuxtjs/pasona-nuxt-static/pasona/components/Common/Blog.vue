<template>
  <div class="blog-area ptb-80">
    <div class="container">
      <div class="section-title">
        <h2>The News from Our Blog</h2>
        <div class="bar"></div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>

      <div class="row">
        <div class="col-lg-4 col-md-6">
          <div class="single-blog-post">
            <div class="blog-image">
              <NuxtLink to="/blog-details">
                <img src="~/assets/img/blog-image/1.jpg" alt="image" />
              </NuxtLink>

              <div class="date">
                <CalendarIcon></CalendarIcon> March 15, 2019
              </div>
            </div>

            <div class="blog-post-content">
              <h3>
                <NuxtLink to="/blog-details">
                  The security risks of changing package owners
                </NuxtLink>
              </h3>

              <span>
                By:
                <NuxtLink to="/blog-grid">Admin</NuxtLink>
              </span>

              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse ultrices gravida.
              </p>

              <NuxtLink to="/blog-details" class="read-more-btn">
                Read More <ArrowRightIcon></ArrowRightIcon>
              </NuxtLink>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6">
          <div class="single-blog-post">
            <div class="blog-image">
              <NuxtLink to="/blog-details">
                <img src="~/assets/img/blog-image/2.jpg" alt="image" />
              </NuxtLink>

              <div class="date">
                <CalendarIcon></CalendarIcon> March 17, 2019
              </div>
            </div>

            <div class="blog-post-content">
              <h3>
                <NuxtLink to="/blog-details">
                  Tips to Protecting Your Business and Family
                </NuxtLink>
              </h3>

              <span>
                By:
                <NuxtLink to="/blog-grid">smith</NuxtLink>
              </span>

              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse ultrices gravida.
              </p>

              <NuxtLink to="/blog-details" class="read-more-btn">
                Read More
                <ArrowRightIcon></ArrowRightIcon>
              </NuxtLink>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 offset-lg-0 offset-md-3">
          <div class="single-blog-post">
            <div class="blog-image">
              <NuxtLink to="/blog-details">
                <img src="~/assets/img/blog-image/3.jpg" alt="image" />
              </NuxtLink>

              <div class="date">
                <CalendarIcon></CalendarIcon> March 19, 2019
              </div>
            </div>

            <div class="blog-post-content">
              <h3>
                <NuxtLink to="/blog-details">
                  Protect Your Workplace from Cyber Attacks
                </NuxtLink>
              </h3>

              <span>
                By:
                <NuxtLink to="/blog-grid">John</NuxtLink>
              </span>

              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis
                ipsum suspendisse ultrices gravida.
              </p>

              <NuxtLink to="/blog-details" class="read-more-btn">
                Read More <ArrowRightIcon></ArrowRightIcon>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Blog",
};
</script>