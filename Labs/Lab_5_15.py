"""Написать 15 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Auto Complete'
4. В поле 'Type multiple color names' выбрать значения: Black, Red, Magenta
5. В поле 'Type single color name' выбрать значения: Black
5. В поле 'Type single color name' заменить значения на Red"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # 3. Выбрать пункт 'Auto Complete'
    auto_complete_option = driver.find_element(By.XPATH, "//span[text()='Auto Complete']")
    auto_complete_option.click()

    # 4. В поле 'Type multiple color names' выбрать значения: Black, Red, Magenta
    multiple_input = driver.find_element(By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    for color in ["Black", "Red", "Magenta"]:
        multiple_input.send_keys(color)
        multiple_input.send_keys(Keys.ENTER)

    # Проверяем, что значения добавлены
    added_colors = driver.find_elements(By.XPATH, "//div[@class='css-12jo7m5 auto-complete__multi-value']")
    added_color_names = [color.text for color in added_colors]
    assert "Black" in added_color_names, "'Black' не найден в поле multiple"
    assert "Red" in added_color_names, "'Red' не найден в поле multiple"
    assert "Magenta" in added_color_names, "'Magenta' не найден в поле multiple"

    # 5. В поле 'Type single color name' выбрать значения: Black
    single_input = driver.find_element(By.XPATH, "//input[@id='autoCompleteSingleInput']")
    single_input.send_keys("Black")
    single_input.send_keys(Keys.ENTER)

    # Проверяем, что значение добавлено
    selected_color = driver.find_element(By.XPATH, "//div[@class='auto-complete__single-value']").text
    assert selected_color == "Black", f"Ожидалось значение 'Black', но найдено '{selected_color}'"

    # 6. В поле 'Type single color name' заменить значение на Red
    single_input = driver.find_element(By.XPATH, "//input[@id='autoCompleteSingleInput']")
    single_input.send_keys(Keys.CONTROL + "a")  # Выделяем весь текст
    single_input.send_keys(Keys.BACKSPACE)  # Удаляем текущее значение
    single_input.send_keys("Red")
    single_input.send_keys(Keys.ENTER)

    # Проверяем, что значение изменено
    selected_color = driver.find_element(By.XPATH, "//div[@class='auto-complete__single-value']").text
    assert selected_color == "Red", f"Ожидалось значение 'Red', но найдено '{selected_color}'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
