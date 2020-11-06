<template>
  <div class="container">
    <h2 align="center">SPLIT BY CATEGORY</h2>
    <div>
      <LineChart :styles="myStyles" :chart-data="datacollection" />
    </div>
  </div>
</template>

<script>
import LineChart from './PieChart.js'
import axios from 'axios'

export default {
  components: {
    LineChart
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
        labels: [
          'Travel',
          'Entertainment',
          'Subscriptions',
          'Utilities',
          'Shopping',
          'Groceries',
          'Restaurants'
        ],
        datasets: [
          {
            label: 'Temp',
            backgroundColor: [
              '#41B883',
              '#E46651',
              '#00D8FF',
              '#E0D8FF',
              '#4068FF',
              '#E1D800',
              '#00FF00'
            ],
            borderColor: 'lightpink',
            pointBackgroundColor: 'blue',
            borderWidth: 1,
            data: this.data
          }
        ]
      }
    },

    getBankSplits () {
      axios
        .get('http://localhost:5000/getBankSplits')
        .then(response => {
          var results = response.data
          var Travel = results.TotalCategory[0].Travel
          var Entertainment = results.TotalCategory[0].Entertainment
          var Subscriptions = results.TotalCategory[0].Subscriptions
          var Utilities = results.TotalCategory[0].Utilities
          var Shopping = results.TotalCategory[0].Shopping
          var Groceries = results.TotalCategory[0].Groceries
          var Restaurants = results.TotalCategory[0].Restaurants

          this.data = [
            Travel,
            Entertainment,
            Subscriptions,
            Utilities,
            Shopping,
            Groceries,
            Restaurants
          ]
          this.fillData()
          console.log(this.data)
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    myStyles () {
      return {
        height: '40%',
        width: '99%',
        position: 'relative'
      }
    }
  }
}
</script>

<style scoped></style>
