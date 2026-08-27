<script>
  import { onMount } from "svelte";
  let message = "loading";
  const base = import.meta.env.VITE_API_BASE_URL;
  onMount(async () => {
    try {
      const r = await fetch(`${base}/message`);
      message = (await r.json()).message;
    } catch (e) {
      message = `error: ${e.message}`;
    }
  });
</script>
<main style="font-family:system-ui;padding:2rem">
  <h1>Svelte + Fastify + MySQL</h1>
  <p id="api-message">{message}</p>
  <small>API base: {base}</small>
</main>
