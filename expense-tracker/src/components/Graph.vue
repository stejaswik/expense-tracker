<template>
  <div class="hello">
    <h2>MONTHLY SPENDING</h2>
    <b-table striped stacked hover :items="initData.Total" dark :fields="dataFields"></b-table>

    <div align="center">
      <b-container class="bv-example-row"></b-container>
    </div>
  </div>
</template>

<script>
// import axios to enable web service calls
import axios from 'axios'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
export default {
  name: 'TableDisplay',
  data () {
    return {
      // Table config data
      dataFields: [
        { key: 'CitiCreditCard' },
        { key: 'DCUChecking' },
        { key: 'BofaCreditCard' },
        { key: 'BofaCheckingAccount' },
        { key: 'DiscoverSavings' },
        { key: 'ChaseCreditCard' },
        { key: 'DiscoverCreditCard' },
        { key: 'MarriottCreditCard' }
      ],
      dark: this.dark,

      // API config data
      initData: [],
      description: '',
      category: 'null',
      card: 'null',
      date: '',
      price: ''
    }
  },
  mounted () {
    // This will execute when component has been loaded
    this.getTotal()

    // This will execute only when the expense has been added. CHeck emit in line 169 of TableDisplay.vue
    this.$root.$on('ExpenseAdded', () => {
      this.getTotal()
    })
  },
  methods: {
    getTotal () {
      axios
        .get('http://localhost:5000/getBankSplits')
        .then(response => {
          this.initData = response.data
        })
        .catch(err => console.error(err))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
