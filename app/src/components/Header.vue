<template>
  <header>
    <div class="container">
      <h1>Hospital Management System</h1>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/doctors">Doctors</router-link></li>
          <li><router-link to="/patients">Patients</router-link></li>
          <router-link to="/appointments">Appointments</router-link>
          <li><router-link to="/Departments">Departments</router-link></li>
          <li><router-link to="/services">Our Services</router-link></li>
          <li>
            <router-link to="/Online_Consultations"> Online Consultations</router-link>
          </li>
          <li>
            <router-link to="/Events">News and Events</router-link>
          </li>
          <li><router-link to="/contact_us">contact-us</router-link></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  background-color: rgb(87, 82, 82);
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
