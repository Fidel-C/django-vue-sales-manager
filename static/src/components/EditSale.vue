<script setup lang="ts">
import { ref, onMounted } from 'vue';

const sale = ref({
  store: null,
  total_price: 0,
  total_qty: 0,
});

const storeOptions = ref([]);

const editSale = async () => {
  try {
    // Send a PUT request to your Django backend to update the sale.
    // Make sure to send the updated sale data in the request.
    // After a successful response, you can navigate to another page or show a success message.
  } catch (error) {
    console.error('Failed to edit sale:', error);
  }
};

// Fetch the sale data from your Django backend when the component is mounted
onMounted(async () => {
  try {
    // Fetch the sale data and populate the sale object.
    // You may need to make an API call to your Django backend for this.
  } catch (error) {
    console.error('Failed to fetch sale data:', error);
  }
});
</script>


<template>
  <q-page>
    <q-page-container>
      <q-card>
        <q-card-section>
          <h2 class="q-mb-md">Edit Sale</h2>
          <q-form @submit="editSale">
            <q-select
              v-model="sale.store"
              :options="storeOptions"
              label="Store"
            />
            <q-input v-model="sale.total_price" label="Total Price" type="number" />
            <q-input v-model="sale.total_qty" label="Total Quantity" type="number" />
            <q-btn label="Save Changes" type="submit" color="primary" />
          </q-form>
        </q-card-section>
      </q-card>
    </q-page-container>
  </q-page>
</template>
