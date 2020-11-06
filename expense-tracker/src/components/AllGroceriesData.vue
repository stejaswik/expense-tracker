<template>
  <div class="container">
    <h4 align="center">GROCERIES</h4>
    <div>
      <BarChart :styles="myStyles" :chart-data="datacollection" />
    </div>
  </div>
</template>

<script>
import BarChart from './LineChart.js'
import axios from 'axios'

export default {
  components: {
    BarChart
  },
  data () {
    return {
      datacollection: null,
      loaded: false,
      UtilitiesData: [],
      GroceriesData: [],
      RestaurantsData: []
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
        labels: this.labels,
        datasets: [
          {
            borderWidth: 3,
            data: this.UtilitiesData,
            barThickness: 25,
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
            opacity: 1,
            borderColor: 'red',
            // borderJoinStyle: "bevel",
            lineTension: 0
          },

          {
            borderWidth: 3,
            data: this.GroceriesData,
            barThickness: 25,
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
            opacity: 1,
            borderColor: 'blue',
            // borderJoinStyle: "bevel",
            lineTension: 0
          },

          {
            borderWidth: 3,
            data: this.RestaurantsData,
            barThickness: 25,
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
            opacity: 1,
            borderColor: 'green',
            // borderJoinStyle: "bevel",
            lineTension: 0
          }
        ]
      }
    },
    getBankSplits () {
      axios
        .get('http://localhost:5000/getSum')
        .then(response => {
          var results = response.data
          var GroceriesmonthsData = results.AllGroceriesTotal

          var lab = []
          var out = []
          for (var i = 0; i < GroceriesmonthsData.length; i++) {
            lab.push(GroceriesmonthsData[i].month)
            out.push(GroceriesmonthsData[i].total)
          }

          this.labels = lab
          this.GroceriesData = out
          this.fillData()
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    myStyles () {
      return {
        height: '60%',
        width: '85%',
        position: 'relative'
      }
    }
  }
}
</script>

<style scoped></style>
