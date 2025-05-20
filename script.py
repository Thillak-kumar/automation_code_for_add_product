import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages import web_utils


def get_driver(headless=True):
    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    if headless:
        chrome_options.add_argument("--headless=new")  # Enables headless mode

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def init_env(driver):
    driver.get("https://admin-panel-production-0e0a.up.railway.app/admin")
    web_utils.wait_for_element(driver,By.CSS_SELECTOR, '[data-css="sidebar-resources"] .adminjs_Box')