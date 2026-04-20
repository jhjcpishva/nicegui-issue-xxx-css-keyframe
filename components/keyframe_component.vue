<template>
  <p class="my-fade-animation">Fade</p>
</template>

<script>
export default {
}
</script>

<style>
p.my-fade-animation {
  animation: fade-in-out 0.5s ease-in-out infinite alternate;
}

@keyframes fade-in-out {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
