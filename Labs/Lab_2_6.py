"""Написать 6 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Upload and Download'
4. Загрузить файл
5. Проверить в поле с именем файла его имя
6. Проверить в поле с полным именем директории имя всего пути"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    # 3. Выбрать пункт 'Upload and Download'
    upload_and_download_option = driver.find_element(By.XPATH, "//span[text()='Upload and Download']")
    upload_and_download_option.click()

    # 4. Загрузить файл
    # Указываем путь к файлу, который хотим загрузить
    file_path = os.path.abspath("c:/lab/file.txt")  # Замените на путь к вашему файлу
    upload_input = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
    upload_input.send_keys(file_path)

    # 5. Проверить в поле с именем файла его имя
    file_name_field = driver.find_element(By.XPATH, "//input[@id='uploadFile']")
    uploaded_file_name = file_name_field.get_attribute("value")
    assert uploaded_file_name == "c:/lab/file.txt", f"Ожидаемое имя файла: 'c:/lab/file.txt', но найдено: '{uploaded_file_name}'"

    # 6. Проверить в поле с полным именем директории имя всего пути
    # Проверяем, что в поле действительно полный путь
    assert uploaded_file_name == file_path, f"Ожидаемый полный путь: '{file_path}', но найдено: '{uploaded_file_name}'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
