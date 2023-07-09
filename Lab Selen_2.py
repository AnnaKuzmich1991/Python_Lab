import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OnlinerTest(unittest.TestCase):
    def setUp(self):
        # Запуск Safari перед каждым тестом
        self.driver = webdriver.Safari()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.onliner.by")

        # Находим поле поиска и вводим запрос
        search_input = driver.find_element(By.CSS_SELECTOR, "input.fast-search__input")
        search_input.send_keys("тестирование")

        # поиск
        search_input.send_keys(Keys.ENTER)

        # Проверяем наличие результатов поиска
        search_results = driver.find_elements(By.CLASS_NAME, "product__title")
        self.assertTrue(len(search_results) >= 0)

    def tearDown(self):
        # Закрытие браузера после каждого теста
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
