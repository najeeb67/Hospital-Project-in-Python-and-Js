<template>
  <header>
    <div class="container">
      <h1>Hospital Management System</h1>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/doctors">Doctors</router-link></li>
          <li><router-link to="/patients">Patients</router-link></li>
          <li><router-link to="/appointments">Appointments</router-link></li>
          <li @click="toggleDropdown" class="dropdown">
            Departments
            <ul v-if="dropdownVisible" class="dropdown-content">
              <li v-for="department in departments" :key="department">
                <router-link
                  :to="{
                    name: 'Departments',
                    params: { department: encodeURIComponent(department) },
                  }"
                >
                  {{ department }}
                </router-link>
              </li>
            </ul>
          </li>
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

<script>
import axios from "axios";

export default {
  data() {
    return {
      departments: [],
      dropdownVisible: false,
    };
  },
  created() {
    this.fetchDepartments();
  },
  methods: {
    async fetchDepartments() {
      try {
        const response = await axios.get("http://localhost:8000/departments/");
        this.departments = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    toggleDropdown() {
      this.dropdownVisible = !this.dropdownVisible;
    },
  },
};
</script>

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
  text-decoration: none;
  padding: 10px;
}

.dropdown {
  position: relative;
  cursor: pointer;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  padding: 10px;
  min-width: 160px;
  border-radius: 5px;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown-content li {
  padding: 8px 12px;
  cursor: pointer;
}

.dropdown-content li:hover {
  background-color: #ddd;
}

.dropdown-content li a {
  color: black;
  text-decoration: none;
}

.dropdown-content li a:hover {
  text-decoration: underline;
}
</style>
