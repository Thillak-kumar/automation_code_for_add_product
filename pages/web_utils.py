import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ElementNotFound(Exception):
    pass


def find_element_from_lst_by_txt(elements, text):
    text = text.strip().lower()
    for el in elements:
        if el.text.strip().lower() == text:
            return el
        time.sleep(0.5)
    raise ElementNotFound(f'Element with text: "{text}" not found')


def find_element_from_lst_start_with_txt(elements, text):
    text = text.lstrip().lower()
    for el in elements:
        if el.text.lstrip().lower().startswith(text):
            return el
    raise ElementNotFound(f'Element that start with text: "{text}" not found')


def find_elements_from_lst_start_with_txt(elements, text):
    text = text.lstrip().lower()
    el_lst = []
    for el in elements:
        if el.text.lstrip().lower().startswith(text):
            el_lst.append(el)
    if len(el_lst) == 0:
        raise ElementNotFound(f'Element with text: "{text}" not found')
    return el_lst


def find_element_from_lst_ends_with_txt(elements, text):
    """
    :param elements: element list
    :param text: text to search
    :return: element that contain text in end of its text
    """
    text = text.lstrip().lower()
    for el in elements:
        if el.text.lstrip().lower().endswith(text):
            return el
    raise ElementNotFound(f'Element that ends with text: "{text}" not found')


def find_element_from_lst_in_txt(elements, text):
    text = text.strip().lower()
    for el in elements:
        if text in el.text.strip().lower():
            return el
    raise ElementNotFound(f'Element with text: "{text}" not found')


def wait_for_element(driver, by, element_to_wait, timeout=10):
    condition = EC.presence_of_element_located((by, element_to_wait))
    WebDriverWait(driver, timeout).until(condition)


def click_and_wait(driver, element_to_click, by, element_to_wait, timeout=20):
    element_to_click.click()
    wait_for_element(driver, by, element_to_wait, timeout)


def wait_for_element_to_disappear(driver, by, element_to_wait, timeout=10):
    condition = EC.presence_of_element_located((by, element_to_wait))
    WebDriverWait(driver, timeout, 1).until_not(condition)


def wait_for_element_to_hide(driver, element_to_wait, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element(element_to_wait)
    )


def click_and_wait_to_disappear(driver, element_to_click, by, element_to_wait, timeout=20):
    element_to_click.click()
    wait_for_element_to_disappear(driver, by, element_to_wait, timeout)


def click_all_elements(element_el_lst):
    for element in element_el_lst:
        element.click()


def actions_click(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    action.click(element)
    action.perform()


def js_scroll_and_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click()", element)


def js_scroll_and_actions_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    action = ActionChains(driver)
    action.click(element)
    action.perform()


def js_scroll_and_move_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    action = ActionChains(driver)
    action.move_to_element(element).perform()


def move_to_element(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element).perform()


def js_click(driver, element):
    driver.execute_script("arguments[0].click()", element)


def upload_file(file_input_el, relative_file_path, client_resources):
    upload_file_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."
                                                     , 'resources', client_resources, relative_file_path))
    file_input_el.send_keys(upload_file_path)


def upload_path(file_input_el, relative_path, client_resources):
    upload_full_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."
                                                     , 'resources', client_resources, relative_path))

    for item in os.listdir(upload_full_path):
        item_path = os.path.join(upload_full_path, item)
        if os.path.isfile(item_path):  # Check if it's a file
            file_input_el.send_keys(item_path)
            time.sleep(1)


def wait_and_upload_path(driver, file_input_el, relative_path, client_resources):
    upload_full_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."
                                                     , 'resources', client_resources, relative_path))

    for item in os.listdir(upload_full_path):
        item_path = os.path.join(upload_full_path, item)
        if os.path.isfile(item_path):  # Check if it's a file
            file_input_el.send_keys(item_path)
        wait_for_element(driver, By.CSS_SELECTOR, '.dialog-panel .drop-zone-input')


def get_parent(child_el, depth=1):
    """
    :param child_el: element
    :param depth: how many step up the html tree to move
    :return: ancestor depth level upward
    """
    return child_el.find_element(By.XPATH, '/'.join([".."] * depth))


