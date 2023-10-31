<script setup lang="ts">
import { useForm } from '@inertiajs/inertia-vue3';
import { ref,} from 'vue';
import { IStore, StoreInput } from '../models';
import { Inertia } from '@inertiajs/inertia';



const form = useForm({

  description: '',
  total_price: 0,
    store:''
 

})

const props=defineProps<{stores:IStore[]}>()





const newList = ref<StoreInput[]>([]);

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


const addSale =() => {
    form.post('create-sale/', {
        data: form.data(), forceFormData: true, onSuccess(data) { 
            console.log(data)
        }, onError(err) {
        console.log(err)
    }})
        
    
}




</script>


<template>
      <q-card flat  class="col">
        <q-card-section>
          <h6 class="q-mb-md text-primary text-center">Add Sale</h6>
           <q-form @submit.prevent="addSale">

    <q-select
      v-model="form.store"
      :options="newList"
      label="Select Store"
    ></q-select>
    <q-input v-model="form.description" label="Description"></q-input>
    <q-input v-model="form.total_price" label="Total Price"></q-input>
    <q-btn type="submit" label="Add Sale"></q-btn>
  </q-form>
        </q-card-section>
      </q-card>

</template>
