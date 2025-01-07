"""Написать 21 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Interaction'
3. Выбрать пункт 'Selectable'
4. Перейти на вкладку Grid
5. Выбрать все значения
6. Снять все значения
7. Выбрать только Five"""

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

    # 2. Перейти в раздел 'Interaction'
    interaction_section = driver.find_element(By.XPATH, "//h5[text()='Interactions']")
    interaction_section.click()

    # 3. Выбрать пункт 'Selectable'
    selectable_option = driver.find_element(By.XPATH, "//span[text()='Selectable']")
    selectable_option.click()

    # 4. Перейти на вкладку Grid
    grid_tab = driver.find_element(By.XPATH, "//a[@id='demo-tab-grid']")
    grid_tab.click()

    # 5. Выбрать все значения
    grid_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'list-group-item')]")
    for item in grid_items:
        item.click()
        time.sleep(0.1)  # Небольшая задержка для корректного взаимодействия

    # Проверяем, что все значения выбраны
    selected_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'active')]")
    assert len(selected_items) == len(grid_items), f"Ожидалось {len(grid_items)} выбранных элементов, но найдено {len(selected_items)}"

    # 6. Снять все значения
    for item in grid_items:
        item.click()
        time.sleep(0.1)

    # Проверяем, что все значения сняты
    selected_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'active')]")
    assert len(selected_items) == 0, "Не все значения сняты"

    # 7. Выбрать только Five
    five_item = driver.find_element(By.XPATH, "//li[text()='Five']")
    five_item.click()

    # Проверяем, что выбрано только значение "Five"
    selected_items = driver.find_elements(By.XPATH, "//li[contains(@class, 'active')]")
    assert len(selected_items) == 1 and selected_items[0].text == "Five", "Выбрано не только 'Five'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
