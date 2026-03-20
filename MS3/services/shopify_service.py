import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHOP_NAME = os.getenv("SHOP_NAME")
ACCESS_TOKEN = os.getenv("SHOPIFY_TOKEN")

BASE_URL = f"https://{SHOP_NAME}/admin/api/2023-10"

headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def get_orders():
    url = f"{BASE_URL}/orders.json?status=any&limit=50"
    res = requests.get(url, headers=headers)
    return res.json().get("orders", [])

def get_customers():
    url = f"{BASE_URL}/customers.json?limit=50"
    res = requests.get(url, headers=headers)
    return res.json().get("customers", [])

def get_products():
    url = f"{BASE_URL}/products.json?limit=50"
    res = requests.get(url, headers=headers)
    return res.json().get("products", [])