<script setup>
import { ref } from "vue";

const product = ref({
  name: "",
  category: null,
  description: "",
  salePrice: null,
  costPrice: null,
});

const categories = [
  { label: "Category 1", value: "category1" },
  { label: "Category 2", value: "category2" },
  // Add more categories here
];

const submitForm = () => {
  // Handle form submission and add the product to your database
  console.log("Product data:", product.value);
  // You can make an API request to add the product here
  // Reset the form fields if needed
  product.value = {
    name: "",
    category: null,
    description: "",
    salePrice: null,
    costPrice: null,
  };
};
</script>


<template>
<q-card class="col-7" flat>
 <h6 class="text-primary text-center">Add Product</h6>

    
    <q-card-section>
     <q-form @submit="submitForm">
    <q-input
      v-model="product.name"
      label="Product Name"
    ></q-input>
    <q-select
      v-model="product.category"
      :options="categories"
      label="Category"
    ></q-select>
    <q-input
      v-model="product.description"
      label="Description"
    ></q-input>
    <q-input
      v-model="product.salePrice"
      type="number"
      label="Sale Price"
    ></q-input>
    <q-input
      v-model="product.costPrice"
      type="number"
      label="Cost Price"
    ></q-input>
    <q-btn
      type="submit"
      label="Add Product"
    ></q-btn>
  </q-form>
    </q-card-section>
</q-card>
</template>