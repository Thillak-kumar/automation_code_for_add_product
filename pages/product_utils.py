import time

from selenium.webdriver.common.by import By

from pages import web_utils

from selenium.webdriver.support.ui import Select


def click_on_test(driver):
    test_el = driver.find_elements(By.CSS_SELECTOR, '[data-css="sidebar-resources"] .adminjs_Box')[1]
    web_utils.js_click(driver, test_el)
    time.sleep(3)


def click_on_product(driver):
    product_el = driver.find_element(By.CSS_SELECTOR, 'a[href="/admin/resources/Product"]')
    web_utils.js_click(driver, product_el)
    web_utils.wait_for_element(driver, By.CSS_SELECTOR, '[data-css="Product-list-breadcrumbs"]')


def click_on_new_button(driver):
    new_btn_el = driver.find_element(By.CSS_SELECTOR, 'a[data-css="Product-new-button"]')
    web_utils.js_click(driver, new_btn_el)
    web_utils.wait_for_element(driver, By.CSS_SELECTOR, '[data-css="Product-new-action-header"]')


def add_product_name(driver, name):
    name_field_el = driver.find_element(By.CSS_SELECTOR, '[data-testid="property-edit-name"] input[name="name"]')
    name_field_el.send_keys(name)


def add_product_image(driver, image):
    image_field_el = driver.find_element(By.CSS_SELECTOR, '[data-testid="property-edit-image"] input[name="image"]')
    image_field_el.send_keys(image)


def add_price(driver, price):
    price_field_el = driver.find_element(By.CSS_SELECTOR, '[data-testid="property-edit-price"] input[name="price"]')
    price_field_el.send_keys(price)


def add_discount_price(driver, discount_price):
    discount_price_field_el = driver.find_element(By.CSS_SELECTOR,
                                                  '[data-testid="property-edit-discountPrice"] input[name="discountPrice"]')
    discount_price_field_el.send_keys(discount_price)


def add_quantity(driver, quantity):
    quantity_el = driver.find_element(By.CSS_SELECTOR, '[data-testid="property-edit-quantity"] input[name="quantity"]')
    quantity_el.send_keys(quantity)


def add_category(driver, category):
    # 1. Click the input to open the dropdown
    category_el = driver.find_element(By.CSS_SELECTOR, '[data-css="Product-edit-category"] input')
    category_el.click()
    time.sleep(5)
    # 2. Wait for dropdown options to appear
    web_utils.wait_for_element(driver, By.CSS_SELECTOR, '[data-css="Product-edit-category"] [role="listbox"]')

    # 3. Find the correct option by visible text
    options = driver.find_elements(By.CSS_SELECTOR, '[data-css="Product-edit-category"] [role="option"]')

    for option in options:
        if option.text.strip() == category:
            option.click()
            break
    else:
        raise Exception(f'Category "{category}" not found in dropdown!')


def add_stock(driver, stock):
    stock_el = driver.find_element(By.CSS_SELECTOR, 'input#stock')
    stock_el.send_keys(stock)


def click_on_save(driver):
    save_el = driver.find_element(By.CSS_SELECTOR, '[data-css="Product-new"] [data-testid="button-save"]')
    web_utils.js_click(driver, save_el)
    web_utils.wait_for_element_to_disappear(driver, By.CSS_SELECTOR,
                                            '[data-css="Product-new"] [data-testid="button-save"]')


def click_on_present_in_cart(driver):
    present_in_cart_el = driver.find_element(By.CSS_SELECTOR, "input#isPresentInCart")
    web_utils.js_click(driver, present_in_cart_el)
    time.sleep(2)


def add_quantity_in_cart(driver, quantity):
    quantity_el = driver.find_element(By.CSS_SELECTOR, 'input#quantityInCart')
    quantity_el.send_keys(quantity)

def click_on_present_in_wishlist(driver):
    present_in_wishlist_el = driver.find_element(By.CSS_SELECTOR, "input#isPresentInWishList")
    web_utils.js_click(driver, present_in_wishlist_el)
    time.sleep(2)

def add_product_to_db(driver, name, image, price, discount_price, quantity, stock, category, is_present_in_cart,
                      is_present_in_wishlist,quantity_in_cart):
    click_on_new_button(driver)
    add_product_name(driver, name)
    add_product_image(driver, image)
    add_price(driver, price)
    add_discount_price(driver, discount_price)
    add_quantity(driver, quantity)
    add_stock(driver, stock)
    add_category(driver, category)
    if is_present_in_cart:
        click_on_present_in_cart(driver)
    if is_present_in_wishlist:
        click_on_present_in_wishlist(driver)
    add_quantity_in_cart(driver, quantity_in_cart)
    click_on_save(driver)
    time.sleep(3)
