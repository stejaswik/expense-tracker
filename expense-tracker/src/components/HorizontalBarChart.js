import { HorizontalBar, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  extends: HorizontalBar,
  mixins: [reactiveProp],
  props: {
    chartData: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    options: {
      responsive: true,
      maintainAspectRatio: true,

      legend: {
        display: false,
        position: "bottom",
        fontColor: "black",
      },
      title: {
        display: false,
        text: "TARGET VS ACTUAL EXPENSES",
      },
      scales: {
        xAxes: [
          {
            gridLines: {
              color: "rgba(0,0,0,0)",
            },
            beginAtzero: 0,
            ticks: {
              max: 5000,
              min: 0,
              stepSize: 1000,
            },
          },
        ],
      },
    },
  }),
  mounted() {
    this.renderChart(this.ChartData, this.options);
  },
};
