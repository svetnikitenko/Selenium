"""Написать 18 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Widgets'
3. Выбрать пункт 'Tabs'
4. Открыть вкладку What
5. Проверить что на ней есть текст
6. Открыть вкладку Origin
7. Проверить что на ней есть текст
8. Открыть вкладку Use
9. Проверить что на ней есть текст
10. Проверить что вкладка More недоступна"""

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
    widgets_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']"))
    )
    widgets_section.click()

    # 3. Выбрать пункт 'Tabs'
    tabs_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Tabs']"))
    )
    tabs_option.click()

    # 4. Открыть вкладку What
    what_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='demo-tab-what']"))
    )
    what_tab.click()

    # 5. Проверить, что на ней есть текст
    what_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='demo-tabpane-what']"))
    ).text
    assert what_content.strip(), "Текст на вкладке 'What' отсутствует"

    # 6. Открыть вкладку Origin
    origin_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='demo-tab-origin']"))
    )
    origin_tab.click()

    # 7. Проверить, что на ней есть текст
    origin_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='demo-tabpane-origin']"))
    ).text
    assert origin_content.strip(), "Текст на вкладке 'Origin' отсутствует"

    # 8. Открыть вкладку Use
    use_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='demo-tab-use']"))
    )
    use_tab.click()

    # 9. Проверить, что на ней есть текст
    use_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='demo-tabpane-use']"))
    ).text
    assert use_content.strip(), "Текст на вкладке 'Use' отсутствует"

    # 10. Проверить, что вкладка More недоступна
    more_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@id='demo-tab-more']"))
    )
    assert "disabled" in more_tab.get_attribute("class"), "Вкладка 'More' доступна, хотя должна быть отключена"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
