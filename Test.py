import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

def test_login_success():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/login")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("1234")

    submit = driver.find_element(By.ID, "login")
    submit.click()
    success_message = driver.find_element(By.LINK_TEXT, 'Profile')
    assert "Profile" in success_message.text
    driver.close()

def test_login_failure():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/login")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("word")

    submit = driver.find_element(By.ID, "login")
    submit.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "span.text-xs").text
    print(error_message)
    assert "The provided credentials do not match our records." in error_message
    driver.close()

def test_passreset_success():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/passwordreset")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    submit = driver.find_element(By.CSS_SELECTOR, "button.text-center")
    submit.click()

    success_message = driver.find_element(By.CSS_SELECTOR, "span.text-xs").text
    assert "Check your email" in success_message

    driver.close()

def test_passreset_failure():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/passwordreset")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    submit = driver.find_element(By.CSS_SELECTOR, "button.text-center")
    submit.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "span.text-xs").text
    assert "The provided credentials do not match our records." in error_message
    driver.close()
def test_ticket_purchase():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/login")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("1234")

    submit = driver.find_element(By.ID, "login")
    submit.click()
    success_message = driver.find_element(By.LINK_TEXT, 'Profile')
    if "Profile" in success_message.text:
        driver.get("http://127.0.0.1:8000/buyTicket")
        time.sleep(2)
        driver.get('http://127.0.0.1:8000/checkout/'+str(random.randint(1, 8)))
        time.sleep(2)
        method = driver.find_element(By.XPATH, "//input[@value='wallet']")
        method.click()
        confirmPurchase = driver.find_element(By.CSS_SELECTOR, "button.text-white")
        confirmPurchase.click()
        time.sleep(2)
        completed = driver.find_element(By.ID, "ActiveTickets").text
        assert "Active Tickets" in completed
        driver.close()
    else:
        driver.close()

def test_refund():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/login")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("mzkamol@gmail.com")

    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys("1234")

    submit = driver.find_element(By.ID, "login")
    submit.click()
    success_message = driver.find_element(By.LINK_TEXT, 'Profile')
    if "Profile" in success_message.text:
        driver.get("http://127.0.0.1:8000/myTickets")
        time.sleep(2)
        activetickets = driver.find_element(By.ID, "ActiveTickets")
        activetickets.click()
        time.sleep(2)
        refund = driver.find_element(By.CSS_SELECTOR, "button.inline-block")
        refund.click()
        time.sleep(3)
        completed = driver.find_element(By.CSS_SELECTOR, "h1.text-4xl").text
        assert "Ticket Refund Success!" in completed
        driver.close()
    else:
        driver.close()
