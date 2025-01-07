"""Написать 6 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Upload and Download'
4. Загрузить файл
5. Проверить в поле с именем файла его имя
6. Проверить в поле с полным именем директории имя всего пути"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # 3. Выбрать пункт 'Dynamic Properties'
    dynamic_properties_option = driver.find_element(By.XPATH, "//span[text()='Dynamic Properties']")
    dynamic_properties_option.click()

    # 4. Подождать, пока текст кнопки 'Color Change' не сменит цвет
    color_change_button = driver.find_element(By.XPATH, "//button[@id='colorChange']")
    initial_color = color_change_button.value_of_css_property("color")

    # Используем WebDriverWait для ожидания изменения цвета
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.XPATH, "//button[@id='colorChange']").value_of_css_property(
            "color") != initial_color
    )
    print("Цвет кнопки 'Color Change' изменился.")

    # 5. Обновить страницу
    driver.refresh()

    # 6. Подождать, пока кнопка 'Visible After 5 Seconds' не появится
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='visibleAfter']"))
    )
    print("Кнопка 'Visible After 5 Seconds' появилась.")

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
