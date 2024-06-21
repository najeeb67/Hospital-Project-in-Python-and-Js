<template>
  <div class="form-container">
    <h2>Add a New Patient</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" v-model="name" required />
      </div>
      <div class="form-group">
        <label for="age">Age</label>
        <input type="number" id="age" v-model="age" required />
      </div>
      <div class="form-group">
        <label for="condition">Condition</label>
        <input type="text" id="condition" v-model="condition" required />
      </div>
      <div class="form-group">
        <label for="doctor_id">Doctor ID</label>
        <input type="number" id="doctor_id" v-model="doctor_id" required />
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      name: '',
      age: '',
      condition: '',
      doctor_id: '' 
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/patients/', {
          name: this.name,
          age: this.age,
          condition: this.condition,
          doctor_id: this.doctor_id // Include doctor_id in the POST request
        });
        console.log("patient added", response.data);
        this.$router.push({ name: 'PatientList' });
      } catch (error) {
        console.error('There was an error adding the patient:', error.response.data);
      }
    }
  }
};
</script>


<style scoped>
.form-container {
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  margin: 40px auto;
}

.form-container h2 {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #555;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: rgb(87, 82, 82);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: rgb(87, 82, 82);
}
</style>
