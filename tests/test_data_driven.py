import json
import csv
import yaml
import pytest
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from utils.logger import get_logger

log = get_logger()

class TestDataDriven:
    @pytest.fixture
    def login_data(self):
        with open('test_data/users.json') as f:
            return json.load(f)
        
    @pytest.fixture
    def product_data(self):
        products = []
        with open('test_data/products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
        return products
    
    @pytest.fixture
    def checkout_data(self):
        with open('test_data/checkout_data.yaml') as f:
            return yaml.safe_load(f)
        
    # login with multiple users
    @pytest.mark.parametrize("user_type,index", [
        ("valid_users",0),
        ("valid_users",1),
        ("invalid_users",0),
        ("invalid_users",1)
    ])
    def test_multiple_users_login(self,driver, login_data, user_type, index):
        user = login_data[user_type][index]
        user_name = user["username"]
        password = user["password"]
        expected = user["expected"]
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login(user_name,password)

    # Display products from csv
    @pytest.mark.parametrize("index",[ 0,1,2])
    def test_products_prices(self,driver,product_data,index):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("standard_user","secret_sauce")
        product = product_data[index]
        # displaying product idex,name and price
        product_index = product["product_index"]
        product_name = product["product_name"]
        product_price = product["expected_price"]
        log.info(f"Displaying the product details. Product index is {product_index} , name is {product_name} and price is {product_price}")
