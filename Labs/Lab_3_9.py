"""Написать 9 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Alerts, Frame & Windows'
3. Выбрать пункт 'Browser Windows'
4. Нажать New Tab
5. Переключиться в открывшуюся вкладку
6. Проверить адрес вкладки
7. Вернуться на первоначальную вкладку
8. Нажать New Window
9. Переключиться в открывшуюся вкладку
10. Проверить адрес вкладки
11. Вернуться на первоначальную вкладку"""

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

    # 2. Перейти в раздел 'Alerts, Frame & Windows'
    alerts_section = driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    alerts_section.click()

    # 3. Выбрать пункт 'Browser Windows'
    browser_windows_option = driver.find_element(By.XPATH, "//span[text()='Browser Windows']")
    browser_windows_option.click()

    # 4. Нажать New Tab
    new_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
    new_tab_button.click()

    # 5. Переключиться в открывшуюся вкладку
    original_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # 6. Проверить адрес вкладки
    current_url = driver.current_url
    assert current_url == "https://demoqa.com/sample", f"Ожидаемый URL: 'https://demoqa.com/sample', но найден: '{current_url}'"

    # 7. Вернуться на первоначальную вкладку
    driver.switch_to.window(original_window)

    # 8. Нажать New Window
    new_window_button = driver.find_element(By.XPATH, "//button[@id='windowButton']")
    new_window_button.click()

    # 9. Переключиться в открывшуюся вкладку
    all_windows = driver.window_handles
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # 10. Проверить адрес вкладки
    current_url = driver.current_url
    assert current_url == "https://demoqa.com/sample", f"Ожидаемый URL: 'https://demoqa.com/sample', но найден: '{current_url}'"

    # 11. Вернуться на первоначальную вкладку
    driver.switch_to.window(original_window)

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
