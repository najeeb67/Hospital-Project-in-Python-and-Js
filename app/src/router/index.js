import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import DoctorForm from "../components/DoctorForm.vue";
import DoctorList from "../components/DoctorList.vue";
import PatientForm from "../components/PatientForm.vue";
import PatientList from "../components/PatientList.vue";
import AppointmentForm from "../components/AppointmentForm.vue";
import Departments from "@/components/Departments.vue";
import services from "@/components/services.vue";
import contact_us from "../views/contact_us.vue";
import Events from "../views/Events.vue";

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
  {
    path: "/services/:service",
    name: "services",
    component: services,
  },
  {
    path: "/contact_us",
    name: "contact_us",
    component: contact_us,
  },
  {
    path: "/Events",
    name: "Events",
    component: Events,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
