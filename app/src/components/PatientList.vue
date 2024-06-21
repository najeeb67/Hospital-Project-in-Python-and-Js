<template>
  <div class="list-container">
    <h2>Patient List</h2>
    <button @click="goToAddPatient">Add Patient</button>
    <ul>
      <li v-for="patient in patients" :key="patient.id">
        {{ patient.name }} - {{ patient.condition }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      patients: [],
    };
  },
  methods: {
    async fetchPatients() {
      try {
        const response = await axios.get("http://localhost:8000/patients/");
        this.patients = response.data;
      } catch (error) {
        console.error("There was an error fetching the patients:", error.response.data);
      }
    },
    goToAddPatient() {
      this.$router.push({ name: "PatientForm" });
    },
  },
  mounted() {
    this.fetchPatients();
  },
};
</script>

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

button {
  background-color: rgb(87, 82, 82);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 20px;
}

button:hover {
  background-color: rgb(87, 82, 82);
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
