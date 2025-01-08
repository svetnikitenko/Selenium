"""Написать 16 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Date Picker'
4. В поле 'Select Date' выбрать 1 декабря 2023 годя
5. В поле 'Date And Time' 2 ноября 2022 года 20:00"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    # 2. Перейти в раздел 'Widgets'
    widgets_section = driver.find_element(By.XPATH, "//h5[text()='Widgets']")
    widgets_section.click()

    # 3. Выбрать пункт 'Date Picker'
    date_picker_option = driver.find_element(By.XPATH, "//span[text()='Date Picker']")
    date_picker_option.click()

    # 4. В поле 'Select Date' выбрать 1 декабря 2023 года
    date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
    date_input.click()
    date_input.send_keys(Keys.CONTROL + "a")  # Выделяем текст
    date_input.send_keys(Keys.BACKSPACE)  # Удаляем текущую дату
    date_input.send_keys("12/01/2023")  # Вводим дату в формате MM/DD/YYYY
    date_input.send_keys(Keys.ENTER)

    # Проверяем, что дата установлена
    assert date_input.get_attribute("value") == "12/01/2023", f"Дата не установлена: {date_input.get_attribute('value')}"

    # 5. В поле 'Date And Time' выбрать 2 ноября 2022 года 20:00
    date_time_input = driver.find_element(By.XPATH, "//input[@id='dateAndTimePickerInput']")
    date_time_input.click()
    date_time_input.send_keys(Keys.CONTROL + "a")  # Выделяем текст
    date_time_input.send_keys(Keys.BACKSPACE)  # Удаляем текущую дату и время

    # Вводим дату и время в формате "Month Day, Year Hours:Minutes PM/AM"
    date_time_input.send_keys("November 2, 2022 8:00 PM")
    date_time_input.send_keys(Keys.ENTER)

    # Проверяем, что дата и время установлены
    assert date_time_input.get_attribute("value") == "November 2, 2022 8:00 PM", f"Дата и время не установлены: {date_time_input.get_attribute('value')}"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