def get_table_cell(table_wrapper_el, row_num, col_num):
    """
    :param table_wrapper_el: an element that wrap the table or the table itself
    :param row_num: row number
    :param col_num: col number
    :return:a cell
    """
    row_el_lst = table_wrapper_el.find_elements(By.TAG_NAME, "tr")
    col_el_lst = row_el_lst[row_num].find_elements(By.CSS_SELECTOR, "td,th")
    return col_el_lst[col_num]


def get_text_from_element_array(element_el_lst):
    """
    :param element_el_lst: list of elements
    :return: list of elements text
    """
    return [el.text.strip() for el in element_el_lst]


def get_attribute_from_element_array(element_el_lst, attribute_name):
    """
    :param element_el_lst: list of elements
    :return: list of elements text
    """
    return [el.text.strip() for el in element_el_lst]


def filter_element_from_lst_ends_with_txt(elements, text):
    """
    :param elements: element list
    :param text: text to search
    :return: element that contain text in end of its text
    """
    text = text.lstrip().lower()
    el_lst = []
    for el in elements:
        if el.text.lstrip().lower().endswith(text):
            el_lst.append(el)
    if not el_lst:
        raise ElementNotFound(f'Element that ends with text: "{text}" not found')
    return el_lst


def does_element_exist(driver, attribute, text):
    try:
        driver.find_element(attribute, text)
    except NoSuchElementException:
        return False
    return True


def click_out_of_popup(driver, attribute):
    """when can't click escape to close popup"""
    other_el = driver.find_element(By.CLASS_NAME, attribute)
    # close_checks_el.click()
    action = ActionChains(driver)
    action.move_to_element(other_el)
    action.click()
    action.perform()


def select_filter_by_outcome(driver, attribute, text):
    checks_drop_down_el_lst = driver.find_elements(By.CLASS_NAME, attribute)
    click_resolution_el = find_element_from_lst_by_txt(checks_drop_down_el_lst, text)
    click_resolution_el.click()


def select_filter_by_status(driver, attribute, text):
    file_status_el_lst = driver.find_elements(By.CSS_SELECTOR, attribute)
    resolved_btn_el = find_element_from_lst_by_txt(file_status_el_lst, text)
    resolved_btn_el.click()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


def click_menu_button(test, attribute):
    """menu button from new discrepancy page"""
    menu_el_lst = test.find_elements(By.CSS_SELECTOR, attribute)
    menu_el_lst[0].click()
    time.sleep(3)


def click_child_that_start_with_txt(driver, selector, text):
    mark_text_el_lst = driver.find_elements(By.CSS_SELECTOR, selector)
    click_mark_discrepancy_el = find_element_from_lst_start_with_txt(mark_text_el_lst, text)
    click_mark_discrepancy_el.click()


def click_child_with_txt(driver, selector, text):
    mark_text_el_lst = driver.find_elements(By.CSS_SELECTOR, selector)
    click_mark_discrepancy_el = find_element_from_lst_by_txt(mark_text_el_lst, text)
    click_mark_discrepancy_el.click()


# def select_check_tab(driver, element, text):
#     checks_tab_el_lst = driver.find_elements(By.CSS_SELECTOR, element)
#     select_tab_el = find_element_from_lst_by_txt(checks_tab_el_lst, text)
#     select_tab_el.click()

def find_member_of_group_by_group_title_text(driver, title_selector, title_text, member_selector, member_text,
                                             depth: int = 1):
    title_el_lst = driver.find_elements(By.CSS_SELECTOR, title_selector)
    title_el = find_element_from_lst_start_with_txt(title_el_lst, title_text)
    parent_el = get_parent(title_el, depth)
    member_el_lst = parent_el.find_elements(By.CSS_SELECTOR, member_selector)
    member_el = find_element_from_lst_start_with_txt(member_el_lst, member_text)
    return member_el


