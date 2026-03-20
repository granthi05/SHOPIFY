from flask import Blueprint, jsonify
from services.shopify_service import get_orders, get_customers, get_products
from collections import defaultdict
from datetime import datetime

analytics_bp = Blueprint("analytics", __name__)

# 🔹 Revenue + Orders
@analytics_bp.route("/revenue")
def revenue():
    orders = get_orders()

    total_revenue = sum(float(o["total_price"]) for o in orders)

    return jsonify({
        "total_revenue": round(total_revenue, 2),
        "orders": len(orders)
    })


# 🔹 Revenue Trend (Line Chart)
@analytics_bp.route("/revenue-trend")
def revenue_trend():
    orders = get_orders()

    daily = defaultdict(float)

    for o in orders:
        date = o["created_at"][:10]
        daily[date] += float(o["total_price"])

    sorted_data = sorted(daily.items())

    return jsonify({
        "labels": [d[0] for d in sorted_data],
        "data": [round(d[1], 2) for d in sorted_data]
    })


# 🔹 Histogram (Order Value Distribution)
@analytics_bp.route("/order-distribution")
def order_distribution():
    orders = get_orders()

    buckets = {
        "0-500": 0,
        "500-1000": 0,
        "1000-2000": 0,
        "2000+": 0
    }

    for o in orders:
        val = float(o["total_price"])

        if val <= 500:
            buckets["0-500"] += 1
        elif val <= 1000:
            buckets["500-1000"] += 1
        elif val <= 2000:
            buckets["1000-2000"] += 1
        else:
            buckets["2000+"] += 1

    return jsonify({
        "labels": list(buckets.keys()),
        "data": list(buckets.values())
    })


# 🔹 Customers
@analytics_bp.route("/customers")
def customers():
    customers = get_customers()

    new = 0
    repeat = 0

    for c in customers:
        if c["orders_count"] == 1:
            new += 1
        else:
            repeat += 1

    return jsonify({
        "new": new,
        "repeat": repeat
    })


# 🔹 Top Products
@analytics_bp.route("/top-products")
def top_products():
    orders = get_orders()

    product_sales = defaultdict(int)

    for o in orders:
        for item in o["line_items"]:
            product_sales[item["title"]] += item["quantity"]

    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    return jsonify(sorted_products[:5])