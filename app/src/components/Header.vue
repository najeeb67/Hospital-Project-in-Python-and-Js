<template>
    <header>
      <div class="container">
        <h1>Hospital Management System</h1>
        <nav>
          <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/doctors">Doctors</router-link></li>
            <li><router-link to="/patients">Patients</router-link></li>
          </ul>
        </nav>
      </div>
    </header>
  </template>
  
  <style scoped>
  header {
    background-color: #3498db;
    color: white;
    padding: 20px 0;
  }
  
  header h1 {
    margin-bottom: 10px;
  }
  
  nav ul {
    list-style: none;
    display: flex;
    gap: 15px;
  }
  
  nav a {
    color: white;
  }
  </style>
  