def find_members_of_group_by_group_title_text(driver, title_selector, title_text, member_selector, depth: int = 1):
    title_el_lst = driver.find_elements(By.CSS_SELECTOR, title_selector)
    title_el = find_element_from_lst_in_txt(title_el_lst, title_text)
    parent_el = get_parent(title_el, depth)
    member_el_lst = parent_el.find_elements(By.CSS_SELECTOR, member_selector)
    return member_el_lst


def assert_url_to_have(driver, part_of_url):
    assert part_of_url in driver.current_url, f"{part_of_url} is not found in {driver.current_url}"


def press_up_arrow(driver):
    ActionChains(driver).send_keys(Keys.ARROW_UP).perform()


def press_down_arrow(driver):
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()


def press_ctrl(driver):
    ActionChains(driver).key_down(Keys.CONTROL).perform()


def release_ctrl(driver):
    ActionChains(driver).key_up(Keys.CONTROL).perform()


def get_lot_cell(driver, index_column, cell_value_column):
    scroll_el = driver.find_elements(By.CSS_SELECTOR, '.table-visualization-container .cdk-virtual-scroll-viewport')
    driver.execute_script("arguments[0].scrollLeft = 0;", scroll_el)
    number_cell_el_lst = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")
    number_cell_el = find_element_from_lst_by_txt(number_cell_el_lst, str(index_column))
    parent_el = get_parent(number_cell_el)
    return parent_el.find_elements(By.TAG_NAME, "td")[cell_value_column]


def get_lot_cell_without_scroll(driver, index_column, cell_value_column):
    number_cell_el_lst = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")
    number_cell_el = find_element_from_lst_by_txt(number_cell_el_lst, str(index_column))
    parent_el = get_parent(number_cell_el)
    return parent_el.find_elements(By.TAG_NAME, "td")[cell_value_column]


def drag_and_drop(driver, source_element, target_element):
    ActionChains(driver).drag_and_drop(source_element, target_element).perform()


def scroll_down(driver, by, element, scroll_amount=1):
    target_element = driver.find_element(by, element)
    actions_click(driver, target_element)
    time.sleep(1)
    actions = ActionChains(driver)
    for _ in range(scroll_amount):
        actions.move_to_element(target_element).send_keys(Keys.ARROW_DOWN)
    actions.perform()


def find_elements_from_lst_ends_with_txt(elements, text):
    text = text.lstrip().lower()
    el_lst = []
    for el in elements:
        if el.text.lstrip().lower().endswith(text):
            el_lst.append(el)
    if len(el_lst) == 0:
        raise ElementNotFound(f'Element with text: "{text}" not found')
    return el_lst


def scroll_down_using_js(driver, by, element, scroll_amount=50):
    scroll_element = driver.find_element(by, element)
    current_scroll_position = driver.execute_script("return arguments[0].scrollTop;", scroll_element)
    new_scroll_position = current_scroll_position + scroll_amount
    driver.execute_script(f"arguments[0].scrollTop = {new_scroll_position};", scroll_element)


def is_scroll_at_end(driver, scroll_el):
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_el)
    scroll_position = driver.execute_script("return arguments[0].scrollTop;", scroll_el)
    client_height = driver.execute_script("return arguments[0].clientHeight;", scroll_el)
    scroll_difference = scroll_height - scroll_position - client_height

    return scroll_difference <= 1


def actions_double_click(driver, element):
    action_chains = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    action_chains.double_click(element).perform()


def find_elements_from_lst_by_txt(elements, text):
    el_lst = []
    text = text.strip().lower()
    for el in elements:
        if el.text.strip().lower() == text:
            el_lst.append(el)
    if len(el_lst) == 0:
        raise ElementNotFound(f'Element with text: "{text}" not found')
    return el_lst


def scroll_to_top(driver, by, element):
    scroll_el = driver.find_element(by, element)
    driver.execute_script("arguments[0].scrollTop = 0;", scroll_el)


def wait_for_the_all_elements_gets_loaded(driver, by, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((by, locator))
    )


