<template id="template">
  <div id="app" class="main">
    <h1 align="center">MONTHLY EXPENSES</h1>
    <div id="toggle">
      <label for="toggle_button">
        <span>Previous Month</span>
        <input type="checkbox" id="toggle_button" />
      </label>
    </div>
    <div class="row">
      <!--Left side-->
      <TableDisplay aign="center" class="tableDisplay" />
    </div>

    <div class="row">
      <AllMonthsData class="col-sm-3 graph2" />
      <!-- <MonthTotal class="graph2 col-md-3" /> -->
      <PrevMonthTotal class="graph2 col-sm-3" />
      <GraphSample class="graph col-sm-3" />
      <AllCreditCardData class="graph col-sm-3" />
    </div>
    <div class="row">
      <!-- <AllRestaurantsData class="graph2 col-sm-3" /> -->
      <!-- <AllEntertainmentData class="graph2 col-sm-3" /> -->
    </div>
    <div class="row">
      <!-- <AllGroceriesData class="graph2 col-sm-3" /> -->
      <!--AllShoppingData class="graph2 col-sm-3" /-->
    </div>

    <!-- <div class="row">
      <AllUtilitiesData class="col-sm-3 graph2" />
      <AllTravelData class="graph2 col-sm-3" />
      <AllSubscriptionsData class="graph2 col-sm-3" />
    </div>-->
  </div>
</template>

<script>
import TableDisplay from './components/TableDisplay.vue'
import GraphSample from './components/GraphSample.vue'
import AllCreditCardData from './components/AllCreditCardData.vue'
// import MonthTotal from "./components/MonthTotal.vue";
import PrevMonthTotal from './components/PrevMonthTotal.vue'
import AllMonthsData from './components/AllMonthsData.vue'
// import AllUtilitiesData from "./components/AllUtilitiesData.vue";
// import AllSubscriptionsData from "./components/AllSubscriptionsData.vue";
// import AllRestaurantsData from "./components/AllRestaurantsData.vue";
// import AllGroceriesData from "./components/AllGroceriesData.vue";
// import AllShoppingData from "./components/AllShoppingData.vue";
// import AllTravelData from "./components/AllTravelData.vue";
// import AllEntertainmentData from "./components/AllEntertainmentData.vue";
export default {
  name: 'App',
  components: {
    TableDisplay,
    AllCreditCardData,
    GraphSample,
    // MonthTotal,
    PrevMonthTotal,
    AllMonthsData
    // AllUtilitiesData,
    // AllSubscriptionsData,
    // AllRestaurantsData,
    // AllGroceriesData
    // AllShoppingData,
    // AllTravelData,
    // AllEntertainmentData
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#toggle {
  text-align: center;
}
.tableDisplay {
  margin-top: 10px;
  margin: auto;
  background-color: #ffffff;
}

.area {
  background-color: #f5f5f5;
}
.graph {
  z-index: 1;
  position: relative;
  border: 1px solid #ffffff;
  background-color: #f5f5f5;
  background-color: #f5f5f5;
  padding-top: 0px;
  margin-top: 10px;
  margin-left: 10px;
  overflow: hidden;
  padding: 0px;
  margin-bottom: 0px;
  padding-bottom: 0px;
}

.graph2 {
  z-index: 1;
  position: relative;
  background-color: #f5f5f5;
  padding-top: 10px;
  margin-top: 10px;
  margin-left: 10px;
  overflow: hidden;
  padding: 00px;
  margin-bottom: 0px;
  padding-bottom: 0px;
}

.left {
  left: 0;
}

h1 {
  background-color: #e64a19;
}

.right {
  right: 0;
}
</style>
