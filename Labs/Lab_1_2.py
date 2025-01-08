"""Написать 2 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Check Box'
4. Нажать на +
5. Поставить чек боксы на пункты: Notes, Veu, Private
6. Нажать -"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # 1. Перейти на страницу https://demoqa.com/
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    # 2. Перейти в раздел 'Elements'
    elements_section = driver.find_element(By.CSS_SELECTOR, ".card-body h5")
    elements_section.click()

    # 3. Выбрать пункт 'Check Box'
    check_box_option = driver.find_element(By.CSS_SELECTOR, "span[title='Check Box']")
    check_box_option.click()

    # 4. Нажать на +
    expand_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_button.click()

    ## 5. Поставить чекбоксы на пункты: Notes, Veu, Private
    notes_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-notes']")
    veu_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-veu']")
    private_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='tree-node-private']")

    notes_checkbox.click()
    veu_checkbox.click()
    private_checkbox.click()

    #  6. Проверяем, что чекбоксы отмечены
    notes_input = driver.find_element(By.ID, "tree-node-notes")
    veu_input = driver.find_element(By.ID, "tree-node-veu")
    private_input = driver.find_element(By.ID, "tree-node-private")

    assert notes_input.is_selected(), "Notes не выбран"
    assert veu_input.is_selected(), "Veu не выбран"
    assert private_input.is_selected(), "Private не выбран"

    # 4. Нажать -
    collapse_button = driver.find_element(By.CSS_SELECTOR, "button[title='Collapse all']")
    collapse_button.click()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
