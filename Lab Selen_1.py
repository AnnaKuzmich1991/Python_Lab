import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Safari при начале каждого теста
        self.driver = webdriver.Safari()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q (строка поиска)
        # (откройте вручную в любом браузере сайт http://www.python.org,
        # нажмите правой кнопкой мыши по строке поиска,
        # выберите пункт "просмотреть код",
        # убедитесь, что у этого элемента name="q")
        elem = driver.find_element(By.NAME, "q")
        # ждем 5 секунд
        time.sleep(5)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("chupakabra")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("No results found.", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q
        # на обновленной странице
        elem = driver.find_element(By.NAME, "q")
        # очищаем строку поиска
        elem.clear()
        # ждем 5 секунд
        time.sleep(5)
        # набор слова pycon в найденном элементе
        elem.send_keys("pycon")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("No results found.", driver.page_source)

    def test_button(self):
        driver = self.driver
        driver.get("http://www.python.org")

        # Проверка наличия кнопок:
        buttons = driver.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            self.assertTrue(button.is_displayed())

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
