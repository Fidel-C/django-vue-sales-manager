<script setup lang="ts">
import { ref, onMounted } from 'vue';

const products = ref([]);
const columns = [
  { name: 'name', required: true, label: 'Product Name', align: 'left', field: 'name', sortable: true },
  { name: 'description', required: true, label: 'Description', align: 'left', field: 'description', sortable: true },
  { name: 'sale_price', required: true, label: 'Sale Price', align: 'left', field: 'sale_price', sortable: true },
  { name: 'cost_price', required: true, label: 'Cost Price', align: 'left', field: 'cost_price', sortable: true },
  { name: 'inventory', required: true, label: 'Inventory', align: 'left', field: 'inventory', sortable: true },
];

const viewProduct = (product) => {
  // You can navigate to the detailed view of the selected product, e.g., '/product/:id'.
  // Use Vue Router for this purpose.
};

// Fetch the list of products from your Django backend
onMounted(async () => {
  try {
    // Fetch the list of products and populate the products array.
    // You may need to make an API call to your Django backend for this.
  } catch (error) {
    console.error('Failed to fetch products:', error);
  }
});
</script>


<template>
  <q-page>
    <q-page-container>
      <q-card>
        <q-card-section>
          <h2 class="q-mb-md">List of Products</h2>
          <q-table
            :rows="products"
            row-key="id"
            :columns="columns"
            :rows-per-page-options="[5, 10, 20]"
          >
            <template v-slot:body-cell-actions="props">
              <q-td :props="props">
                <q-btn
                  label="View"
                  color="primary"
                  @click="viewProduct(props.row)"
                />
              </q-td>
            </template>
          </q-table>
        </q-card-section>
      </q-card>
    </q-page-container>
  </q-page>
</template>
