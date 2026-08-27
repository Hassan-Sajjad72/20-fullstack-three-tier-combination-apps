import { createApp, ref, onMounted } from "vue";
createApp({
  setup() {
    const message = ref("loading");
    const base = import.meta.env.VITE_API_BASE_URL;
    onMounted(async () => {
      try {
        const r = await fetch(`${base}/message`);
        message.value = (await r.json()).message;
      } catch (e) {
        message.value = `error: ${e.message}`;
      }
    });
    return { message, base };
  },
  template: `<main style="font-family:system-ui;padding:2rem">
    <h1>Vue + FastAPI + PostgreSQL</h1><p id="api-message">{{message}}</p><small>API base: {{base}}</small>
  </main>`
}).mount("#app");
