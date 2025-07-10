<template>
  <div>
    <CommonPageTitle :pageTitle="products.name" />
    <ProductsDetails
      :id="products.id"
      :name="products.name"
      :price="products.price"
      :image="products.image"
    />
  </div>
</template>

<script setup lang="ts">
import data from "~/data";

interface ProductItem {
  id: string;
  name: string;
  price: number;
  oldPrice: number;
  image: string;
}

const route = useRoute();
const id = route.params.id as string;

const itemsList = data as unknown as ProductItem[];
const products = itemsList.find((item) => item.id === id);

defineProps(["products"]);

function defineProps(arg0: string[]) {
  throw new Error("Function not implemented.");
}
</script>