<script lang="ts">
import Layout from '../layouts/base.vue'
import ListStores from '../components/ListStores.vue';


export default {
    layout: Layout,
    components: { ListStores }
}

</script>



<script setup lang="ts">
import { toRefs, ref } from 'vue'
import { Link, useForm } from '@inertiajs/inertia-vue3';
import { fabShopify} from '@quasar/extras/fontawesome-v5'
import { ionCart,ionStorefront,ionLogOut,ionPerson} from '@quasar/extras/ionicons-v7'

import AddStore from '../components/AddStore.vue'
import AddSale from '../components/AddSale.vue'
import AddProduct from '../components/AddProduct.vue';
import AddCategory from '../components/AddCategory.vue';
import ListSales from '../components/ListSales.vue';

const count=ref(0)



const logOut = async () => {
  useForm({}).get('logout/', {
    onSuccess(data){
     console.log('success')
    },
    onError(error) {
     console.log(error)
  }
})

  
}

// to recive the props as one object
const props = defineProps({dev:String,user:Object,stores:Array})

// to spread our the props
toRefs(props)

    
</script >


<template>
  <div class="column" style="height:100%;">
<div class="col row flex-1">
  <!-- left side bar -->
    <div class="column bg-black col-2 q-mx-pa items-center">
          <q-list bordered class="q-pt-xl q-gutter-y-lg">

          <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon color="grey-1" :name="ionPerson" />
              </q-item-section>
              <q-item-section class="text-accent">{{ user?.username }}</q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon color="grey-1" :name="ionCart" />
              </q-item-section>
              <q-item-section class="text-accent">Products</q-item-section>
            </q-item>

            <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon color="grey-1" :name="ionStorefront" />
              </q-item-section>
              <q-item-section class="text-accent">Stores</q-item-section>
            </q-item>

             <q-item clickable v-ripple>
              <q-item-section avatar>
                <q-icon color="grey-1" :name="fabShopify" />
              </q-item-section>
              <q-item-section class="text-accent">Sales</q-item-section>
            </q-item>

              <q-item clickable v-ripple @click="logOut">
              <q-item-section avatar>
                <q-icon color="grey-1" :name="ionLogOut" />
              </q-item-section>
              <q-item-section class="text-accent">Logout</q-item-section>
            </q-item>
          </q-list>
    </div>

    <!-- end of left side-bar -->


<!-- main dashboard -->
    <div class="column  col-8 q-pt-xl">
             

      <!-- add store and add sale containers -->
<div class="row q-mx-auto  full-width justify-around q-gutter-x-md q-pa-sm">

     <AddStore/>

   <AddSale :stores="stores" />

</div>
<!-- end of add store and add sale containers -->




<q-separator spaced inset horizontal dark style="height:5px;" />



<!-- add  products -->

<div class="row full-width q-pa-sm q-my-xl q-mx-auto q-gutter-x-md justify-around">




<AddProduct/>

<AddCategory :stores="stores"/>



</div>
<!-- end of add products-->



    </div>
    <!-- end of main dashboard -->




    <!-- right side-bar  -->
<div class="column bg-primary col-2 items-center q-mx-auto">

    
<ListSales/>

<ListStores :stores="stores" />

    </div>

    <!-- end of right side-bar -->

</div>
    
  </div>



</template>



<style scoped>

</style>