<template>
  <div class="form-container">
    <h2>Add a New Doctor</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" v-model="name" required />
      </div>
      <div class="form-group">
        <label for="specialization">Specialization</label>
        <input type="text" id="specialization" v-model="specialization" required />
      </div>
      <div class="form-group">
        <label for="department">Department</label>
        <input type="text" id="department" v-model="department" required />
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
      specialization: '',
      department: ''
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/doctors/', {
          name: this.name,
          specialization: this.specialization,
          department: this.department
        });
        console.log('Doctor Added:', response.data);
        this.$router.push({ name: 'DoctorList' });
      } catch (error) {
        console.error('There was an error adding the doctor:', error);
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
