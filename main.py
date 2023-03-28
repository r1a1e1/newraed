from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
time.sleep(1)
standard = 'standard_user'
standard2 = 'standard_usewwr'
password = 'secret_sauce'
price = 29.99 + 9.99

def opensite(driver):
    driver.get('https://www.saucedemo.com/')
    return driver


def login(driver):
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(standard)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    return driver


def add_items(driver):
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    price = float(driver.find_element(By.CSS_SELECTOR, '#cart_contents_container > div > div.cart_list > div:nth-child(3) > div.cart_item_label > div.item_pricebar > div').text[1:]) +float(driver.find_element(By.CSS_SELECTOR, '#cart_contents_container > div > div.cart_list > div:nth-child(4) > div.cart_item_label > div.item_pricebar > div').text[1:])

    return price


def pay(driver):
    driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('raed')
    driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('abu ful')
    driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('19987898987')
    driver.find_element(By.CSS_SELECTOR,'#continue').click()
    driver.find_element(By.CSS_SELECTOR,'#finish').click()
    return driver.find_element(By.CSS_SELECTOR,'#checkout_complete_container > h2').text



