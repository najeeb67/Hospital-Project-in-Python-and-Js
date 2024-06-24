<template>
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-section about">
          <h2>About Us</h2>
          <p>
            The Hospital Management System is dedicated to providing the best healthcare
            services. Our mission is to ensure the well-being of our patients through
            state-of-the-art medical care.
          </p>
        </div>
        <div class="footer-section services">
          <h2>Our Services</h2>
          <ul>
            <li>24/7 Emergency Services</li>
            <li>Inpatient and Outpatient Care</li>
            <li>Specialized Medical Treatments</li>
            <li>Diagnostic Imaging</li>
            <li>Physiotherapy</li>
          </ul>
        </div>
        <div class="footer-section news">
          <h2>Latest News</h2>
          <ul>
            <li>New cardiology unit opened</li>
            <li>Upcoming health seminar</li>
            <li>Community outreach programs</li>
          </ul>
        </div>
        <div class="footer-section contact">
          <h2>Contact Us</h2>
          <p><i class="fas fa-phone"></i> +92223323232</p>
          <p><i class="fas fa-envelope"></i> info@hospital.com</p>
          <p><i class="fas fa-map-marker-alt"></i> Lahore Pakistan</p>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="social-icons">
          <a href="#"><i class="fab fa-facebook-f"></i></a>
          <a href="#"><i class="fab fa-twitter"></i></a>
          <a href="#"><i class="fab fa-linkedin-in"></i></a>
          <a href="#"><i class="fab fa-instagram"></i></a>
        </div>
        <p>&copy; 2024 Hospital Management System. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer {
  background-color: rgb(87, 82, 82);
  color: white;
  padding: 30px 0 15px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.footer-section {
  flex: 1;
  margin: 10px 20px;
  min-width: 250px;
}

.footer-section h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.footer-section p,
.footer-section ul,
.footer-section a {
  font-size: 1rem;
  color: #ddd;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 10px;
}

.footer-section ul li a {
  text-decoration: none;
  color: #ddd;
  transition: color 0.3s;
}

.footer-section ul li a:hover {
  color: #fff;
}

.footer-section .fas {
  margin-right: 10px;
}

.footer-bottom {
  text-align: center;
  padding: 10px 0;
  border-top: 1px solid #555;
  margin-top: 20px;
}

.social-icons {
  margin-bottom: 10px;
}

.social-icons a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
  font-size: 1.2rem;
  transition: color 0.3s;
}

.social-icons a:hover {
  color: #ddd;
}

@media (max-width: 768px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
  }

  .footer-section {
    margin: 10px 0;
  }
}
</style>
