<template>
  <div class="container">
    <div>
      <h4 align="center">THIS MONTH VS PREVIOUS MONTH</h4>
      <BarChart :styles="myStyles" :chart-data="datacollection" responsive="true" />
    </div>
  </div>
</template>

<script>
import BarChart from "./BarChart.js";
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
  async mounted() {
    this.getBankSplits();

    this.$root.$on("ExpenseAdded", () => {
      this.getBankSplits();
    });
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: [
          "Entertainment",
          "Groceries",
          "Restaurants",
          "Shopping",
          "Travel",
          "Utilities",
          "Subscriptions"
        ],
        datasets: [
          {
            label: "Previous Month",
            backgroundColor: [
              "#E46651",
              "#E46651",
              "#E46651",
              "#E46651",
              "#E46651",
              "#E46651",
              "#E46651",
              "#E46651"
            ],
            borderWidth: 1,
            hoverBorderWidth: 1,
            hoverBorderColor: "#ffffff",
            data: this.PrevData
          },

          {
            label: "Current Month",
            backgroundColor: [
              "#41B883",
              "#41B883",
              "#41B883",
              "#41B883",
              "#41B883",
              "#41B883",
              "#41B883",
              "#41B883"
            ],
            borderColor: "lightpink",
            pointBackgroundColor: "blue",
            borderWidth: 1,
            hoverBorderWidth: 1,
            hoverBorderColor: "#ffffff",
            data: this.data,
            legend: {
              position: "bottom"
            }
          }
        ]
      };
    },
    getBankSplits() {
      axios
        .get("http://localhost:5000/getBankSplits")
        .then(response => {
          var results = response.data;

          this.PrevData = [
            results.PrevMonthTotal[0].EntertainmentPrev,
            results.PrevMonthTotal[0].GroceriesPrev,
            results.PrevMonthTotal[0].RestaurantsPrev,
            results.PrevMonthTotal[0].ShoppingPrev,
            results.PrevMonthTotal[0].TravelPrev,
            results.PrevMonthTotal[0].UtilitiesPrev,
            results.PrevMonthTotal[0].SubscriptionsPrev
          ];

          this.data = [
            results.TotalCategory[0].Entertainment,
            results.TotalCategory[0].Groceries,
            results.TotalCategory[0].Restaurants,
            results.TotalCategory[0].Shopping,
            results.TotalCategory[0].Travel,
            results.TotalCategory[0].Utilities,
            results.TotalCategory[0].Subscriptions
          ];
          this.fillData();
        })
        .catch(err => console.error(err));
    }
  },
  computed: {
    myStyles() {
      return {
        height: "40%",
        width: "90%",
        position: "relative"
      };
    }
  }
};
</script>

<style scoped></style>
