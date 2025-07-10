<template>
    <li class="accordion-item">
        <div 
            class="accordion__trigger"
            :class="{'accordion__trigger_active': visible}"
            @click="open"
        >
            <slot name="accordion-trigger"></slot>
        </div>

        <transition 
            name="accordion"
            @enter="start"
            @after-enter="end"
            @before-leave="start"
            @after-leave="end"
        >
            <div 
                class="accordion-body"
                v-show="visible"
            >
                <ul class="pl-0">
                    <slot name="accordion-content"></slot>
                </ul>
            </div>
        </transition>
    </li>
</template>

<script>
export default {
    name: 'AccordionItem',
    props: {},
    inject: ["Accordion"],
    data() {
        return {
            index: null
        };
    },
    computed: {
        visible() {
            return this.index == this.Accordion.active;
        }
    },
    methods: {
        open() {
            if (this.visible) {
                this.Accordion.active = null;
            } else {
                this.Accordion.active = this.index;
            }
        },
        start(el) {
            el.style.height = el.scrollHeight + "px";
        },
        end(el) {
            el.style.height = "";
        }
    },
    created() {
        this.index = this.Accordion.count++;
    }
}
</script>