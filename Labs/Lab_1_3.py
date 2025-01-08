"""Написать 3 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Radio Button'
4. Выбрать Yes
5. Проверить что появилась надпись Yes
6. Выбрать Impressive
7. Проверить что появилась надпись Impressive
8. Проверить что кнопка No недоступна"""

from selenium import webdriver
from selenium.webdriver.common.by import By

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

    # 3. Выбрать пункт 'Check Box'
    check_box_option = driver.find_element(By.XPATH, "//span[text()='Check Box']")
    check_box_option.click()

    # 4. Нажать на +
    expand_button = driver.find_element(By.XPATH, "//button[@title='Expand all']")
    expand_button.click()

    # 5. Поставить чек боксы на пункты: Notes, Veu, Private
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
    veu_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-veu']")
    private_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-private']")

    notes_checkbox.click()
    veu_checkbox.click()
    private_checkbox.click()

    # Проверяем, что чекбоксы отмечены
    notes_input = driver.find_element(By.XPATH, "//input[@id='tree-node-notes']")
    veu_input = driver.find_element(By.XPATH, "//input[@id='tree-node-veu']")
    private_input = driver.find_element(By.XPATH, "//input[@id='tree-node-private']")

    assert notes_input.is_selected(), "Notes не выбран"
    assert veu_input.is_selected(), "Veu не выбран"
    assert private_input.is_selected(), "Private не выбран"

    # 6. Нажать -
    collapse_button = driver.find_element(By.XPATH, "//button[@title='Collapse all']")
    collapse_button.click()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
