
<script setup lang="ts">
import { ref } from "vue";
import { useForm } from '@inertiajs/inertia-vue3';
import { IStore, StoreInput } from '../models';



const category = useForm({
  title: "",
  store:""
});


const props=defineProps<{stores:IStore[]}>()





const newList = ref < StoreInput[] > ([]);


// Loop through the original list and transform each object
for (let i = 0; i < props!.stores!.length; i++) {
    let originalObject:IStore = props.stores[i];
    let transformedObject= <StoreInput>{
        value: originalObject!.id,
        label: originalObject!.name
    };
    newList.value.push(transformedObject);
}

console.log(newList.value)


const submitForm = () => {
  // Handle form submission and add the category to your database
 

};
</script>



<template>
<q-card flat class="col-4">
    <h6 class="text-primary text-center">Add Category</h6>
    <q-card-section>
       <q-form @submit="submitForm">
    <q-input v-model="category.title" label="Category Title"></q-input>
    <q-select
      v-model="selectedStores"
      :options="newList"
      label="Select Store(s)"
    ></q-select>
    <q-btn type="submit" label="Add Category"></q-btn>
  </q-form>
    </q-card-section>
</q-card>
</template>