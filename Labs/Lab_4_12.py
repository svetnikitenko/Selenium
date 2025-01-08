"""Написать 12 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Alerts, Frame & Windows'
3. Выбрать пункт 'Nested Frames'
4. Проверить наличие текста 'Child Iframe' в 1 frame
5. Проверить наличие текста 'Parent frame' в 2 frame"""

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

    # 3. Выбрать пункт 'Nested Frames'
    nested_frames_option = driver.find_element(By.XPATH, "//span[text()='Nested Frames']")
    nested_frames_option.click()

    # 4. Проверить наличие текста 'Parent frame' в 2 frame
    # Переключаемся на родительский фрейм
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame1']"))
    parent_frame_text = driver.find_element(By.XPATH, "//body").text
    assert "Parent frame" in parent_frame_text, f"Текст в родительском фрейме не соответствует: '{parent_frame_text}'"

    # 5. Проверить наличие текста 'Child Iframe' в 1 frame
    # Переключаемся на дочерний фрейм внутри родительского
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
    child_frame_text = driver.find_element(By.XPATH, "//p").text
    assert child_frame_text == "Child Iframe", f"Текст в дочернем фрейме не соответствует: '{child_frame_text}'"

    # Возвращаемся в основной контекст страницы
    driver.switch_to.default_content()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
