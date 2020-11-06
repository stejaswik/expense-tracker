<template>
  <div>
    <div>
      <b-container>
        <b-alert
          :show="dismissCountDown"
          dismissible
          fade
          variant="success"
          @dismissed="dismissCountDown = 0"
          @dismiss-count-down="countDownChanged"
        >
          <p>Expense added</p>
        </b-alert>
        <!-- <table class="col-lg-12" style="background-color:#f3f3f4"> -->
        <b-row>
          <b-form inline>
            <b-form-input
              class="mb-1 mr-sm-1 mb-sm-0"
              type="text"
              v-model="description"
              placeholder="Description"
            ></b-form-input>
            <b-form-input
              inline
              class="mb-1 mr-sm-1 mb-sm-0"
              type="text"
              v-model="price"
              placeholder="Price"
            ></b-form-input>
            <b-form-select
              inline
              class="mb-1 mr-sm-1 mb-sm-0"
              v-model="card"
              :options="crdOptions"
            ></b-form-select>
            <b-form-select
              class="mb-1 mr-sm-1 mb-sm-0"
              v-model="category"
              :options="catOptions"
              placeholder="Category"
            ></b-form-select>
          </b-form>
          <b-form>
            <b-form-datepicker
              type="text"
              v-model="date"
              id="example-datepicker"
              class="mb-1 mr-sm-1 mb-sm-0"
              placeholder="Date"
            ></b-form-datepicker>
          </b-form>
          <b-form>
            <b-button
              size="mb-1 mr-sm-1 mb-sm-0"
              type="submit"
              v-on:click="addItem()"
              variant="primary"
              @click="showAlert"
              >Submit</b-button
            >
            <b-form-checkbox v-model="dark" inline>Dark</b-form-checkbox>
          </b-form>
        </b-row>
        <!-- </table> -->
        <hr />
      </b-container>
      <b-container>
        <h4>Monthly Expense: {{ this.total }}</h4>
        <h4>Target Expense: 3600</h4>
      </b-container>
      <b-container class="tableScoped">
        <b-table
          caption-top
          bordered
          responsive
          :sticky-header="StickyHeader"
          :items="initData.Expenses"
          :dark="dark"
          :fields="dataFields"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
        >
          <!--v-for is how we loop through the response to print e recurring attribute. -->
          <!-- <b-row
            class="height"
            align-v="center"
            v-for="item in initData.Expenses"
            :key="item.id"
          >
            <b-col cols="2" class="exp-col">{{ item.description }}</b-col>
            <b-col cols="2" class="exp-col">{{ item.price }}</b-col>
            <b-col cols="3" class="exp-col">{{ item.card }}</b-col>
            <b-col cols="2" class="exp-col">{{ item.category }}</b-col>
            <b-col cols="3" class="exp-col">{{ item.date }}</b-col>
          </b-row>-->
        </b-table>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from "axios";

axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
const baseURL = "http://localhost:5000/addExpense";
export default {
  name: "TableDisplay",
  data() {
    return {
      //Table config data
      sortDesc: false,
      sortBy: "date",
      StickyHeader: "480px",
      dataFields: [
        { key: "date", sortable: true },
        { key: "description", sortable: true },
        { key: "price", sortable: true },
        { key: "category", sortable: true },
        { key: "card", sortable: true },
      ],
      dark: this.dark,
      total: 0,
      //API config data
      initData: [],
      description: "",
      category: "null",
      fail: 0,
      card: "null",
      date: "",
      price: "",
      dismissSecs: 2,
      dismissCountDown: 0,
      showDismissibleAlert: false,

      //Dropdown data
      catOptions: [
        { text: "Select One", value: null },
        "GROCERIES",
        "UTILITIES",
        "SHOPPING",
        "TRAVEL",
        "SUBSCRIPTIONS",
        "ENTERTAINMENT",
        "INCOME",
        "RESTAURANTS",
        "CREDIT CARD",
      ],
      crdOptions: [
        { text: "Select One", value: null },
        "BOFA CHECKING",
        "BOFA CREDIT CARD",
        "CITI CREDIT CARD",
        "DCU CHECKING",
        "DISOCVER SAVINGS",
        "CHASE CREDIT CARD",
        "MARRIOTT CREDIT CARD",
        "DISCOVER CREDIT CARD",
      ],
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000/getExpenses")
      .then((response) => {
        this.initData = response.data;
        this.total = response.data.Sum;
      })
      .catch((err) => console.error(err));
  },
  methods: {
    addItem() {
      axios
        .post(baseURL, {
          date: this.date,
          description: this.description,
          card: this.card,
          category: this.category,
          price: this.price,
        })
        .then((response) => {
          this.initData = response.data;
          this.$root.$emit("ExpenseAdded");
        })

        .catch((err) => console.error(err));
      this.dismissCountDown = 2;
      //this.name = "";
      this.date = "";
      this.description = "";
      this.card = "";
      this.category = "";
      this.price == "";
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tableScoped {
  background-color: white;
  margin-right: 0px;
  padding-left: 0px;
  margin-top: 0px;
  padding-right: 0px;
}
</style>
