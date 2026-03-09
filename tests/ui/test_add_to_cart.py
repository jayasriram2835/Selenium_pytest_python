import pytest
from data.test_data import login_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize("user,pwd", login_data)
def test_add_product_to_cart(driver, user, pwd):

    login = LoginPage(driver)
    login.load()
    login.login(user, pwd)

    product = ProductPage(driver)
    product.add_product_to_cart()
    product.open_cart()

    assert "cart" in driver.current_url

