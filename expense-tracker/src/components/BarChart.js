import { Bar, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  extends: Bar,
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
            ticks: {
              autoSkip: true,
              maxTicksLimit: 10,
            },
          },
        ],
        yAxes: [
          {
            beginAtzero: 0,
            ticks: {
              max: 4000,
              min: 0,
              stepSize: 500,
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
