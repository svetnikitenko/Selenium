"""Написать 19 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Select Menu'
4. В поле 'Select Value' выбрать 'A root option'
5. В поле 'Select One' выбрать 'Ms.'
6. В поле 'Old Style Select Menu' выбрать 'Black'
7. В поле 'Multiselect drop down' выбрать: Black, Red
8. В поле 'Standard multi select' выбрать 'Opel'"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

    # 3. Выбрать пункт 'Select Menu'
    select_menu_option = driver.find_element(By.XPATH, "//span[text()='Select Menu']")
    select_menu_option.click()

    # 4. В поле 'Select Value' выбрать 'A root option'
    select_value = driver.find_element(By.XPATH, "//div[@id='withOptGroup']")
    select_value.click()
    root_option = driver.find_element(By.XPATH, "//div[text()='A root option']")
    root_option.click()

    # Проверяем выбор
    selected_value = driver.find_element(By.XPATH, "//div[@id='withOptGroup']/div/div").text
    assert selected_value == "A root option", f"Ожидалось 'A root option', но выбрано '{selected_value}'"

    # 5. В поле 'Select One' выбрать 'Ms.'
    select_one = driver.find_element(By.XPATH, "//div[@id='selectOne']")
    select_one.click()
    ms_option = driver.find_element(By.XPATH, "//div[text()='Ms.']")
    ms_option.click()

    # Проверяем выбор
    selected_one = driver.find_element(By.XPATH, "//div[@id='selectOne']/div/div").text
    assert selected_one == "Ms.", f"Ожидалось 'Ms.', но выбрано '{selected_one}'"

    # 6. В поле 'Old Style Select Menu' выбрать 'Black'
    old_style_select = driver.find_element(By.XPATH, "//select[@id='oldSelectMenu']")
    select = Select(old_style_select)
    select.select_by_visible_text("Black")

    # Проверяем выбор
    selected_old_style = select.first_selected_option.text
    assert selected_old_style == "Black", f"Ожидалось 'Black', но выбрано '{selected_old_style}'"

    # 7. В поле 'Multiselect drop down' выбрать: Black, Red
    multi_select = driver.find_element(By.XPATH, "//div[@id='react-select-4-input']")
    for color in ["Black", "Red"]:
        multi_select.send_keys(color)
        multi_select.send_keys(Keys.ENTER)

    # Проверяем выбор
    selected_multi_values = driver.find_elements(By.XPATH, "//div[@class='css-12jo7m5 multi-value__label']")
    selected_multi_colors = [value.text for value in selected_multi_values]
    for color in ["Black", "Red"]:
        assert color in selected_multi_colors, f"Ожидалось '{color}' в Multiselect drop down, но не найдено"

    # 8. В поле 'Standard multi select' выбрать 'Opel'
    standard_multi_select = driver.find_element(By.XPATH, "//select[@id='cars']")
    select = Select(standard_multi_select)
    select.select_by_visible_text("Opel")

    # Проверяем выбор
    selected_standard_values = [option.text for option in select.all_selected_options]
    assert "Opel" in selected_standard_values, f"Ожидалось 'Opel', но выбрано '{selected_standard_values}'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
