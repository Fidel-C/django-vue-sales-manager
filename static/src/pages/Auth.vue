<script setup lang="ts">
import { ref } from 'vue';
import RegisterForm from '../components/RegisterForm.vue';
import LoginForm from '../components/LoginForm.vue';
import { usePage,useForm } from '@inertiajs/inertia-vue3';
import { Inertia } from '@inertiajs/inertia';
import { Notify } from 'quasar';




const activeTab = ref('login')

const errors=ref(null)


const submitRegister = async (form) => {
 

const res= await form.post(`${usePage().url.value}register/`,{data:form.data(),forceFormData:true})
console.log(res)


    
}




const submitLogin = (val) => {
    const form = useForm({ ...val.data() })
    form.post(`${usePage().url.value}login/`, {
        data: form.data(), forceFormData: true, onSuccess() {
        Notify.create({type:'positive',message:'Logged In',icon:'key'})
        }, onError(errors) {
            console.log(errors)
            

        
        }
    })
    
   

  

}


</script>


<template>
  <div class="column a-pa-sm">
    
    <q-tabs v-model="activeTab">
      <q-tab name="login">Login</q-tab>
      <q-tab name="register">Register</q-tab>
    </q-tabs>
    <q-tab-panels v-model="activeTab">
      <q-tab-panel name="login">
        <LoginForm  @submitted="submitLogin" />
      </q-tab-panel>
      <q-tab-panel name="register">
        <RegisterForm  @submitted="submitRegister"  />
      </q-tab-panel>
    </q-tab-panels>
  </div>
</template>

