import requests
import pandas as pd
url = "https://helmboots.com/products.json"
r = requests.get(url)
data = r.json()
products = []
for product in data["products"]:
    item = {
        "title": product["title"],
        "id": product["id"],
        "handle": product["handle"],
        "vendor": product["vendor"],
        "type": product["product_type"],
        "creation_date": product["created_at"],
        "availability": product["variants"][0]["available"],
        "sku": product["variants"][0]["sku"],
        "price": product["variants"][0]["price"],
        "original_price": product["variants"][0]["compare_at_price"],

    }
    try:
        img = product["images"][0]["src"]
    except:
        img = "None"
    products.append(item)
    item["img"] = img
df = pd.DataFrame(products)
df.to_csv("products.csv", index=False)