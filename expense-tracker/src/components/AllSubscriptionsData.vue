<template>
  <div class="container">
    <h4 align="center">SUBSCRIPTIONS</h4>
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
      SubscriptionsData: []
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
            data: this.SubscriptionsData,
            barThickness: 25,
            backgroundColor: "rgba(255, 255, 255, 0.8)",
            opacity: 1,
            borderColor: "#444fff",
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
          var SubscriptionsMonthsData = results.AllSubscriptionsTotal;
          var lab = [];
          var out = [];
          for (var i = 0; i < SubscriptionsMonthsData.length; i++) {
            lab.push(SubscriptionsMonthsData[i].month);
            out.push(SubscriptionsMonthsData[i].total);
          }

          this.labels = lab;
          this.SubscriptionsData = out;
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
