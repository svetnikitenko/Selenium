"""Написать 14 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Accordian'
4. Раскрыть аккордион 'What is Lorem Ipsum?'
5. Проверить наличие текста
6. Раскрыть аккордион 'Where does it come from?'
7. Проверить наличие текста
8. Раскрыть аккордион 'Why do we use it?'
9. Проверить наличие текста"""

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

    # 2. Перейти в раздел 'Widgets'
    widgets_section = driver.find_element(By.XPATH, "//h5[text()='Widgets']")
    widgets_section.click()

    # 3. Выбрать пункт 'Accordian'
    accordian_option = driver.find_element(By.XPATH, "//span[text()='Accordian']")
    accordian_option.click()

    # 4. Раскрыть аккордион 'What is Lorem Ipsum?'
    first_accordion = driver.find_element(By.XPATH, "//div[@id='section1Heading']")
    first_accordion.click()

    # 5. Проверить наличие текста
    first_accordion_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='section1Content']/p"))
    ).text
    assert "Lorem Ipsum" in first_accordion_text, f"Текст не найден в первом аккордионе: '{first_accordion_text}'"

    # 6. Раскрыть аккордион 'Where does it come from?'
    second_accordion = driver.find_element(By.XPATH, "//div[@id='section2Heading']")
    second_accordion.click()

    # 7. Проверить наличие текста
    second_accordion_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='section2Content']/p"))
    ).text
    assert "Contrary to popular belief" in second_accordion_text, f"Текст не найден во втором аккордионе: '{second_accordion_text}'"

    # 8. Раскрыть аккордион 'Why do we use it?'
    third_accordion = driver.find_element(By.XPATH, "//div[@id='section3Heading']")
    third_accordion.click()

    # 9. Проверить наличие текста
    third_accordion_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='section3Content']/p"))
    ).text
    assert "It is a long established fact" in third_accordion_text, f"Текст не найден в третьем аккордионе: '{third_accordion_text}'"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
