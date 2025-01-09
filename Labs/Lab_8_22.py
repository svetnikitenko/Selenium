from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


    driver = webdriver.Chrome()  
    driver.get("https://demoqa.com/")

    try:
        driver.find_element(By.XPATH, "//div[text()='Book Store Application']").click()
        driver.find_element(By.ID, "login").click()

        driver.find_element(By.ID, "userName").send_keys("user")
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "login").click()

        time.sleep(1)
        error_message = driver.find_element(By.ID, "name").text
        print(f"Error message: {error_message}, Expected: Invalid username or password!")

        driver.find_element(By.ID, "newUser").click()
        driver.find_element(By.ID, "firstName").send_keys("first")
        driver.find_element(By.ID, "lastName").send_keys("last")
        driver.find_element(By.ID, "userName").send_keys("user")
        driver.find_element(By.ID, "password").send_keys("s")
        driver.find_element(By.ID, "register").click()

        time.sleep(100)
        error_message = driver.find_element(By.ID, "name").text
        print(f"Error message: {error_message}, Expected: Please verify reCaptcha to register!")

    except Exception as ex:
        print(f"Ошибка в тесте Lab_8: {ex}")

    finally:
        driver.quit()


