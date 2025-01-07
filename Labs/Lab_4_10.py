"""Написать 10 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Alerts, Frame & Windows'
3. Выбрать пункт 'Alerts'
4. Нажать 1 кнопку Click Me
5. Проверить текст в модальном окне
6. Нажать ОК
7. Нажать 2 кнопку Click Me
8. Проверить текст в модальном окне
9. Нажать ОК
10. Нажать 3 кнопку Click Me
11. Проверить текст в модальном окне
12. Нажать Отмена
13. Нажать 4 кнопку Click Me
14. Ввести текст в модальном окне
15. Нажать ОК"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # 1. Перейти на страницу https://demoqa.com/
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    # 2. Перейти в раздел 'Alerts, Frame & Windows'
    alerts_section = driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    alerts_section.click()

    # 3. Выбрать пункт 'Alerts'
    alerts_option = driver.find_element(By.XPATH, "//span[text()='Alerts']")
    alerts_option.click()

    # 4. Нажать 1 кнопку Click Me
    first_button = driver.find_element(By.XPATH, "//button[@id='alertButton']")
    first_button.click()

    # 5. Проверить текст в модальном окне
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "You clicked a button", f"Ожиданный текст: 'You clicked a button', но найден: '{alert.text}'"

    # 6. Нажать ОК
    alert.accept()

    # 7. Нажать 2 кнопку Click Me
    second_button = driver.find_element(By.XPATH, "//button[@id='timerAlertButton']")
    second_button.click()

    # 8. Проверить текст в модальном окне
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "This alert appeared after 5 seconds", f"Ожиданный текст: 'This alert appeared after 5 seconds', но найден: '{alert.text}'"

    # 9. Нажать ОК
    alert.accept()

    # 10. Нажать 3 кнопку Click Me
    third_button = driver.find_element(By.XPATH, "//button[@id='confirmButton']")
    third_button.click()

    # 11. Проверить текст в модальном окне
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Do you confirm action?", f"Ожиданный текст: 'Do you confirm action?', но найден: '{alert.text}'"

    # 12. Нажать Отмена
    alert.dismiss()

    # 13. Нажать 4 кнопку Click Me
    fourth_button = driver.find_element(By.XPATH, "//button[@id='promtButton']")
    fourth_button.click()

    # 14. Ввести текст в модальном окне
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Test Input")

    # 15. Нажать ОК
    alert.accept()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
