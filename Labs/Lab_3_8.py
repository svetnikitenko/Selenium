
"""Написать 8 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Forms'
3. Выбрать пункт 'Practice Form'
4. Заполнить поля Name
5. Заполнить поле Email валидным значение
6. Выбрать Gender
7. Заполнить поле Mobile валидным значением
8. Заполнить поле Date of Birth
9. Выбрать в поле Subject 3 любых значения
10. Выбрать Hobbies
11. Заполнить Current Addres
12. Выбрать State and City
13. Нажать Submit
14. Проверить что в открывшимся окне есть введенные данные.
15. Нажать Close"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Настройка драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    # 1. Перейти на страницу https://demoqa.com/
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    # 2. Перейти в раздел 'Forms'
    forms_section = driver.find_element(By.XPATH, "//h5[text()='Forms']")
    forms_section.click()

    # 3. Выбрать пункт 'Practice Form'
    practice_form_option = driver.find_element(By.XPATH, "//span[text()='Practice Form']")
    practice_form_option.click()

    # 4. Заполнить поля Name
    first_name_input = driver.find_element(By.XPATH, "//input[@id='firstName']")
    first_name_input.send_keys("Svetlana")

    last_name_input = driver.find_element(By.XPATH, "//input[@id='lastName']")
    last_name_input.send_keys("Nikitenko")

    # 5. Заполнить поле Email валидным значением
    email_input = driver.find_element(By.XPATH, "//input[@id='userEmail']")
    email_input.send_keys("svetlananikitenko@mail.ru")

    # 6. Выбрать Gender
    gender_radio_button = driver.find_element(By.XPATH, "//label[text()='Female']")
    gender_radio_button.click()

    # 7. Заполнить поле Mobile валидным значением
    mobile_input = driver.find_element(By.XPATH, "//input[@id='userNumber']")
    mobile_input.send_keys("7999000000")

    # 8. Заполнить поле Date of Birth
    date_of_birth_input = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
    date_of_birth_input.click()
    date_of_birth_input.send_keys(Keys.CONTROL + "a")
    date_of_birth_input.send_keys("05 Feb 1984")
    date_of_birth_input.send_keys(Keys.ENTER)

    # 9. Выбрать в поле Subject 3 любых значения
    subject_input = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
    subject_input.send_keys("English")
    subject_input.send_keys(Keys.ENTER)
    subject_input.send_keys("Arts")
    subject_input.send_keys(Keys.ENTER)
    subject_input.send_keys("Biology")
    subject_input.send_keys(Keys.ENTER)

    # 10. Выбрать Hobbies
    hobbies_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
    hobbies_checkbox.click()

    # 11. Заполнить Current Address
    current_address_input = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    current_address_input.send_keys("Omsk, Lenina 1")

    # 12. Выбрать State and City
    state_dropdown = driver.find_element(By.XPATH, "//div[@id='state']")
    state_dropdown.click()
    state_option = driver.find_element(By.XPATH, "//div[text()='NCR']")
    state_option.click()

    city_dropdown = driver.find_element(By.XPATH, "//div[@id='city']")
    city_dropdown.click()
    city_option = driver.find_element(By.XPATH, "//div[text()='Delhi']")
    city_option.click()

    # 13. Нажать Submit
    submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    submit_button.click()

    # 14. Проверить, что в открывшемся окне есть введенные данные
    modal_dialog = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']"))
    )
    modal_text = modal_dialog.text
    assert "Svetlana Nikitenko" in modal_text, "Имя не найдено в результатах."
    assert "svetlananikitenko@mail.ru" in modal_text, "Email не найден в результатах."
    assert "7999000000" in modal_text, "Мобильный номер не найден в результатах."
    assert "English, Arts, Biology" in modal_text, "Предметы не найдены в результатах."
    assert "Sports" in modal_text, "Хобби не найдено в результатах."
    assert "Omsk, Lenina 1" in modal_text, "Адрес не найден в результатах."
    assert "NCR Delhi" in modal_text, "Состояние и город не найдены в результатах."

    # 15. Нажать Close
    close_button = driver.find_element(By.XPATH, "//button[@id='closeLargeModal']")
    close_button.click()

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
