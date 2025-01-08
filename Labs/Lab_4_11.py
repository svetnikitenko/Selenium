"""Написать 11 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Alerts, Frame & Windows'
3. Выбрать пункт 'Frames'
4. Проверить наличие текста 'This is a sample page' в 1 frame
5. Проверить наличие текста 'This is a sample page' в 2 frame"""

from selenium import webdriver
from selenium.webdriver.common.by import By

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

    # 3. Выбрать пункт 'Frames'
    frames_option = driver.find_element(By.XPATH, "//span[text()='Frames']")
    frames_option.click()

    # 4. Проверить наличие текста 'This is a sample page' в 1 frame
    driver.switch_to.frame("frame1")  # Переключение в первый iframe
    frame1_text = driver.find_element(By.XPATH, "//h1").text
    assert frame1_text == "This is a sample page", f"Текст в первом фрейме не соответствует: '{frame1_text}'"
    driver.switch_to.default_content()  # Возврат в основной контекст страницы

    # 5. Проверить наличие текста 'This is a sample page' в 2 frame
    driver.switch_to.frame("frame2")  # Переключение во второй iframe
    frame2_text = driver.find_element(By.XPATH, "//h1").text
    assert frame2_text == "This is a sample page", f"Текст во втором фрейме не соответствует: '{frame2_text}'"
    driver.switch_to.default_content()  # Возврат в основной контекст страницы

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
