<template>
    <div class="our-latest-projects ptb-80">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 col-md-12">
                    <div class="section-title text-left">
                        <h2>Our Latest <span>Projects</span></h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>

                <div class="col-lg-6 col-md-12">
                    <div class="shorting-menu">
                        <button 
                            class="filter" 
                            :class="{active:itemFilterKey == 'all'}" 
                            v-on:click="itemFilterKey = 'all'" 
                        >
                            All
                        </button>
                        <button 
                            class="filter" 
                            :class="{active:itemFilterKey == 'design'}"
                            v-on:click="itemFilterKey = 'design'"
                        >
                            Design
                        </button>
                        <button
                            class="filter" 
                            :class="{active:itemFilterKey == 'branding'}"
                            v-on:click="itemFilterKey = 'branding'"
                        >
                            Branding
                        </button>
                        
                        <button
                            :class="{active:itemFilterKey == 'architecture'}"
                            v-on:click="itemFilterKey = 'architecture'"
                        >
                            Architecture
                        </button>
                        
                        <button
                            :class="{active:itemFilterKey == 'creative'}"
                            v-on:click="itemFilterKey = 'creative'"
                        >
                            Creative
                        </button>
                    </div>
                </div>
            </div>

            <div class="projects-items">
                <div class="row justify-content-center">
                    <div 
                        v-for="item in itemFilter"
                        :key="item.id"
                        class="col-lg-4 col-sm-6"
                    >
                        <div class="single-latest-projects">
                            <img :src="item.img" alt="image">

                            <div class="content">
                                <span>{{item.category}}</span>
                                <h3>{{item.title}}</h3>
                            </div>
                            <a href="#" class="link-btn"></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'OurLatestProjects',
    data: function (){
        return {
            itemFilterKey: 'all',
            items: [
                {
                    id: 1,
                    img: require('../../../assets/img/agency-portfolio-projects/img1.jpg'),
                    category: 'Design',
                    title: 'Creative Woman',
                    key: 'architecture'
                },
                {
                    id: 2,
                    img: require('../../../assets/img/agency-portfolio-projects/img2.jpg'),
                    category: 'Camera',
                    title: 'Worldwide Photography',
                    key: 'design'
                },
                {
                    id: 3,
                    img: require('../../../assets/img/agency-portfolio-projects/img3.jpg'),
                    category: 'Design',
                    title: 'Creative Design',
                    key: 'creative'
                },
                {
                    id: 4,
                    img: require('../../../assets/img/agency-portfolio-projects/img4.jpg'),
                    category: 'Tower',
                    title: 'Creative Tower',
                    key: 'design'
                },
                {
                    id: 5,
                    img: require('../../../assets/img/agency-portfolio-projects/img5.jpg'),
                    category: 'Design',
                    title: 'Creative World',
                    key: 'design'
                },
                {
                    id: 6,
                    img: require('../../../assets/img/agency-portfolio-projects/img6.jpg'),
                    category: 'Design',
                    title: 'Creative Style',
                    key: 'architecture'
                },
                {
                    id: 7,
                    img: require('../../../assets/img/agency-portfolio-projects/img7.jpg'),
                    category: 'Design',
                    title: 'Creative Woman',
                    key: 'design'
                },
                {
                    id: 8,
                    img: require('../../../assets/img/agency-portfolio-projects/img8.jpg'),
                    category: 'Design',
                    title: 'Creative Woman',
                    key: 'branding'
                },
                {
                    id: 9,
                    img: require('../../../assets/img/agency-portfolio-projects/img9.jpg'),
                    category: 'Design',
                    title: 'Creative Woman',
                    key: 'creative'
                },
            ],
        }
    },
    computed: {
        itemFilter(){
            return this[this.itemFilterKey]
        },
        all(){
            return this.items
        },
        design(){
            return this.items.filter((item) => item.key == 'design')
        },
        branding(){
            return this.items.filter((item) => item.key == 'branding')
        },
        architecture(){
            return this.items.filter((item) => item.key == 'architecture')
        },
        creative(){
            return this.items.filter((item) => item.key == 'creative')
        },
    }
}
</script>