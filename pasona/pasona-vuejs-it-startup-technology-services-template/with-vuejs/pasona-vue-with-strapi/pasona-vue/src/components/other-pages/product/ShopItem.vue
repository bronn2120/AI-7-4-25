<template>
    <div>
        <div class="single-products">
            <div class="products-image">
                <img :src="item.image" :alt="item.name">

                <!-- <ul>
                    <li><a href="#" data-toggle="modal" data-target="#productsModalCenter"><vue-feather type="search"></vue-feather></a></li>
                    <li><a href="#"><vue-feather type="heart"></vue-feather></a></li>
                    <li><a href="#"><vue-feather type="link"></vue-feather></a></li>
                </ul> -->
            </div>

            <div class="products-content">
                <h3>
                    <router-link to="/details">{{item.name}}</router-link>
                </h3>
                <span>${{item.price}}</span>
                <ul>
                    <li><i class="flaticon-star-1"></i></li>
                    <li><i class="flaticon-star-1"></i></li>
                    <li><i class="flaticon-star-1"></i></li>
                    <li><i class="flaticon-star-1"></i></li>
                    <li><i class="flaticon-star-1"></i></li>
                </ul>
                <a 
                    href="javascript:void(0)" 
                    class="add-to-cart-btn"
                    @click="addToCart(item)"
                >
                    Add to Cart
                </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ShopItem',
    props: ['item'],
    methods: {
        addToCart(item) {
            this.$toast.success('Added to bag', {
                icons: 'shopping_cart',
                theme: "bubble", 
                position: "top-right", 
                timeout : 4000
            });
            if(this.size !== '') {
                this.$store.commit({
                    type: 'addToCart',
                    id: item.id,
                    name: item.name,
                    price: item.price,
                    image: item.image,
                    productQuantity: 1,
                    totalPrice: item.price,
                })
            }
        }
    }
}
</script>