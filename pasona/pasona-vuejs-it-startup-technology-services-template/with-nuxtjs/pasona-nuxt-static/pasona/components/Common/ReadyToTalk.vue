<template>
  <div class="ready-to-talk">
    <div class="container">
      <h3>Ready to talk?</h3>
      <p>Our team is here to answer your question about Pasona</p>
      <NuxtLink to="/contact" class="btn btn-primary"> Contact Us </NuxtLink>
      <span>
        <NuxtLink to="/contact">
          Or, get started now with a free trial
        </NuxtLink>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReadyToTalk",
};
</script>