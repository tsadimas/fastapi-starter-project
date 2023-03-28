<template>
  <section>
    <p>This site is built with FastAPI and Vue.</p>

    <div id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p>
    </div>
  </section>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
});
</script>