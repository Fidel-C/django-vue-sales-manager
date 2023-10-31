<script setup lang="ts">
import { ref, onMounted } from 'vue';

const sales = ref([]);
const columns = [
  { name: 'store.name', required: true, label: 'Store Name', align: 'left', field: 'store.name', sortable: true },
  { name: 'total_price', required: true, label: 'Total Price', align: 'left', field: 'total_price', sortable: true },
  { name: 'total_qty', required: true, label: 'Total Quantity', align: 'left', field: 'total_qty', sortable: true },
];

const viewSale = (sale) => {
  // You can navigate to the detailed view of the selected sale, e.g., '/sale/:id'.
  // Use Vue Router for this purpose.
};



// Fetch the list of sales from your Django backend
onMounted(async () => {
  try {
    // Fetch the list of sales and populate the sales array.
    // You may need to make an API call to your Django backend for this.
  } catch (error) {
    console.error('Failed to fetch sales:', error);
  }
});
</script>
<template>

      <q-card flat class="bg-primary text-accent q-mx-auto full-width" style="overflow-x:scroll;">
        <q-card-section>
          <h6 class="q-mb-md text-center">My Sales</h6>
          <q-table
            :rows="sales"
            row-key="id"
            :columns="columns"
            :rows-per-page-options="[5, 10, 20]"
            class="bg-primary text-accent"
            responsive
          >
            <template v-slot:body-cell-actions="props">
              <q-td :props="props">
                <q-btn
                  label="View"
                  color="primary"
                  @click="viewSale(props.row)"
                />
              </q-td>
            </template>
          </q-table>
        </q-card-section>
      </q-card>
  
</template>
