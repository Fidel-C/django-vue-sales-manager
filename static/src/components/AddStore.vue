<script setup lang="ts">
import { ref } from 'vue';
import { Inertia } from '@inertiajs/inertia';
import { useForm } from '@inertiajs/inertia-vue3';

const form = useForm({
  name: '',
  location: '',
});

const addStore = async () => {
    form.post('create-store/', {
        data: form.data(), forceFormData: true, onSuccess(data) {
            console.log(data)
           form.reset()
        }, onError(error) {
        console.log(error)
    }})
 
}
</script>



<template>
 
      <q-card flat class="col">
        <q-card-section>
          <h6 class="q-mb-md text-primary text-center">Add Store</h6>
          <q-form @submit.prevent="addStore">
            <q-input v-model="form.name" label="Store Name" />
            <q-input v-model="form.location" label="Location" />
            <q-btn label="Add Store" type="submit" color="primary" />
          </q-form>
        </q-card-section>
      </q-card>
 
</template>


