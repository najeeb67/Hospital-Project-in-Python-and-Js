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
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      age: '',
      condition: ''
    };
  },
  methods: {
    submitForm() {
      // Handle form submission logic
      console.log('Patient Added:', { name: this.name, age: this.age, condition: this.condition });
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
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}
</style>
