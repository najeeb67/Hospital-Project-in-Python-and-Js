<template>
    <div>
      <PatientForm />
      <PatientList />
    </div>
  </template>
  
  <script>
  import PatientForm from '@/components/PatientForm.vue';
  import PatientList from '@/components/PatientList.vue';
  
  export default {
    components: {
      PatientForm,
      PatientList
    }
  };
  </script>
  
  <style>
  /* Add your styles here */
  </style>
  