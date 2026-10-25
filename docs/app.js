/**
 * RISK Master Analytics Suite — Executive Web Application Logic
 * Implements interactive tab switching, dynamic Chart.js visualizations,
 * and a real-time What-If scenario financial simulator.
 */

document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initCharts();
  initSimulator();
});

// ==============================================================================
// 1. TAB SWITCHING LOGIC
// ==============================================================================
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-tab");

      tabBtns.forEach(b => b.classList.remove("active"));
      tabPanes.forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.classList.add("active");
      }
    });
  });
}

// ==============================================================================
// 2. CHART.JS INTERACTIVE VISUALIZATIONS
// ==============================================================================
function initCharts() {
  if (typeof Chart === "undefined") {
    console.warn("Chart.js not loaded.");
    return;
  }

  // --- Chart 1: Superstore Monthly Trajectory (Dual Axis) ---
  const ctxSuperMonthly = document.getElementById("chartSuperMonthly");
  if (ctxSuperMonthly) {
    const months = [
      "2014-01", "2014-04", "2014-08", "2014-11", "2014-12",
      "2015-01", "2015-04", "2015-08", "2015-11", "2015-12",
      "2016-01", "2016-04", "2016-08", "2016-11", "2016-12",
      "2017-01", "2017-04", "2017-08", "2017-11", "2017-12"
    ];
    const sales = [
      14236, 28295, 27909, 78628, 69545,
      18174, 34195, 36898, 75972, 74919,
      18542, 38750, 31631, 79411, 96999,
      43971, 36521, 63120, 118447, 83829
    ];
    const profits = [
      2450, 3487, 5318, 9292, 8983,
      -3281, 4187, 5300, 4011, 8011,
      2824, 2977, 2062, 4011, 17885,
      7140, 933, 9040, 9605, 8483
    ];

    new Chart(ctxSuperMonthly, {
      type: "bar",
      data: {
        labels: months,
        datasets: [
          {
            type: "line",
            label: "Net Profit ($)",
            data: profits,
            borderColor: "#059669",
            backgroundColor: "#059669",
            borderWidth: 2.5,
            yAxisID: "y1",
            tension: 0.3
          },
          {
            type: "bar",
            label: "Sales ($)",
            data: sales,
            backgroundColor: "rgba(37, 99, 235, 0.65)",
            borderColor: "#2563EB",
            borderWidth: 1,
            yAxisID: "y"
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            type: "linear",
            display: true,
            position: "left",
            ticks: { callback: v => "$" + (v / 1000) + "k" }
          },
          y1: {
            type: "linear",
            display: true,
            position: "right",
            grid: { drawOnChartArea: false },
            ticks: { callback: v => "$" + (v / 1000) + "k" }
          }
        }
      }
    });
  }

  // --- Chart 2: Sub-Category Profit Ranking ---
  const ctxSubCat = document.getElementById("chartSubCat");
  if (ctxSubCat) {
    const subcats = [
      "Copiers", "Phones", "Accessories", "Paper", "Binders", "Chairs",
      "Storage", "Appliances", "Furnishings", "Envelopes", "Art",
      "Labels", "Machines", "Fasteners", "Supplies", "Bookcases", "Tables"
    ];
    const subProfits = [
      55618, 44516, 41937, 34054, 30222, 26590,
      21279, 18138, 13059, 6964, 6528,
      5546, 3385, 950, -1189, -3473, -17725
    ];
    const colors = subProfits.map(p => p >= 0 ? "#059669" : "#DC2626");

    new Chart(ctxSubCat, {
      type: "bar",
      data: {
        labels: subcats,
        datasets: [{
          label: "Net Profit ($)",
          data: subProfits,
          backgroundColor: colors,
          borderRadius: 4
        }]
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { ticks: { callback: v => "$" + (v / 1000) + "k" } }
        }
      }
    });
  }

  // --- Chart 3: Telco Tenure Cohort Retention Curves ---
  const ctxCohort = document.getElementById("chartCohort");
  if (ctxCohort) {
    const cohorts = ["0–12m", "13–24m", "25–36m", "37–48m", "49–60m", "61–72m"];
    const retentionRates = [52.6, 71.3, 77.6, 81.3, 89.9, 93.4];
    const churnRates = [47.4, 28.7, 22.4, 18.7, 10.1, 6.6];

    new Chart(ctxCohort, {
      type: "line",
      data: {
        labels: cohorts,
        datasets: [
          {
            label: "Retention Rate %",
            data: retentionRates,
            borderColor: "#059669",
            backgroundColor: "rgba(5, 150, 105, 0.1)",
            fill: true,
            borderWidth: 2.5,
            tension: 0.2
          },
          {
            label: "Churn Rate %",
            data: churnRates,
            borderColor: "#DC2626",
            backgroundColor: "transparent",
            borderDash: [5, 5],
            borderWidth: 2.5,
            tension: 0.2
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: { min: 0, max: 100, ticks: { callback: v => v + "%" } }
        }
      }
    });
  }

  // --- Chart 4: Corporate Financial Waterfall ---
  const ctxWaterfall = document.getElementById("chartWaterfall");
  if (ctxWaterfall) {
    new Chart(ctxWaterfall, {
      type: "bar",
      data: {
        labels: ["1. Gross Sales", "2. Discounts", "3. Net Sales", "4. COGS", "5. Operating Profit"],
        datasets: [{
          label: "$ Millions",
          data: [127.93, -9.21, 118.73, -101.83, 16.89],
          backgroundColor: ["#2563EB", "#DC2626", "#1E40AF", "#DC2626", "#059669"],
          borderRadius: 4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: { ticks: { callback: v => "$" + v + "M" } }
        }
      }
    });
  }
}

// ==============================================================================
// 3. REAL-TIME WHAT-IF FINANCIAL SIMULATOR
// ==============================================================================
function initSimulator() {
  const discountSlider = document.getElementById("sliderDiscount");
  const cogsSlider = document.getElementById("sliderCogs");

  const valDiscount = document.getElementById("valDiscount");
  const valCogs = document.getElementById("valCogs");

  const simNetSalesEl = document.getElementById("simNetSales");
  const simProfitEl = document.getElementById("simProfit");
  const simMarginEl = document.getElementById("simMargin");
  const simDeltaEl = document.getElementById("simDelta");

  const baseGross = 127931598.50;
  const baseDiscounts = 9205248.24;
  const baseCogs = 101832648.00;
  const baseProfit = 16893702.25;

  function updateSimulation() {
    if (!discountSlider || !cogsSlider) return;

    const discShift = parseFloat(discountSlider.value) / 100.0;
    const cogsShift = parseFloat(cogsSlider.value) / 100.0;

    valDiscount.textContent = (discShift >= 0 ? "+" : "") + (discShift * 100).toFixed(0) + "%";
    valCogs.textContent = (cogsShift >= 0 ? "+" : "") + (cogsShift * 100).toFixed(0) + "%";

    const simDiscounts = baseDiscounts * (1.0 + discShift);
    const simNetSales = baseGross - simDiscounts;
    const simCogs = baseCogs * (1.0 + cogsShift);
    const simProfit = simNetSales - simCogs;
    const simMargin = (simProfit / simNetSales) * 100.0;
    const deltaProfit = simProfit - baseProfit;

    simNetSalesEl.textContent = "$" + (simNetSales / 1e6).toFixed(2) + "M";
    simProfitEl.textContent = "$" + (simProfit / 1e6).toFixed(2) + "M";
    simMarginEl.textContent = simMargin.toFixed(2) + "%";

    if (deltaProfit >= 0) {
      simDeltaEl.textContent = "+$" + (deltaProfit / 1e6).toFixed(2) + "M vs Baseline";
      simDeltaEl.className = "metric-sub";
    } else {
      simDeltaEl.textContent = "-$" + (Math.abs(deltaProfit) / 1e6).toFixed(2) + "M vs Baseline";
      simDeltaEl.className = "metric-sub danger";
    }
  }

  if (discountSlider && cogsSlider) {
    discountSlider.addEventListener("input", updateSimulation);
    cogsSlider.addEventListener("input", updateSimulation);
    updateSimulation();
  }
}
