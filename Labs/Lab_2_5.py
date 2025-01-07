"""Написать 5 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Links'
4. Нажать на кнопку Home
5. Переключиться на открывшееся окно
6. Проверить адрес открывшегося окна
7. Переключиться на первое окно
8. Нажать Moved
9. Проверить что появилась надпись Link has responded with staus 301 and status text Moved Permanently
"""

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

    # 3. Выбрать пункт 'Links'
    links_option = driver.find_element(By.XPATH, "//span[text()='Links']")
    links_option.click()

    # 4. Нажать на кнопку Home
    home_button = driver.find_element(By.XPATH, "//a[text()='Home']")
    home_button.click()

    # 5. Переключиться на открывшееся окно
    # Получаем все окна
    original_window = driver.current_window_handle
    all_windows = driver.window_handles

    # Переключаемся на новое окно
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # 6. Проверить адрес открывшегося окна
    current_url = driver.current_url
    assert current_url == "https://demoqa.com/", f"Ожидаемый URL: https://demoqa.com/, но найден: {current_url}"

    # 7. Переключиться на первое окно
    driver.switch_to.window(original_window)

    # 8. Нажать Moved
    moved_button = driver.find_element(By.XPATH, "//a[text()='Moved']")
    moved_button.click()

    # 9. Проверить, что появилась надпись Link has responded with status 301 and status text Moved Permanently
    response_text = driver.find_element(By.XPATH, "//p[@id='linkResponse']").text
    expected_text = "Link has responded with staus 301 and status text Moved Permanently"
    #expected_text = "Link has responded with status 301 and status text Moved Permanently"
    assert response_text == expected_text, f"Ожидаемый текст: '{expected_text}', но найден: '{response_text}'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
