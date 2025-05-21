import json
import time
import pytest

from pages.product_utils import add_product_to_db,click_on_test,click_on_product
from script import get_driver,init_env
import pandas as pd

class TestAddProductsFromJson:
    def test_add_products(self):
        # Initialize driver
        driver = get_driver()
        init_env(driver)

        # Load JSON file to add the products for fruits category
        df = pd.read_excel(r"C:\Users\thill\Downloads\products_by_categories.xlsx")

        # Iterate through each row (product)
        for index, product in df.iterrows():
            name = product["productName"]
            image = product["image"]
            price = product["price"]
            discount_price = product["discountPrice"]
            quantity = product["quantity"]
            category = product["category"]
            stock = product["Stock"]
            present_in_cart = product["isPresentInCart"]
            quantity_in_cart = product["QuantityInCart"]
            present_in_wishlist = product["isPresentInWishlist"]

            print(f"Adding product: {name}")
            click_on_test(driver)
            click_on_product(driver)
            # Call your method
            add_product_to_db(
                driver,
                name=name,
                image=image,
                price=price,
                discount_price=discount_price,
                quantity=quantity,
                stock=stock,
                category=category,
                is_present_in_cart=present_in_cart,
                is_present_in_wishlist=present_in_wishlist,
                quantity_in_cart=quantity_in_cart
            )

            time.sleep(2)  # Small delay between products to avoid server overload
        driver.quit()
