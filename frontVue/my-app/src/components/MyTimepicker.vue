<template>
    <div>
        <vue-timepicker v-model="selectedTime" format="HH:mm" ref="timepicker" />
        <button @click="confirmTime">Confirm Time</button>
    </div>
</template>
  
<script>

import VueTimepicker from 'vue2-timepicker';

export default {
    components: {
        VueTimepicker,
    },
    data() {
        return {
            selectedTime: '', // Holds the selected time in "HH:mm" format
        };
    },
    methods: {
        confirmTime() {
            console.log('Selected Time:', this.selectedTime);
        },
    },
};
</script>

  
  
  
  