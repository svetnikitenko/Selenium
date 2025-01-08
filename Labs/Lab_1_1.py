"""Написать 1 тест:
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Text Box'
4. Заполнить все поля форме валидными значениями
5. Нажать кнопку Submit
6. Проверить что ниже появились введенные данные
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # 1. Перейти на страницу https://demoqa.com/
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    # 2. Перейти в раздел 'Elements'
    elements_section = driver.find_element(By.XPATH, "//h5[text()='Elements']")
    elements_section.click()

    # 3. Выбрать пункт 'Text Box'
    text_box_option = driver.find_element(By.XPATH, "//span[text()='Text Box']")
    text_box_option.click()

    # 4. Заполнить все поля форме валидными значениями
    driver.find_element(By.ID, "userName").send_keys("Max Lashkin")
    driver.find_element(By.ID, "userEmail").send_keys("max.lashkin@gmail.com")
    driver.find_element(By.ID, "currentAddress").send_keys("70 Let Oktyabrya street 6-1, kv. 3, Omsk")
    driver.find_element(By.ID, "permanentAddress").send_keys("Bratskaya street 3, kv. 11, Omsk")

    # 5. Нажать кнопку Submit
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 6. Проверить, что ниже появились введенные данные
    time.sleep(1)  # Небольшая пауза для отображения результатов
    output_name = driver.find_element(By.ID, "name").text
    output_email = driver.find_element(By.ID, "email").text
    output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
    output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

    assert "Max Lashkin" in output_name, "Имя не совпадает"
    assert "max.lashkin@gmail.com" in output_email, "Email не совпадает"
    assert "70 Let Oktyabrya street 6-1, kv. 3, Omsk" in output_current_address, "Current Address не совпадает"
    assert "Bratskaya street 3, kv. 11, Omsk" in output_permanent_address, "Permanent Address не совпадает"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
