<template>
  <div>
    <h1>Doctors in {{ department }}</h1>
    <ul>
      <li v-for="doctor in doctors" :key="doctor.id">
        {{ doctor.name }} - {{ doctor.specialization }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["department"],
  data() {
    return {
      doctors: [],
    };
  },
  watch: {
    department: "fetchDoctors",
  },
  created() {
    this.fetchDoctors();
  },
  methods: {
    async fetchDoctors() {
      if (this.department) {
        try {
          const response = await axios.get(
            `http://localhost:8000/departments/${encodeURIComponent(
              this.department
            )}/doctors`
          );
          this.doctors = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
};
</script>

<style scoped>
/* Add some styles if needed */
</style>
