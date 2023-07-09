import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari()

    def test_search_on_google(self):
        # Открываем веб-браузер Safari
        driver = self.driver
        driver.get("https://www.google.com")
        # Проверяем, что заголовок страницы содержит слово "Google"
        self.assertIn("Google", driver.title)
        time.sleep(5)
        # Находим элемент страницы с именем "q" (строка поиска)
        elem = driver.find_element(By.NAME, "q")
        time.sleep(5)
        # Вводим слово "python" в найденный элемент (строку поиска)
        elem.send_keys("python")
        time.sleep(5)
      
        elem.submit()
        time.sleep(5)
        # Проверяем, что на странице с результатами поиска отсутствует строка No results found
        self.assertNotIn("No results found", driver.page_source)

    def test_button(self):
        # Открываем браузер Safari
        driver = self.driver
        # Переходим на страницу
        driver.get("https://www.google.com")
        # Находим все кнопки на странице
        buttons = driver.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            # Проверяем, что кнопка отображается на странице
            if button.is_displayed():
                self.assertTrue(True, f"Button '{button.text}' is displayed")
            else:
                self.assertFalse(True, f"Button '{button.text}' is not displayed")

    def tearDown(self):
        # Закрываем веб-браузер Safari
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
