<template>
  <div class="container">
    <h4 align="center">TRAVEL</h4>
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
            borderWidth: 1,
            data: this.GroceriesData,
            barThickness: 25,
            backgroundColor: 'rgba(255, 255, 255, 0.8)',
            opacity: 1,
            borderColor: 'blue',
            // borderJoinStyle: "bevel",
            pointRadius: 1,
            lineTension: 0.45
          }
        ]
      }
    },
    getBankSplits () {
      axios
        .get('http://localhost:5000/getSum')
        .then(response => {
          var results = response.data
          var GroceriesmonthsData = results.AllTravelTotal

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
