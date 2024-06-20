// apiService.js
import axios from 'axios';

// Create an instance of axios with custom configurations
const apiClient = axios.create({
  baseURL: 'http://localhost:8000',  // Replace with your FastAPI server URL
  headers: {
    'Content-Type': 'application/json',
    // You can add other headers here as needed
  }
});

// Define your ApiService methods
export default {
  // Example method to fetch all doctors
  getDoctors() {
    return apiClient.get('/doctors/');
  },

  // Example method to create a new doctor
  createDoctor(doctor) {
    return apiClient.post('/doctors/', doctor);
  },

  // Example method to update an existing doctor
  updateDoctor(doctorId, doctor) {
    return apiClient.put(`/doctors/${doctorId}`, doctor);
  },

  // Example method to delete a doctor
  deleteDoctor(doctorId) {
    return apiClient.delete(`/doctors/${doctorId}`);
  },

  // Example method to fetch all patients
  getPatients() {
    return apiClient.get('/patients/');
  },

  // Example method to create a new patient
  createPatient(patient) {
    return apiClient.post('/patients/', patient);
  },

  // Example method to update an existing patient
  updatePatient(patientId, patient) {
    return apiClient.put(`/patients/${patientId}`, patient);
  },

  // Example method to delete a patient
  deletePatient(patientId) {
    return apiClient.delete(`/patients/${patientId}`);
  }
};
