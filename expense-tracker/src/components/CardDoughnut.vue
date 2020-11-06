<template>
  <div class="container">
    <h2 align="center">SPLIT BY CARD</h2>
    <div>
      <PieChart :styles="myStyles" :chartData="datacollection" :options="options" />
    </div>
  </div>
</template>

<script>
import PieChart from './PieChart.js'
// import BarChart from "./BarChart.js";
import axios from 'axios'

export default {
  components: {
    PieChart
    // BarChart
  },
  data () {
    return {
      datacollection: null,
      loaded: false,
      options: {
        legend: {
          display: 'false'
        }
      },
      data: []
    }
  },
  mounted () {
    this.getBankSplits()
    this.getCategorySplits()

    this.$root.$on('ExpenseAdded', () => {
      this.getBankSplits()
      this.getCategorySplits()
    })
  },
  methods: {
    fillData () {
      console.log([labeldata])
      this.datacollection = {
        labels: [
          'Citi Credit Card',
          'Bofa Credit Card',
          'Bofa Checking Account',
          'DCU Checking',
          'Discover Savings',
          'Discover Credit Card',
          'Marriott Credit Card',
          'Chase Credit Card'
        ],
        datasets: [
          {
            backgroundColor: [
              '#41B883',
              '#E46651',
              '#00D8FF',
              '#E0D8FF',
              '#4068FF',
              '#E1D800',
              '#00FF00',
              '#00FFFF'
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
          var Citi = results.TotalCard[0].CitiCreditCard
          var DCUChecking = results.TotalCard[0].DCUChecking
          var BofaCr = results.TotalCard[0].BofaCreditCard
          var BofaChk = results.TotalCard[0].BofaCheckingAccount
          var MarriottCr = results.TotalCard[0].MarriottCreditCard
          var ChaseCr = results.TotalCard[0].ChaseCreditCard
          var DiscoverSavings = results.TotalCard[0].DiscoverSavings
          var DiscoverCr = results.TotalCard[0].DiscoverCreditCard

          this.data = [
            Citi,
            BofaCr,
            BofaChk,
            DCUChecking,
            DiscoverSavings,
            DiscoverCr,
            MarriottCr,
            ChaseCr
          ]
          this.fillData()
        })
        .catch(err => console.error(err))
    }
  },
  computed: {
    myStyles () {
      return {
        height: '40%',
        width: '10%',
        position: 'relative'
      }
    }
  }
}
</script>

<style scoped></style>
