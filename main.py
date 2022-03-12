import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.linkedin.com')
browser.maximize_window()

email_field = browser.find_element(By.ID, 'session_key')
email_field.send_keys('ur email')

email_field = browser.find_element(By.ID, 'session_password')
email_field.send_keys('ur password')

signInButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
signInButton.click()

search_input = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Pesquisar"]')
search_input.send_keys('ReactJS')
search_input.send_keys(Keys.ENTER)

time.sleep(3)

job_filter = browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Vagas"]')
job_filter.click()

time.sleep(3)

location_input = browser.find_elements(By.CSS_SELECTOR, '.jobs-search-box__inner input[role="combobox"]')[1]

for i in range(0, len('Brasil')):
    location_input.send_keys(Keys.BACKSPACE)

location_input.send_keys('Mundialmente')

search_button = browser.find_element(By.CSS_SELECTOR, '.jobs-search-box__submit-button')
search_button.click()
