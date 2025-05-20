import time

from selenium.webdriver.common.by import By

from pages import web_utils

def click_on_test(driver):
    test_el = driver.find_elements(By.CSS_SELECTOR, '[data-css="sidebar-resources"] .adminjs_Box')[1]
    web_utils.js_click(driver, test_el)
    time.sleep(3)

def click_on_category(driver):
    category_el = driver.find_element(By.CSS_SELECTOR, 'a[href="/admin/resources/Category"]')
    web_utils.js_click(driver, category_el)
    web_utils.wait_for_element(driver, By.CSS_SELECTOR, '[data-css="Category-list-table-wrapper"]')

def click_on_new_button(driver):
    new_btn_el = driver.find_element(By.CSS_SELECTOR, 'a[data-css="Category-new-button"]')
    web_utils.js_click(driver, new_btn_el)
    web_utils.wait_for_element(driver, By.CSS_SELECTOR, '[data-css="Category-new-form"]')

def add_category_name(driver, name):
    name_el = driver.find_element(By.CSS_SELECTOR,"input#name")
    name_el.click()
    web_utils.clear_text_field(name_el)
    name_el.send_keys(name)

def add_category_image(driver,image_link):
    image_el = driver.find_element(By.CSS_SELECTOR,"input#image")
    image_el.click()
    web_utils.clear_text_field(image_el)
    image_el.send_keys(image_link)

def click_on_save(driver):
    save_el = driver.find_element(By.CSS_SELECTOR, '[data-css="Category-new-drawer-footer"] [data-testid="button-save"]')
    web_utils.actions_click(driver, save_el)
    web_utils.wait_for_element_to_disappear(driver, By.CSS_SELECTOR,
                                            '[data-css="Category-new-drawer-footer"] [data-testid="button-save"]')

def add_category_to_db(driver,category_lst):
    click_on_test(driver)
    click_on_category(driver)
    for category in category_lst:
        click_on_new_button(driver)
        category_name = category[0]
        category_image_link = category[1]
        add_category_name(driver, category_name)
        add_category_image(driver, category_image_link)
        click_on_save(driver)
