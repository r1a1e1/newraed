import pytest
import requests
from main import *

class TestUI:
    def test_1(self):
        opensite(driver)
        assert driver.current_url =='https://www.saucedemo.com/'

    def test_2(self):
        opensite(driver)
        login(driver)
        actual = add_items(driver)
        expected = price
        assert expected == actual

    def test_3_N(self):
        opensite(driver)
        login(driver)
        actual = add_items(driver)
        expected = 20
        assert expected != actual
    def test_4_N(self):
        opensite(driver)
        assert driver.current_url != 'https://www.sauchjmo.com/'


class TestAPI:
    def test_1(self):
        res =requests.get('https://reqres.in/api/users/1')
        assert res.status_code == 200
    def test_2(self):
        res = requests.get('https://reqres.in/api/users/1')
        assert res.json()['data']['id'] == 1