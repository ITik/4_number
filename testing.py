from selenium import webbrowser
import unittest
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://rasp.yandex.ru')

    def test_01 (self):
        driver = self.driver
        input_field = driver.find_element_by_id('from')
        input_field.send_keys('Кемерово')
        input_field = driver.find_element_by_id('to')
        input_field.send_keys('Москва')
        input_field = driver.find_element_by_id('when')
        input_field.send_keys('7 июля')
        input_field.send_keys(Keys.ENTER)

        k = 0
        for title in titles:
            self.assertIsNone(driver.find_elements_by_class('SegmentTitle__number'))
            self.assertIsNone(driver.find_elements_by_class('SearchSegment__duration'))
            k = k+1
        self.assertEqual(5, k)


    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_id('from')
        input_field.send_keys('Кемерово проспект Ленина')
        input_field = driver.find_element_by_id('to')
        input_field.send_keys('Кемерово Бакинский переулок')
        input_field = driver.find_element_by_id('when')
        input_field.send_keys('среда')
        input_field = driver.find_element_by_data-code('bus')
        input_field.send_keys(Keys.driver.find_element_by_class('Button__title'))

    def tearDown(self):
        sel.driver.quit()



