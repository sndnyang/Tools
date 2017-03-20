# coding=utf-8 
import re
import json
import unittest
import traceback

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from colortest import ColorTestRunner

import sys

reload(sys)
sys.setdefaultencoding('utf-8') 

class ProcessTestCase(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
        self.browser = webdriver.Chrome(chrome_options=options)
      # self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    # 退出清理工作
    def tearDown(self):
        pass

    # 具体的测试用例，一定要以test开头
    def test_process(self):
        browser = self.browser
        browser.get('http://localhost:5000/tutorial/2236d636-85e7-467d-a627-58feb9c21cdc')

        #button = browser.find_element_by_xpath('//*[@id="tutorial"]/div[3]/div/div/button')
        action = ActionChains(browser)
        browser.find_element_by_class_name("small_step").send_keys(u'前向传播')
        button = browser.find_element_by_css_selector('#tutorial>div.lesson.lesson2>div>div>button')
        # jcode = button.get_attribute("onclick")
        # browser.execute_script(jcode)
        # browser.execute_script('$("#tutorial>div.lesson.lesson2>div>div>button").click()')
        hover = ActionChains(browser).move_to_element(button)
        hover.perform()
        button.click()
        print "Button is clicked at time: " + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        
        wait.until(lambda driver: browser.execute_script("return jQuery.active == 0"))
        print "Ajax request is completed at time: " + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.assertEqual(True, True, "easiest case")
        
   

if __name__=='__main__':
    #unittest.main(testRunner = ColorTestRunner())
    unittest.main()
