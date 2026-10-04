from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait



load_dotenv()

FORM:str = os.getenv('FORM') or ''

def fill_form(data):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get(FORM)

    for item in data:
        link = item['link']
        price = item['price']
        address = item['address']

        wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[1]')))
        
        address_input = driver.find_element(By.XPATH, '(//input[@type="text"])[1]')
        address_input.send_keys(address)

        price_input = driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
        price_input.send_keys(price)

        link_input = driver.find_element(By.XPATH, '(//input[@type="text"])[3]')
        link_input.send_keys(link)


        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button"]//span[text()="Submit"]')))
        submit_button.click()

        submit_another = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Submit another response")]')))
        submit_another.click()


if __name__ == "__main__":

    data = [{'link': 'https://www.zillow.com/homedetails/123-Main-St-Somecity-CA-12345/12345678_zpid/', 'price': '$500,000', 'address': '123 Main St, Somecity, CA 12345'}]
    fill_form(data)