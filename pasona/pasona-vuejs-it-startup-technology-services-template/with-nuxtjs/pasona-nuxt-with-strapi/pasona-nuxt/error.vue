<template>
  <div class="error-area">
    <div class="d-table">
      <div class="d-table-cell">
        <div class="container">
          <div class="error-content">
            <div class="notfound-404">
              <h1>Oops!</h1>
            </div>
            <h3>404 - Page not found</h3>
            <p>
              The page you are looking for might have been removed had its name
              changed or is temporarily unavailable.
            </p>
            <NuxtLink to="/" class="btn btn-primary">Go to Homepage</NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ErrorPage'
};
</script>
