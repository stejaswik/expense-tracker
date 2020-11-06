<template>
  <div class="container">
    <h5 align="center">THIS MONTH VS PREVIOUS MONTH</h5>
    <div>
      <HorizontalBar :styles="myStyles" :chart-data="datacollection" />
    </div>
  </div>
</template>

<script>
import HorizontalBar from './HorizontalBarChart.js'
import axios from 'axios'

export default {
  components: {
    HorizontalBar
  },
  data () {
    return {
      datacollection: null,
      loaded: false,
      data: []
    }
  },
  mounted () {
    this.getBankSplits()

    this.$root.$on('ExpenseAdded', () => {
      this.getBankSplits()
    })
  },
  methods: {
    fillData () {
      this.datacollection = {
        labels: ['Actual', 'Target'],
        datasets: [
          {
            backgroundColor: ['#41BFFF', '#515e66'],
            borderWidth: 3,
            data: this.data,
            barThickness: 25
          }
        ]
      }
    },
    getBankSplits () {
      axios
        .get('http://localhost:5000/getBankSplits')
        .then((response) => {
          var results = response.data
          this.data = [results.Total[0].MonthlyTotal, 3600]
          this.fillData()
        })
        .catch((err) => console.error(err))
    }
  },
  computed: {
    myStyles () {
      return {
        height: '40%',
        width: '90%',
        position: 'relative'
      }
    }
  }
}
</script>

<style scoped></style>
