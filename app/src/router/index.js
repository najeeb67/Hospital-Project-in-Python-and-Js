import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import DoctorForm from "../components/DoctorForm.vue";
import DoctorList from "../components/DoctorList.vue";
import PatientForm from "../components/PatientForm.vue";
import PatientList from "../components/PatientList.vue";
import AppointmentForm from "../components/AppointmentForm.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/doctors/add",
    name: "DoctorForm",
    component: DoctorForm,
  },
  {
    path: "/doctors",
    name: "DoctorList",
    component: DoctorList,
  },
  {
    path: "/patients/add",
    name: "PatientForm",
    component: PatientForm,
  },
  {
    path: "/patients",
    name: "PatientList",
    component: PatientList,
  },
  {
    path: "/appointments",
    name: "AppointmentForm",
    component: AppointmentForm,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
