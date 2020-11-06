<template>
  <div class="container">
    <h4 align="center">ENTERTAINMENT</h4>
    <div>
      <BarChart :styles="myStyles" :chart-data="datacollection" />
    </div>
  </div>
</template>

<script>
import BarChart from "./LineChart.js";
import axios from "axios";

export default {
  components: {
    BarChart
  },
  data() {
    return {
      datacollection: null,
      loaded: false,
      data: []
    };
  },
  mounted() {
    this.getBankSplits();

    this.$root.$on("ExpenseAdded", () => {
      this.getBankSplits();
    });
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.labels,
        datasets: [
          {
            borderWidth: 3,
            data: this.data,
            barThickness: 25,
            backgroundColor: "rgba(255, 255, 255, 0.8)",
            opacity: 1,
            borderColor: "green",
            lineTension: 0
          }
        ]
      };
    },
    getBankSplits() {
      axios
        .get("http://localhost:5000/getSum")
        .then(response => {
          var results = response.data;
          var monthsData = results.AllEntertainmentTotal;
          console.log(monthsData);
          // this.data = [results.AllMonthTotal.length, 36];
          var lab = [];
          var out = [];
          for (var i = 0; i < monthsData.length; i++) {
            lab.push(monthsData[i].month);
            out.push(monthsData[i].total);
          }

          this.labels = lab;
          this.data = out;
          this.fillData();
        })
        .catch(err => console.error(err));
    }
  },
  computed: {
    myStyles() {
      return {
        height: "60%",
        width: "85%",
        position: "relative"
      };
    }
  }
};
</script>

<style scoped></style>