def find_element_from_lst_by_txt_with_retries(driver, by, locator, text, retries=5):
    element_found = False
    elements = driver.find_elements(by, locator)
    founded_el = None
    for _ in range(retries):
        try:
            for el in elements:
                if el.text.strip().lower() == text.lower():
                    element_found = True
                    founded_el = el
            if element_found:
                return founded_el
            else:
                raise ElementNotFound(f'Element with text: "{text}" not found')
        except Exception as e:
            elements = driver.find_elements(by, locator)  # Refresh the list of elements
            time.sleep(0.5)


def find_element_from_lst_start_with_txt_with_retries(driver, by, locator, text, retries=5):
    element_found = False
    elements = driver.find_elements(by, locator)
    founded_el = None
    text = text.lower().strip()
    for _ in range(retries):
        try:
            for el in elements:
                if el.text.strip().lower().startswith(text):
                    element_found = True
                    founded_el = el
            if element_found:
                return founded_el
            else:
                raise ElementNotFound(f'Element with text: "{text}" not found')
        except StaleElementReferenceException:
            elements = driver.find_elements(by, locator)  # Refresh the list of elements
            time.sleep(0.5)


def scroll_to_right(driver):
    scroll_el = driver.find_element(By.CSS_SELECTOR, '.cdk-virtual-scrollable')
    driver.execute_script("arguments[0].scrollLeft += arguments[0].offsetWidth;", scroll_el)


def wait_for_loader_to_disappear(driver, timeout=20):
    try:
        wait_for_element_to_disappear(driver, By.CSS_SELECTOR, '.loader [data-mat-icon-name="temp-loader"]', timeout)
    except TimeoutException:
        pass


def wait_for_loader_to_appear(driver, timeout=15):
    wait_for_element(driver, By.CSS_SELECTOR, '.loader [data-mat-icon-name="temp-loader"]', timeout)


def find_elements_from_lst_with_txt(elements, text):
    text = text.lstrip().lower()
    el_lst = []
    for el in elements:
        if text in el.text.lstrip().lower():
            el_lst.append(el)
    if len(el_lst) == 0:
        raise ElementNotFound(f'Element with text: "{text}" not found')
    else:
        return el_lst


def get_text_from_element_array_in_lower_case(element_el_lst):
    """
    :param element_el_lst: list of elements
    :return: list of elements text
    """
    return [el.text.strip().lower() for el in element_el_lst]


def make_element_visible(driver, element):
    driver.execute_script("arguments[0].style.visibility='visible';", element)


def wait_for_element_to_be_clickable(driver, by, element, timeout=10):
    locator = driver.find_element(by, element)
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def find_element_from_lst_by_txt_with_splitting_braces(elements, text):
    text = text.strip().lower()
    for el in elements:
        text_in_el = el.text.strip().lower().split('(')[0].strip()
        if text_in_el == text:
            return el
        time.sleep(0.5)
    raise ElementNotFound(f'Element with text: "{text}" not found')


def find_elements_from_lst_starting_by_txt_with_splitting_braces(elements, text):
    text = text.strip().lower()
    matching_elements = []

    for el in elements:
        text_in_el = el.text.strip().lower().split('(')[0].strip()
        if text_in_el.startswith(text):
            matching_elements.append(el)
        time.sleep(0.5)

    if matching_elements:
        return matching_elements
    else:
        raise ElementNotFound(f'Element with text starting by: "{text}" not found')


def wait_for_file_to_download(download_path, file_name, timeout=30):
    """Wait for a file to appear in the download directory."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            files = os.listdir(download_path)
            print(f"files  --- {files}")
            if files:  # Check if any file is present in the directory
                for file in files:
                    if file.startswith(file_name):
                        print(
                            f"file {file_name} downloaded in {download_path}, it also have {os.listdir(download_path)}")
                        return
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            time.sleep(2)

    raise TimeoutError(f"file {file_name} not  downloaded in {download_path}, it has {os.listdir(download_path)}")


def maximize_window(driver):
    driver.execute_script("window.moveTo(0, 0); window.resizeTo(screen.width, screen.height);")
    time.sleep(1)


def right_actions_click(driver, element):
    action = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    action.context_click(element).perform()


def clear_text_field(element):
    element.send_keys(Keys.CONTROL, 'a')
    element.send_keys(Keys.BACKSPACE)
