# services/analytics_engine.py

def calculate_roas(revenue, ad_spend):
    if ad_spend == 0:
        return 0
    return round(revenue / ad_spend, 2)

def revenue_growth(today, yesterday):
    if yesterday == 0:
        return 100
    return round(((today - yesterday) / yesterday) * 100, 2)

def customer_split(customers):
    new = len([c for c in customers if c['orders'] == 1])
    repeat = len([c for c in customers if c['orders'] > 1])
    return {"new": new, "repeat": repeat}