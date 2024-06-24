<template>
  <div>
    <h1>{{ service }}</h1>
    <p>Details about the {{ service }} service.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      service: "",
    };
  },
  created() {
    this.service = decodeURIComponent(this.$route.params.service);
  },
};
</script>
