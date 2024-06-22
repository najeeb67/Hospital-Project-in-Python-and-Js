<template>
  <div class="form-container">
    <h2>Appointment Page</h2>
    <form @submit.prevent="createAppointment">
      <div class="form-group">
        <label for="doctor">Doctor:</label>
        <select v-model="appointment.doctor_id">
          <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">
            {{ doctor.name }} ({{ doctor.department }})
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="patient">Patient:</label>
        <select v-model="appointment.patient_id">
          <option v-for="patient in patients" :key="patient.id" :value="patient.id">
            {{ patient.name }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="time">Appointment Time:</label>
        <input type="datetime-local" v-model="appointment.appointment_time" />
      </div>
      <button type="submit">Create Appointment</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      doctors: [],
      patients: [],
      appointment: {
        doctor_id: null,
        patient_id: null,
        appointment_time: "",
      },
    };
  },
  created() {
    this.fetchDoctors();
    this.fetchPatients();
  },
  methods: {
    async fetchDoctors() {
      const response = await axios.get("http://localhost:8000/doctors");
      this.doctors = response.data;
    },
    async fetchPatients() {
      const response = await axios.get("http://localhost:8000/patients");
      this.patients = response.data;
    },
    async createAppointment() {
      try {
        await axios.post("http://localhost:8000/appointments", this.appointment);
        alert("Appointment created successfully!");
        this.appointment = {
          doctor_id: null,
          patient_id: null,
          appointment_time: "",
        };
      } catch (error) {
        console.error("There was an error creating the appointment:", error);
      }
    },
  },
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

.form-group input,
.form-group select {
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
