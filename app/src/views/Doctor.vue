<template>
    <div>
      <DoctorForm />
      <DoctorList />
    </div>
  </template>
  
  <script>
  import DoctorForm from '@/components/DoctorForm.vue';
  import DoctorList from '@/components/DoctorList.vue';
  
  export default {
    components: {
      DoctorForm,
      DoctorList
    }
  };
  </script>
  
  <style>
  /* Add your styles here */
  </style>
  