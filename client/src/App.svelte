<script>
  import { Router, createRouter } from "@roxi/routify";
  import routes from "../.routify/routes.default.js";

  export const router = createRouter({ routes });
</script>

<!-- The Router will now find and use your _module.svelte file automatically -->
<Router {router} />
