<template>
  <div>
    <!-- Start Page Title -->
    <div class="page-title-area">
      <div class="d-table">
        <div class="d-table-cell">
          <div class="container">
            <h2>Checkout</h2>
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

    <!-- Start Checkout Area -->
    <div class="checkout-area ptb-80">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12">
            <div class="user-actions">
              <vue-feather type="edit"></vue-feather>
              <span
                >Returning customer? <a href="#">Click here to login</a></span
              >
            </div>
          </div>
        </div>

        <form>
          <div class="row">
            <OrderForm></OrderForm>

            <YourOrders></YourOrders>
          </div>
        </form>
      </div>
    </div>
    <!-- End Checkout Area -->
  </div>
</template>

<script>
import OrderForm from "./OrderForm";
import YourOrders from "./YourOrders";

export default {
  name: "CheckoutPage",
  components: {
    OrderForm,
    YourOrders,
  },
};
</script>