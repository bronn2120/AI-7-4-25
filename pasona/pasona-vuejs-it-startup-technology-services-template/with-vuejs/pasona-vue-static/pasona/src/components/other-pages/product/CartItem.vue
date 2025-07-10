<template>
    <tr>
        <td class="product-thumbnail">
            <a href="#">
                <img :src="item.image" alt="item">
            </a>
        </td>

        <td class="product-name">
            <a href="#">{{item.name}}</a>
        </td>

        <td class="product-price">
            <span class="unit-amount">${{item.price}}</span>
        </td>

        <td class="product-quantity">
            <div class="input-counter">
                {{item.productQuantity}}
            </div>
        </td>

        <td class="product-subtotal">
            <span class="subtotal-amount">${{item.totalPrice}}</span>

            <a href="javascript:void(0)" @click="removeFromCart(item)" class="remove">
                <vue-feather type="trash-2"></vue-feather>
            </a>
        </td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: ['item'],
    methods: {
        removeFromCart(item){
            this.$toast.success('Removed from bag', {
                icons: 'shopping_cart',
                theme: "bubble", 
                position: "top-right", 
                timeout : 4000
            });
            this.$store.commit('removeFromCart', item);
        }
    }
}
</script>