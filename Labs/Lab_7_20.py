"""Написать 20 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Interaction'
3. Выбрать пункт 'Sortable'
4. Перейти на вкладку List
5. Отсортировать значения в убывающем порядке
"""
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

    # 3. Выбрать пункт 'Sortable'
    sortable_option = driver.find_element(By.XPATH, "//span[text()='Sortable']")
    sortable_option.click()

    # 4. Перейти на вкладку List
    list_tab = driver.find_element(By.XPATH, "//a[@id='demo-tab-list']")
    list_tab.click()

    # 5. Отсортировать значения в убывающем порядке
    # Получаем элементы списка
    list_items = driver.find_elements(By.XPATH,
                                      "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')]")

    # Получаем текст элементов
    initial_order = [item.text for item in list_items]
    sorted_order = sorted(initial_order, reverse=True)

    # Перемещаем элементы
    actions = ActionChains(driver)
    for target_index, target_text in enumerate(sorted_order):
        for item in list_items:
            if item.text == target_text:
                actions.click_and_hold(item).move_to_element(list_items[target_index]).release().perform()
                time.sleep(0.5)  # Небольшая задержка для обновления DOM
                break

        # Обновляем список после каждого перемещения
        list_items = driver.find_elements(By.XPATH,
                                          "//div[@id='demo-tabpane-list']//div[contains(@class, 'list-group-item')]")

    # Проверяем финальный порядок
    final_order = [item.text for item in list_items]
    assert final_order == sorted_order, f"Элементы не отсортированы в порядке убывания: {final_order}"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()

