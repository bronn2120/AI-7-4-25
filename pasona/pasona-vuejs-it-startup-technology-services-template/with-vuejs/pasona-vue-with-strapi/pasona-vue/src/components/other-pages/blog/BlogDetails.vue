<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Blog Details</h2>
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

    <!-- Start Blog Details Area -->
    <div class="blog-details-area ptb-80">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-12">
            <div class="blog-details-desc" v-if="details !== null">
              <div class="article-image">
                <img
                  :src="details[0].attributes.image.data.attributes.url"
                  alt="image"
                />
              </div>

              <div class="article-content">
                <div class="entry-meta">
                  <ul>
                    <li>
                      <vue-feather type="clock"></vue-feather>
                      <a href="#">
                        {{
                          formatPublishedDate(details[0].attributes.publishedAt)
                        }}
                      </a>
                    </li>
                    <li>
                      <vue-feather type="user"></vue-feather>
                      <a href="#">
                        {{ details[0].attributes.author }}
                      </a>
                    </li>
                  </ul>
                </div>

                <h3>{{ details[0].attributes.title }}</h3>

                <span v-html="details[0].attributes.richText"></span>
              </div>

              <div class="article-footer">
                <div class="article-tags">
                  <a href="#">Fashion</a>
                  <a href="#">Smart</a>
                  <a href="#">Marketing</a>
                  <a href="#">Games</a>
                  <a href="#">Travel</a>
                </div>
              </div>

              <div class="startp-post-navigation">
                <div class="prev-link-wrapper">
                  <div class="info-prev-link-wrapper">
                    <a href="#">
                      <span class="image-prev">
                        <img
                          src="../../../assets/img/blog-image/2.jpg"
                          alt="image"
                        />
                        <span class="post-nav-title">Prev</span>
                      </span>

                      <span class="prev-link-info-wrapper">
                        <span class="prev-title"
                          >Don't buy a tech gift until you read these
                          rules</span
                        >
                        <span class="meta-wrapper">
                          <span class="date-post">January 21, 2022</span>
                        </span>
                      </span>
                    </a>
                  </div>
                </div>

                <div class="next-link-wrapper">
                  <div class="info-next-link-wrapper">
                    <a href="#">
                      <span class="next-link-info-wrapper">
                        <span class="next-title"
                          >The golden rule of buying a phone as a gift</span
                        >
                        <span class="meta-wrapper">
                          <span class="date-post">January 21, 2022</span>
                        </span>
                      </span>

                      <span class="image-next">
                        <img
                          src="../../../assets/img/blog-image/3.jpg"
                          alt="image"
                        />
                        <span class="post-nav-title">Next</span>
                      </span>
                    </a>
                  </div>
                </div>
              </div>

              <div class="comments-area">
                <h3 class="comments-title">2 Comments:</h3>

                <ol class="comment-list">
                  <li class="comment">
                    <article class="comment-body">
                      <footer class="comment-meta">
                        <div class="comment-author vcard">
                          <img
                            src="../../../assets/img/client-image/1.jpg"
                            class="avatar"
                            alt="image"
                          />
                          <b class="fn">John Jones</b>
                          <span class="says">says:</span>
                        </div>

                        <div class="comment-metadata">
                          <a href="#">
                            <time>April 24, 2019 at 10:59 am</time>
                          </a>
                        </div>
                      </footer>

                      <div class="comment-content">
                        <p>
                          Lorem Ipsum has been the industry’s standard dummy
                          text ever since the 1500s, when an unknown printer
                          took a galley of type and scrambled it to make a type
                          specimen.
                        </p>
                      </div>

                      <div class="reply">
                        <a href="#" class="comment-reply-link">Reply</a>
                      </div>
                    </article>

                    <ol class="children">
                      <li class="comment">
                        <article class="comment-body">
                          <footer class="comment-meta">
                            <div class="comment-author vcard">
                              <img
                                src="../../../assets/img/client-image/2.jpg"
                                class="avatar"
                                alt="image"
                              />
                              <b class="fn">Steven Smith</b>
                              <span class="says">says:</span>
                            </div>

                            <div class="comment-metadata">
                              <a href="#">
                                <time>April 24, 2019 at 10:59 am</time>
                              </a>
                            </div>
                          </footer>

                          <div class="comment-content">
                            <p>
                              Lorem Ipsum has been the industry’s standard dummy
                              text ever since the 1500s, when an unknown printer
                              took a galley of type and scrambled it to make a
                              type specimen.
                            </p>
                          </div>

                          <div class="reply">
                            <a href="#" class="comment-reply-link">Reply</a>
                          </div>
                        </article>
                      </li>

                      <ol class="children">
                        <li class="comment">
                          <article class="comment-body">
                            <footer class="comment-meta">
                              <div class="comment-author vcard">
                                <img
                                  src="../../../assets/img/client-image/3.jpg"
                                  class="avatar"
                                  alt="image"
                                />
                                <b class="fn">Sarah Taylor</b>
                                <span class="says">says:</span>
                              </div>

                              <div class="comment-metadata">
                                <a href="#">
                                  <time>April 24, 2019 at 10:59 am</time>
                                </a>
                              </div>
                            </footer>

                            <div class="comment-content">
                              <p>
                                Lorem Ipsum has been the industry’s standard
                                dummy text ever since the 1500s, when an unknown
                                printer took a galley of type and scrambled it
                                to make a type specimen.
                              </p>
                            </div>

                            <div class="reply">
                              <a href="#" class="comment-reply-link">Reply</a>
                            </div>
                          </article>
                        </li>
                      </ol>
                    </ol>
                  </li>

                  <li class="comment">
                    <article class="comment-body">
                      <footer class="comment-meta">
                        <div class="comment-author vcard">
                          <img
                            src="../../../assets/img/client-image/4.jpg"
                            class="avatar"
                            alt="image"
                          />
                          <b class="fn">John Doe</b>
                          <span class="says">says:</span>
                        </div>

                        <div class="comment-metadata">
                          <a href="#">
                            <time>April 24, 2019 at 10:59 am</time>
                          </a>
                        </div>
                      </footer>

                      <div class="comment-content">
                        <p>
                          Lorem Ipsum has been the industry’s standard dummy
                          text ever since the 1500s, when an unknown printer
                          took a galley of type and scrambled it to make a type
                          specimen.
                        </p>
                      </div>

                      <div class="reply">
                        <a href="#" class="comment-reply-link">Reply</a>
                      </div>
                    </article>

                    <ol class="children">
                      <li class="comment">
                        <article class="comment-body">
                          <footer class="comment-meta">
                            <div class="comment-author vcard">
                              <img
                                src="../../../assets/img/client-image/5.jpg"
                                class="avatar"
                                alt="image"
                              />
                              <b class="fn">James Anderson</b>
                              <span class="says">says:</span>
                            </div>

                            <div class="comment-metadata">
                              <a href="#">
                                <time>April 24, 2019 at 10:59 am</time>
                              </a>
                            </div>
                          </footer>

                          <div class="comment-content">
                            <p>
                              Lorem Ipsum has been the industry’s standard dummy
                              text ever since the 1500s, when an unknown printer
                              took a galley of type and scrambled it to make a
                              type specimen.
                            </p>
                          </div>

                          <div class="reply">
                            <a href="#" class="comment-reply-link">Reply</a>
                          </div>
                        </article>
                      </li>
                    </ol>
                  </li>
                </ol>

                <div class="comment-respond">
                  <h3 class="comment-reply-title">Leave a Reply</h3>

                  <form class="comment-form">
                    <p class="comment-notes">
                      <span id="email-notes"
                        >Your email address will not be published.</span
                      >
                      Required fields are marked
                      <span class="required">*</span>
                    </p>
                    <p class="comment-form-comment">
                      <label>Comment</label>
                      <textarea
                        name="comment"
                        id="comment"
                        cols="45"
                        rows="5"
                        maxlength="65525"
                        required="required"
                      ></textarea>
                    </p>
                    <p class="comment-form-author">
                      <label>Name <span class="required">*</span></label>
                      <input
                        type="text"
                        id="author"
                        name="author"
                        required="required"
                      />
                    </p>
                    <p class="comment-form-email">
                      <label>Email <span class="required">*</span></label>
                      <input
                        type="email"
                        id="email"
                        name="email"
                        required="required"
                      />
                    </p>
                    <p class="comment-form-url">
                      <label>Website</label>
                      <input type="url" id="url" name="url" />
                    </p>
                    <p class="comment-form-cookies-consent">
                      <input
                        type="checkbox"
                        value="yes"
                        name="wp-comment-cookies-consent"
                        id="wp-comment-cookies-consent"
                      />
                      <label for="wp-comment-cookies-consent"
                        >Save my name, email, and website in this browser for
                        the next time I comment.</label
                      >
                    </p>
                    <p class="form-submit">
                      <input
                        type="submit"
                        name="submit"
                        id="submit"
                        class="submit"
                        value="Post Comment"
                      />
                    </p>
                  </form>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 col-md-12">
            <BlogSideber></BlogSideber>
          </div>
        </div>
      </div>
    </div>
    <!-- End Blog Details Area -->
  </div>
</template>

<script>
import BlogSideber from "./BlogSideber.vue";
import axios from "axios";

export default {
  name: "BlogDetails",
  components: {
    BlogSideber,
  },
  data() {
    return {
      details: null,
    };
  },
  created: async function () {
    const { slug } = this.$route.params;
    const reaponse = await axios.get(
      `http://localhost:1337/api/blogs?filters[slug][$eq]=${slug}&populate=*`,
      { params: { slug } }
    );
    this.details = reaponse.data.data;
  },
  methods: {
    formatPublishedDate(dateString) {
      const options = { month: "long", day: "numeric", year: "numeric" };
      const formattedDate = new Date(dateString).toLocaleDateString(
        undefined,
        options
      );
      return formattedDate;
    },
  },
};
</script>