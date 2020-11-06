import { Line, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  extends: Line,
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
              fontSize: 15,
              maxTicksLimit: 10,
            },
          },
        ],
        yAxes: [
          {
            gridLines: {
              color: "rgba(0,0,0,0)",
            },
            beginAtzero: 0,
            ticks: {
              SuggestedMax: 8000,
              fontSize: 10,
              suggestedMin: 0,
              stepSize: 500,
              autoSkip: true,
              maxTicksLimit: 8,
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
