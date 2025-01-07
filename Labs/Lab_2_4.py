"""Написать 4 тест
1. Перейти на страницу https://demoqa.com/
2. Перейти в раздел 'Elements'
3. Выбрать пункт 'Buttons'
4. Нажать на кнопку Click Me
5. Проверить что появилась надпись You have done a dynamic click
6. Сделать двойной клик на кнопку Double Click Me
7. Проверить что появилась надпись You have done a double click
8. Сделать клик правой кнопкой кнопку Right Click Me
9. Проверить что появилась надпись You have done a right click
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

    # 3. Выбрать пункт 'Buttons'
    buttons_option = driver.find_element(By.XPATH, "//span[text()='Buttons']")
    buttons_option.click()

    # 4. Нажать на кнопку Click Me
    click_me_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    click_me_button.click()

    # 5. Проверить, что появилась надпись You have done a dynamic click
    dynamic_click_text = driver.find_element(By.XPATH, "//p[@id='dynamicClickMessage']")
    assert dynamic_click_text.text == "You have done a dynamic click", "Сообщение о динамическом клике отсутствует"

    # 6. Сделать двойной клик на кнопку Double Click Me
    double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    actions = ActionChains(driver)
    actions.double_click(double_click_button).perform()

    # 7. Проверить, что появилась надпись You have done a double click
    double_click_text = driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']")
    assert double_click_text.text == "You have done a double click", "Сообщение о двойном клике отсутствует"

    # 8. Сделать клик правой кнопкой на кнопку Right Click Me
    right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    actions.context_click(right_click_button).perform()

    # 9. Проверить, что появилась надпись You have done a right click
    right_click_text = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
    assert right_click_text.text == "You have done a right click", "Сообщение о правом клике отсутствует"

    print("Тест успешно выполнен!")

finally:
    # Закрыть браузер
    driver.quit()
