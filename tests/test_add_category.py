import pytest
from script import get_driver, init_env
from pages.category_utils import add_category_to_db
class TestAddCategory:

    def test_add_categories(self):
        driver = get_driver()
        init_env(driver)
        # input should be like this
        # category name , image
        category_lst=[
            ["platinum","https://cdn.britannica.com/28/141028-050-5ECC6A2B/one-unreactive-elements.jpg"],
            ["iron", "https://5.imimg.com/data5/KX/RC/MY-3834000/iron-rod.jpg"],
        ]

        add_category_to_db(driver, category_lst)
