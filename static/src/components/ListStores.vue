<script setup lang="ts">
import { ref, onMounted, toRefs } from 'vue';


const columns = [
  { name: 'name', required: true, label: 'Store Name', align: 'left', field: 'name', sortable: true },
  { name: 'location', required: true, label: 'Location', align: 'left', field: 'location', sortable: true },
];


const props=defineProps({stores:Array})

toRefs(props)

const viewStore = (store) => {
  // You can navigate to the detailed view of the selected store, e.g., '/store/:id'.
  // Use Vue Router for this purpose.
};

// Fetch the list of stores from your Django backend

</script>


<template>

      <q-card flat class="text-accent bg-primary">
        <q-card-section>
          <h6 class="q-mb-md text-center text-accent">My Stores</h6>
          <q-table
            flat
            :rows="stores"
            row-key="id"
            :columns="columns"
            :rows-per-page-options="[5, 10, 20]"
            class="bg-primary text-accent"
          >
            <template v-slot:body-cell-actions="props">
              <q-td :props="props">
                <q-btn
                  label="View"
                  color="primary"
                  @click="viewStore(props.row)"
                />
              </q-td>
            </template>
          </q-table>
        </q-card-section>
      </q-card>
 
</template>

