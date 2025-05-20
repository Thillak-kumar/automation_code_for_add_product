import json
import time
import pytest

from pages.product_utils import add_product_to_db
from script import get_driver,init_env

class TestAddProductsFromJson:
    def test_add_products(self):
        # Initialize driver
        driver = get_driver()
        init_env(driver)

        # Load JSON file to add the products for fruits category
        with open(r'C:\Users\thill\Downloads\final_fruits_products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)

        for product in products:
            name = product["name"]
            image = product["image_url"]
            price = product["price_mrp"]
            discount_price = product["price_sale"]
            quantity = product["unit"]
            category = "Fruits"

            print(f"Adding product: {name}")

            # Call your method
            add_product_to_db(
                driver,
                name=name,
                image=image,
                price=price,
                discount_price=discount_price,
                quantity=quantity,
                category=category
            )

            time.sleep(2)  # Small delay between products to avoid server overload
        driver.quit()
