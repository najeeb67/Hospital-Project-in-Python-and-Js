<template>
    <div class="list-container">
      <h2>Doctor List</h2>
      <ul>
        <li v-for="doctor in doctors" :key="doctor.id">{{ doctor.name }} - {{ doctor.specialization }}</li>
      </ul>
    </div>
    <h2><router-view to="/DoctorForm"> </router-view></h2>
    
  </template>
  
  

  <style scoped>
  .list-container {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 40px auto;
  }
  
  .list-container h2 {
    margin-bottom: 20px;
  }
  
  ul {
    list-style: none;
  }
  
  ul li {
    background-color: #f4f4f9;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  </style>
  