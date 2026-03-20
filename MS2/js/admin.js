const API = "http://127.0.0.1:5000";

async function loadAdminDashboard() {

    const rev = await fetch(API + "/analytics/revenue").then(r => r.json());
    const cust = await fetch(API + "/analytics/customers").then(r => r.json());
    const trend = await fetch(API + "/analytics/revenue-trend").then(r => r.json());
    const hist = await fetch(API + "/analytics/order-distribution").then(r => r.json());
    const products = await fetch(API + "/analytics/top-products").then(r => r.json());

    // KPI
    document.getElementById("rev").innerText = rev.total_revenue;
    document.getElementById("orders").innerText = rev.orders;
    document.getElementById("customers").innerText = cust.new + cust.repeat;

    // Products
    const productList = document.getElementById("products");
    productList.innerHTML = "";

    products.forEach(p => {
        const li = document.createElement("li");
        li.innerText = `${p[0]} (${p[1]})`;
        productList.appendChild(li);
    });

    createCharts(trend, hist);
}

function createCharts(trend, hist) {

    // 🔵 LINE CHART (REAL REVENUE)
    new Chart(document.getElementById("lineChart"), {
        type: "line",
        data: {
            labels: trend.labels,
            datasets: [{
                label: "Revenue",
                data: trend.data,
                borderColor: "blue",
                tension: 0.4
            }]
        }
    });

    // 🟡 HISTOGRAM (REAL DATA)
    new Chart(document.getElementById("histChart"), {
        type: "bar",
        data: {
            labels: hist.labels,
            datasets: [{
                label: "Orders",
                data: hist.data,
                backgroundColor: "orange"
            }]
        }
    });

    // 🟢 BAR CHART (Simulated ROAS for now)
    new Chart(document.getElementById("barChart"), {
        type: "bar",
        data: {
            labels: ["Google Ads","Facebook Ads","Instagram"],
            datasets: [{
                label: "ROAS",
                data: [4.2, 3.5, 2.8],
                backgroundColor: ["green","blue","purple"]
            }]
        }
    });
}

loadAdminDashboard();