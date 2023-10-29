<script setup lang="ts">
import { toRefs,ref } from 'vue'


const count=ref(0)


const props=defineProps(['dev'])

toRefs(props)


</script >


<template>
    <div>


    </div>
</template>



<style scoped>

</style>