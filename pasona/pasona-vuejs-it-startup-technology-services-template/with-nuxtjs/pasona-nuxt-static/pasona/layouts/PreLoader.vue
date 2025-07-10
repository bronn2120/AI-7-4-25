<template>
    <div>
        <div class="preloader" v-if="!loading">
            <div class="spinner"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PreLoader',
    data: () => ({
        loading: false,
    }),
    created() {
        this.$nextTick(function() {
            this.loading = true
        })
    },
}
</script>