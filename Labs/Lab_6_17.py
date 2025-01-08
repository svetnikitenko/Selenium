"""Написать 17 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Slider'
4. Сдвинуть слайдер на значение 50
5. Проверить что в окне справа значение 50"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

    # 3. Выбрать пункт 'Slider'
    slider_option = driver.find_element(By.XPATH, "//span[text()='Slider']")
    slider_option.click()

    # 4. Сдвинуть слайдер на значение 50
    slider = driver.find_element(By.XPATH, "//input[@type='range']")
    value_box = driver.find_element(By.XPATH, "//input[@id='sliderValue']")

    # Устанавливаем слайдер на значение 50, шагая по одному
    current_value = int(value_box.get_attribute("value"))

    # Если текущее значение меньше 50
    while current_value < 50:
        ActionChains(driver).drag_and_drop_by_offset(slider, 1, 0).perform()
        current_value = int(value_box.get_attribute("value"))

    # Если текущее значение больше 50
    while current_value > 50:
        ActionChains(driver).drag_and_drop_by_offset(slider, -1, 0).perform()
        current_value = int(value_box.get_attribute("value"))

    # 5. Проверить, что в окне справа значение 50
    final_value = int(value_box.get_attribute("value"))
    assert final_value == 50, f"Ожидалось значение 50, но получено {final_value}"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
