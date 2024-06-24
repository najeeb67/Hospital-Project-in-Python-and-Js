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
          <li @click="toggleDropdown('departments')" class="dropdown">
            Departments
            <ul v-if="dropdowns.departments" class="dropdown-content">
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
          <li @click="toggleDropdown('services')" class="dropdown">
            Our Services
            <ul v-if="dropdowns.services" class="dropdown-content">
              <li v-for="service in services" :key="service">
                <router-link
                  :to="{
                    name: 'services',
                    params: { service: encodeURIComponent(service) },
                  }"
                >
                  {{ service }}
                </router-link>
              </li>
            </ul>
          </li>
          <li>
            <router-link to="/Events">News and Events</router-link>
          </li>
          <li><router-link to="/contact_us">Contact Us</router-link></li>
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
      services: [],
      dropdowns: {
        departments: false,
        services: false,
      },
    };
  },
  created() {
    this.fetchDepartments();
    this.fetchServices();
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
    async fetchServices() {
      try {
        const response = await axios.get("http://localhost:8000/services/");
        this.services = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    toggleDropdown(dropdown) {
      this.dropdowns[dropdown] = !this.dropdowns[dropdown];
    },
  },
};
</script>

<style scoped>
header {
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 20px 0;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

header h1 {
  margin-bottom: 10px;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-size: 2rem;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 0;
  padding: 0;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-size: 1rem;
  transition: background-color 0.3s ease, color 0.3s ease;
}

nav a:hover {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
}

.dropdown {
  position: relative;
  cursor: pointer;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 1;
  padding: 10px;
  min-width: 160px;
  border-radius: 5px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.dropdown:hover .dropdown-content {
  display: block;
  opacity: 1;
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

@media (max-width: 768px) {
  nav ul {
    flex-direction: column;
    align-items: center;
  }
}
</style>
