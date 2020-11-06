import { Doughnut, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  extends: Doughnut,
  mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      default: null,
    },

    options: {
      responsive: true,
      maintainAspectRatio: true,
      legend: {
        display: true,
        position: "bottom",
      },
    },
  },
  mounted() {
    this.renderChart(this.ChartData, this.options);
  },
};
