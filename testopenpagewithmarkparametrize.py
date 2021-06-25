from selenium import webdriver
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

Alamat = [
    ("https://www.facebook.com", "Facebook - Masuk atau Daftar")
]

@pytest.mark.parametrize('address, result', Alamat)

def test_openpage(address,result):
    driver.get(address)
    Title = driver.title
    
    assert Title == result
