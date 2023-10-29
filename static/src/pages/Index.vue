<template>
    <div>

    <div>This  is a vue app in django developed by {{dev}}</div>

    </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'



const props=defineProps(['dev'])

toRefs(props)


</script >

<style scoped>

</style>