import pytest
from pages.login_page import LoginPage


def test_login_valido(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url


def test_usuario_bloqueado(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.error_text()


@pytest.mark.parametrize("user, pwd, mensaje", [
    ("standard_user", "incorrecta", "do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_login_invalido(driver, user, pwd, mensaje):
    page = LoginPage(driver)
    page.open()
    page.login(user, pwd)
    assert mensaje in page.error_text()