"""Написать 13 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Alerts, Frame & Windows'
3. Выбрать пункт 'Modal Dialogs'
4. Нажать Small Modal
5. В открывшемся окне сверить заголовок
6. В открывшемся окне сверить основной текст
7. Нажать Close"""

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

    # 3. Выбрать пункт 'Modal Dialogs'
    modal_dialogs_option = driver.find_element(By.XPATH, "//span[text()='Modal Dialogs']")
    modal_dialogs_option.click()

    # 4. Нажать Small Modal
    small_modal_button = driver.find_element(By.XPATH, "//button[@id='showSmallModal']")
    small_modal_button.click()

    # 5. В открывшемся окне сверить заголовок
    modal_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-title h4']"))
    ).text
    assert modal_title == "Small Modal", f"Ожиданный заголовок: 'Small Modal', но найден: '{modal_title}'"

    # 6. В открывшемся окне сверить основной текст
    modal_body = driver.find_element(By.XPATH, "//div[@class='modal-body']").text
    expected_body_text = "This is a small modal. It has very less content"
    assert modal_body == expected_body_text, f"Ожиданный текст: '{expected_body_text}', но найден: '{modal_body}'"

    # 7. Нажать Close
    close_button = driver.find_element(By.XPATH, "//button[@id='closeSmallModal']")
    close_button.click()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
