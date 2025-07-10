<template>
  <div class="shop-details-area ptb-80">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-5">
          <div class="products-details-image">
            <img :src="image" alt="img" />
          </div>
        </div>

        <div class="col-lg-7">
          <div class="products-details">
            <h3>{{ name }}</h3>

            <div class="price">${{ price }}</div>
            <ul class="rating">
              <li><i class="flaticon-star-1"></i></li>
              <li><i class="flaticon-star-1"></i></li>
              <li><i class="flaticon-star-1"></i></li>
              <li><i class="flaticon-star-1"></i></li>
              <li><i class="flaticon-star-1"></i></li>
            </ul>

            <p>
              There are many variations of passages of Lorem Ipsum available,
              but the majority have suffered alteration in some form, by
              injected humour, or randomised words which don't look even
              slightly believable.
            </p>

            <div class="availability">Availability: <span>In Stock</span></div>

            <form>
              <div class="quantity align-items-center">
                <span>Quantity:</span>
                <div class="input-counter">
                  <span @click="cartStore.remove(id)" class="minus-btn">
                    <MinusIcon></MinusIcon>
                  </span>
                  {{ itemNumber }}
                  <span @click="cartStore.add(id)" class="plus-btn">
                    <PlusIcon></PlusIcon>
                  </span>
                </div>
              </div>

              <button
                type="button"
                class="default-btn"
                @click="cartStore.add(id)"
              >
                Add to Cart
              </button>
              <a href="#" class="add-to-wishlist-btn" title="Add to Wishlist">
                <HeartIcon></HeartIcon>
              </a>

              <div class="buy-btn">
                <a href="#" class="btn btn-primary">Buy it Now</a>
              </div>
            </form>

            <div class="custom-payment-options">
              <span>Guaranteed safe checkout:</span>

              <div class="payment-methods">
                <img src="~/assets/img/payment-image/1.svg" alt="image" />
                <img src="~/assets/img/payment-image/2.svg" alt="image" />
                <img src="~/assets/img/payment-image/3.svg" alt="image" />
                <img src="~/assets/img/payment-image/4.svg" alt="image" />
                <img src="~/assets/img/payment-image/5.svg" alt="image" />
                <img src="~/assets/img/payment-image/6.svg" alt="image" />
                <img src="~/assets/img/payment-image/7.svg" alt="image" />
              </div>
            </div>

            <div class="products-share-social">
              <span>Share:</span>

              <ul>
                <li>
                  <a href="https://facebook.com/" target="_blank">
                    <FacebookIcon></FacebookIcon>
                  </a>
                </li>
                <li>
                  <a href="https://twitter.com/" target="_blank">
                    <TwitterIcon></TwitterIcon>
                  </a>
                </li>
                <li>
                  <a href="https://linkedin.com/" target="_blank">
                    <LinkedinIcon></LinkedinIcon>
                  </a>
                </li>
                <li>
                  <a href="https://instagram.com/" class="instagram">
                    <InstagramIcon></InstagramIcon>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-12 col-md-12">
          <div class="products-details-tabs">
            <b-tabs content-class="mt-3">
              <b-tab title="Description">
                <div class="content">
                  <div class="products-description">
                    <p>
                      Lorem Ipsum is simply dummy text of the printing and
                      typesetting industry. Lorem Ipsum has been the industry’s
                      standard dummy text ever since the 1500s, when an unknown
                      printer took a galley of type and scrambled it to make a
                      type specimen book. It has survived not only five
                      centuries, but also the leap into electronic typesetting,
                      remaining essentially unchanged. Lorem Ipsum is simply
                      dummy text of the printing.
                    </p>
                  </div>
                </div>
              </b-tab>

              <b-tab title="Additional Information">
                <div class="content">
                  <div class="products-description">
                    <ul class="additional-information">
                      <li><span>Brand</span> ThemeForest</li>
                      <li><span>Color</span> Brown</li>
                      <li><span>Size</span> Large, Medium</li>
                      <li><span>Weight</span> 27 kg</li>
                      <li><span>Dimensions</span> 16 x 22 x 123 cm</li>
                    </ul>
                  </div>
                </div>
              </b-tab>

              <b-tab title="Additional Information">
                <div class="content">
                  <div class="products-reviews">
                    <h3>Customer Reviews</h3>
                    <p>There are no reviews yet.</p>

                    <form class="review-form">
                      <p>Rate this item</p>

                      <div class="star-source">
                        <svg>
                          <linearGradient
                            x1="50%"
                            y1="5.41294643%"
                            x2="87.5527344%"
                            y2="65.4921875%"
                            id="grad"
                          >
                            <stop stop-color="#f2b01e" offset="0%"></stop>
                            <stop stop-color="#f2b01e" offset="60%"></stop>
                            <stop stop-color="#f2b01e" offset="100%"></stop>
                          </linearGradient>
                          <symbol id="star" viewBox="153 89 106 108">
                            <polygon
                              id="star-shape"
                              stroke="url(#grad)"
                              stroke-width="5"
                              fill="currentColor"
                              points="206 162.5 176.610737 185.45085 189.356511 150.407797 158.447174 129.54915 195.713758 130.842203 206 95 216.286242 130.842203 253.552826 129.54915 222.643489 150.407797 235.389263 185.45085"
                            ></polygon>
                          </symbol>
                        </svg>
                      </div>

                      <div class="star-rating">
                        <input type="radio" name="star" id="five" />
                        <label for="five">
                          <svg class="star">
                            <use xlink:href="#star" />
                          </svg>
                        </label>

                        <input type="radio" name="star" id="four" />
                        <label for="four">
                          <svg class="star">
                            <use xlink:href="#star" />
                          </svg>
                        </label>

                        <input type="radio" name="star" id="three" />
                        <label for="three">
                          <svg class="star">
                            <use xlink:href="#star" />
                          </svg>
                        </label>

                        <input type="radio" name="star" id="two" />
                        <label for="two">
                          <svg class="star">
                            <use xlink:href="#star" />
                          </svg>
                        </label>

                        <input type="radio" name="star" id="one" />
                        <label for="one">
                          <svg class="star">
                            <use xlink:href="#star" />
                          </svg>
                        </label>
                      </div>

                      <div class="row">
                        <div class="col-lg-12">
                          <div class="form-group">
                            <textarea
                              name="review-message"
                              id="message"
                              cols="30"
                              rows="4"
                              placeholder="Write your review*"
                              class="form-control"
                            ></textarea>
                          </div>
                        </div>

                        <div class="col-lg-6 col-md-6">
                          <div class="form-group">
                            <input
                              type="text"
                              placeholder="Name*"
                              class="form-control"
                            />
                          </div>
                        </div>

                        <div class="col-lg-6 col-md-6">
                          <div class="form-group">
                            <input
                              type="email"
                              placeholder="Email*"
                              class="form-control"
                            />
                          </div>
                        </div>

                        <div class="col-lg-12 col-md-12">
                          <button type="submit" class="btn btn-primary">
                            Submit
                          </button>
                        </div>
                      </div>
                    </form>
                  </div>
                </div>
              </b-tab>
            </b-tabs>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useCartStore } from "~/store/cart.js";

export default defineComponent({
  props: ["id", "name", "price", "image"],
  data() {
    return {
      itemNumber: 1,
    };
  },
  setup() {
    const cartStore = useCartStore();

    return {
      cartStore,
    };
  },
});
</script>