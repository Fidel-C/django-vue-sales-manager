
<script setup lang="ts">
import {ref} from 'vue'
import { useForm,usePage} from '@inertiajs/inertia-vue3';
import { Inertia } from '@inertiajs/inertia';


const form=useForm({
    username: '',
    password:''
})






//this is to emit events from this child component to the parent component(Auth)
const emit=defineEmits(['submitted'])






</script>


<template>

 <div>
      <div class="q-pa-md">
        <q-card class="q-pa-md">
          <h2 class="text-h5 q-mb-md text-secondary">Log In</h2>
          <q-form
    @submit.prevent="emit('submitted',form)"
    @reset="form.reset()"
    class="q-gutter-md"
   >

   <div class="column q-pa-sm justify-between q-gutter-y-md">
    <q-input  label="Username" v-model="form.username" />
    <div class="text-red-5" v-if="form.errors.username">{{ form.errors.username }}</div>
  
    <q-input  label="Password" type="password"  v-model="form.password" />
      <div class="text-red-5 " v-if="form.errors.password">{{ form.errors.password }}</div>

        

   </div>
    
    <div>
        <q-btn label="Reset" type="reset" color="warning" flat class="q-ml-sm" />
        <q-btn label="Submit" type="submit" color="primary"/>
    </div>
   </q-form>
        </q-card>
      </div>
    </div>


  
</template>



<style scoped>

</style>