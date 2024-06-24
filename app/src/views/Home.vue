<template>
  <div class="home">
    <div class="hero">
      <div class="hero-content">
        <h1>Welcome to the Hospital Management System</h1>
        <p>Your health is our priority.</p>
        <router-link to="/appointments" class="btn-primary"
          >Book an Appointment</router-link
        >
      </div>
    </div>

    <div class="services-section">
      <h2>Our Services</h2>
      <div class="services">
        <div class="service">
          <h3>Emergency Care</h3>
          <p>24/7 emergency care to provide immediate assistance.</p>
        </div>
        <div class="service">
          <h3>Outpatient Services</h3>
          <p>Comprehensive outpatient services for all your needs.</p>
        </div>
        <div class="service">
          <h3>Surgery</h3>
          <p>State-of-the-art surgical facilities with expert surgeons.</p>
        </div>
        <div class="service">
          <h3>Pediatrics</h3>
          <p>Specialized care for children by experienced pediatricians.</p>
        </div>
      </div>
    </div>

    <div class="testimonials-section">
      <h2>What Our Patients Say</h2>
      <div class="testimonials">
        <div class="testimonial">
          <p>
            "The care and attention I received at the hospital were outstanding. Highly
            recommend!"
          </p>
          <span>- Najeeb</span>
        </div>
        <div class="testimonial">
          <p>"Excellent service and professional staff. I felt well taken care of."</p>
          <span>- Ahmad</span>
        </div>
      </div>
    </div>

    <div class="contact-section">
      <h2>Contact Us</h2>
      <p>If you have any questions or need further information, please contact us.</p>
      <router-link to="/contact_us" class="btn-secondary">Contact Us</router-link>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
}

.hero {
  background-size: cover;
  background-position: center;
  color: white;
  padding: 100px 20px;
}

.hero-content {
  background: rgba(0, 0, 0, 0.5);
  padding: 20px;
  display: inline-block;
  border-radius: 10px;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.btn-primary {
  background-color: rgb(87, 82, 82);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1.2rem;
}

.services-section,
.testimonials-section,
.contact-section {
  padding: 50px 20px;
}

.services-section h2,
.testimonials-section h2,
.contact-section h2 {
  font-size: 2rem;
  margin-bottom: 30px;
}

.services {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.service {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  width: 200px;
  margin: 10px;
}

.service h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.testimonials {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.testimonial {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  margin: 10px;
}

.testimonial p {
  font-size: 1rem;
  margin-bottom: 10px;
}

.testimonial span {
  font-weight: bold;
}

.contact-section p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1.2rem;
}
</style>
