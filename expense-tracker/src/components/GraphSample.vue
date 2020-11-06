<template>
  <div class="container">
    <h2 align="center">SPLIT BY CARDS</h2>
    <div>
      <BarChart :styles="myStyles" :chartData="datacollection" />
    </div>
  </div>
</template>

<script>
import BarChart from "./BarChart.js";

import axios from "axios";

export default {
  components: {
    //Get the pieChart component
    BarChart,
  },
  data() {
    return {
      datacollection: null,
      loaded: false,
      data: [],
    };
  },
  //Define functions that run on refresh/load
  mounted() {
    this.getBankSplits();

    this.$root.$on("ExpenseAdded", () => {
      this.getBankSplits();
    });
  },
  //Define methods
  methods: {
    fillData() {
      this.datacollection = {
        labels: [
          "Citi Credit Card",
          "Bofa Credit Card",
          "Bofa Checking Account",
          "DCU Checking",
          "Discover Savings",
          "Discover Credit Card",
          "Marriott Credit Card",
          "Chase Credit Card",
        ],
        datasets: [
          {
            backgroundColor: [
              "#41B883",
              "#E46651",
              "#00D8FF",
              "#E0D8FF",
              "#4068FF",
              "#E1D800",
              "#00FF00",
              "#00FFFF",
            ],
            borderColor: "lightpink",
            pointBackgroundColor: "blue",
            borderWidth: 1,
            data: this.data,
          },
        ],
      };
    },
    getBankSplits() {
      axios
        //call the method getBankSplits
        .get("http://localhost:5000/getBankSplits")
        .then((response) => {
          //once the response is received, parse the data.
          var results = response.data;
          var Citi = results.TotalCard[0].CitiCreditCard;
          var DCUChecking = results.TotalCard[0].DCUChecking;
          var BofaCr = results.TotalCard[0].BofaCreditCard;
          var BofaChk = results.TotalCard[0].BofaCheckingAccount;
          var MarriottCr = results.TotalCard[0].MarriottCreditCard;
          var ChaseCr = results.TotalCard[0].ChaseCreditCard;
          var DiscoverSavings = results.TotalCard[0].DiscoverSavings;
          var DiscoverCr = results.TotalCard[0].DiscoverCreditCard;

          //Setup graph data
          this.data = [
            Citi,
            BofaCr,
            BofaChk,
            DCUChecking,
            DiscoverSavings,
            DiscoverCr,
            MarriottCr,
            ChaseCr,
          ];
          this.fillData();
        })
        .catch((err) => console.error(err));
    },
  },
  computed: {
    myStyles() {
      return {
        height: "40%",
        width: "99%",
        position: "relative",
      };
    },
  },
};
</script>

<style scoped></style>
