<template>
    <div class="page-title-area">
            <div class="d-table">
                <div class="d-table-cell">
                    <div class="container">
                        <h2>{{pageTitle}}</h2>
                    </div>
                </div>
			</div>
			
			<div class="shape1"><img src="~/assets/img/shape1.png" alt="shape"></div>
			<div class="shape2 rotateme"><img src="~/assets/img/shape2.svg" alt="shape"></div>
			<div class="shape3"><img src="~/assets/img/shape3.svg" alt="shape"></div>
			<div class="shape4"><img src="~/assets/img/shape4.svg" alt="shape"></div>
			<div class="shape5"><img src="~/assets/img/shape5.png" alt="shape"></div>
			<div class="shape6 rotateme"><img src="~/assets/img/shape4.svg" alt="shape"></div>
			<div class="shape7"><img src="~/assets/img/shape4.svg" alt="shape"></div>
			<div class="shape8 rotateme"><img src="~/assets/img/shape2.svg" alt="shape"></div>
        </div>
</template>

<script>
export default {
    name: 'PageTitle',
    props: ['pageTitle']
}
</script>