import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

driver = webdriver.Chrome()
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
assert 'Practice Page' in driver.title
driver.maximize_window()

radio_button = driver.find_element(By.XPATH, '//input[@value="radio1"]').click()

suggession_class = driver.find_element(By.XPATH, '//input[@id="autocomplete"]')
suggession_class.click()
suggession_class.send_keys('Armenia')
suggession_class.send_keys(Keys.ENTER)

dropdown = driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]')
drop = Select(dropdown)
drop.select_by_index(3)

checkbox = driver.find_element(By.XPATH, '//input[@id="checkBoxOption2"]').click()

parent_handle = driver.current_window_handle
switch_win = driver.find_element(By.XPATH, '//button[@id="openwindow"]').click()
time.sleep(4)
all_handles = driver.window_handles
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,
                            '//div[@style="position: absolute; inset: 0px; box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px inset;"]').click()
        driver.find_element(By.XPATH,
                            '//img[@alt="selenium-webdriver-with-java-basics-advanced-interview-guide"]').click()
        time.sleep(3)
        driver.close()
        break
driver.switch_to.window(parent_handle)

parent_handle = driver.current_window_handle
switch_tab = driver.find_element(By.XPATH, '//a[@id="opentab"]').click()
all_handles = driver.window_handles
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        switch_sec = driver.find_element(By.XPATH, '//span[@class="icon flaticon-book-1"]').click()
        time.sleep(4)
        driver.close()
        break
driver.switch_to.window(parent_handle)

driver.find_element(By.XPATH, '//input[@id="name"]').send_keys('Anahit')
switch_alert = driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()
driver.switch_to.alert.accept()

elem = driver.find_element(By.ID, 'displayed-text').send_keys('12345')
hide = driver.find_element(By.ID, 'hide-textbox').click()
time.sleep(2)
show = driver.find_element(By.ID, 'show-textbox').click()

scroll_t = driver.find_element(By.XPATH, '//div[@class="tableFixHead"]')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", scroll_t)
time.sleep(3)

element = driver.find_element(By.XPATH, '//div[@class="tableFixHead"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()

hover_over = driver.find_element(By.ID, "mousehover")
hover = ActionChains(driver).move_to_element(hover_over)
hover.perform()
top = driver.find_element(By.XPATH, '//a[@href ="#top"]')
top.click()
time.sleep(3)

driver.find_element(By.XPATH, '//header[@class="jumbotron text-center header_style"]')
wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element(By.ID, "courses-iframe")))
all_access_plan = driver.find_element(By.XPATH, '//a[@href="lifetime-access"][@class="new-navbar-highlighter"]').click()
time.sleep(3)
driver.quit()
