import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import DoctorForm from "../components/DoctorForm.vue";
import DoctorList from "../components/DoctorList.vue";
import PatientForm from "../components/PatientForm.vue";
import PatientList from "../components/PatientList.vue";
import AppointmentForm from "../components/AppointmentForm.vue";
import Departments from "@/components/Departments.vue";

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
  {
    path: "/departments/:department",
    name: "Departments",
    component: Departments,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
