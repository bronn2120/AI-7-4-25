<template>
  <div class="cart-area ptb-80">
    <div class="container">
      <div class="row">
        <div class="col-lg-12 col-md-12">
          <form v-if="cartStore.formattedCart.length">
            <div class="cart-table table-responsive">
              <table class="table table-bordered">
                <thead>
                  <tr>
                    <th scope="col">Product</th>
                    <th scope="col">Name</th>
                    <th scope="col">Unit Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total</th>
                  </tr>
                </thead>

                <tbody>
                  <tr v-for="item in cartStore.formattedCart" :key="item.id">
                    <td class="product-thumbnail">
                      <NuxtLink :to="`/products-details/${item.id}`">
                        <img :src="item.image" :alt="item.name" />
                      </NuxtLink>
                    </td>

                    <td class="product-name">
                      <NuxtLink :to="`/products-details/${item.id}`">
                        {{ item.name }}
                      </NuxtLink>
                    </td>

                    <td class="product-price">
                      <span class="unit-amount">${{ item.price }}</span>
                    </td>

                    <td class="product-quantity">
                      <div class="input-counter">
                        <span
                          @click="cartStore.remove(item.id)"
                          class="minus-btn"
                        >
                          <MinusIcon></MinusIcon>
                        </span>
                        {{ item.quantity }}
                        <span @click="cartStore.add(item.id)" class="plus-btn">
                          <PlusIcon></PlusIcon>
                        </span>
                      </div>
                    </td>

                    <td class="product-subtotal">
                      <span class="subtotal-amount"> ${{ item.cost }} </span>

                      <a
                        href="javascript:void(0)"
                        @click="cartStore.remove(item.id)"
                        class="remove"
                      >
                        <Trash2Icon></Trash2Icon>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="cart-buttons">
              <div class="row align-items-center">
                <div class="col-lg-7 col-md-7 col-sm-7">
                  <div class="continue-shopping-box">
                    <NuxtLink to="/shop-one" class="btn btn-light">
                      Continue Shopping
                    </NuxtLink>
                  </div>
                </div>
              </div>
            </div>

            <div class="cart-totals" v-if="cartStore.total">
              <h3>Cart Totals</h3>

              <ul>
                <li>
                  Subtotal
                  <span>${{ cartStore.total }}</span>
                </li>
                <li>
                  Shipping
                  <span>$2.00</span>
                </li>
                <li>
                  Total
                  <span>
                    <b>${{ cartStore.total }}</b>
                  </span>
                </li>
              </ul>
              <NuxtLink to="/checkout" class="btn btn-primary">
                Proceed to Checkout
              </NuxtLink>
            </div>
          </form>

          <div v-else>
            <button class="btn btn-primary" @click="$router.push('/shop-one')">
              Your cart is empty. Fill it
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCartStore } from "~/store/cart.js";
const cartStore = useCartStore();
</script>