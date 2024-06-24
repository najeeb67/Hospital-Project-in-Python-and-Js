<template>
  <div class="news-events">
    <h1>News and Events</h1>
    <div class="events">
      <div class="event" v-for="event in events" :key="event.id">
        <h2>{{ event.title }}</h2>
        <p>{{ event.date }}</p>
        <p>{{ event.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewsEvents",
  data() {
    return {
      events: [
        {
          id: 1,
          title: "Health Fair",
          date: "2024-06-30",
          description:
            "Join us for our annual health fair, where you can get free health screenings and learn more about healthy living.",
        },
        {
          id: 2,
          title: "Blood Donation Drive",
          date: "2024-07-15",
          description:
            "We are organizing a blood donation drive. Come and donate blood to save lives.",
        },
      ],
    };
  },
};
</script>

<style scoped>
.news-events {
  padding: 20px;
}

.news-events h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.event {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
}

.event h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.event p {
  font-size: 1rem;
  margin-bottom: 5px;
}
</style>
