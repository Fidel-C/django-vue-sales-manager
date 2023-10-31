<script setup lang="ts">
import { Inertia } from '@inertiajs/inertia';
import { useForm, usePage } from '@inertiajs/inertia-vue3';



const emit=defineEmits(['submitted'])


const form = useForm({
    first_name: '',
    last_name: '', username: '',
    email: '',
    password1: '',
    password2:''
})







</script>


<template>

 <q-container>
      <div class="q-pa-md">
        <q-card class="q-pa-md">
          <h2 class="text-h5 q-mb-md text-secondary">Sign Up</h2>
     
   <q-form
    @submit.prevent="emit('submitted',form)"
    @reset="form.reset()"
    class="q-gutter-md"
   >

   <div class="column q-pa-sm justify-between q-gutter-y-md">

    <q-input   label="First Name" v-model="form.first_name" />
    <q-input  label="Last Name" v-model="form.last_name" />
    <q-input  label="Username" v-model="form.username" />
    <q-input  label="Email" v-model="form.email" type="email" />
    <q-input  label="Password" type="password"  v-model="form.password1" />
    <q-input  label="Password Confirm" type="password" v-model="form.password2" />
        

   </div>
    
    <div>
        <q-btn label="Reset" type="reset" color="warning" flat class="q-ml-sm" />
        <q-btn label="Submit" type="submit" color="primary"/>
    </div>
   </q-form>
        </q-card>
      </div>
    </q-container>



</template>



<style scoped>

</style>