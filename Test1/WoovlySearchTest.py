import os
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

class WoovlyTest(unittest.TestCase):

    @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome('../Test1/Driver /chromedriver')
    #     cls.driver.implicitly_wait(5)
    #     cls.driver.maximize_window()

    def test_search_woovlyLandingPage(self):
        self.driver = webdriver.Chrome('../Test1/Driver /chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.woovly.com/")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign Up/']"))).click()
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        print("Back End : {} ".format(backendPerformance))
        print("Front End : {} ".format(frontendPerformance))
        time.sleep(10)
        self.driver.close()

    def test_login(self):
        self.driver = webdriver.Chrome('../Test1/Driver /chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = {'browser': 'ALL'}
        self.driver.get("https://www.woovly.com/")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign Up/']"))).click()
        self.driver.implicitly_wait(10)
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Already a Member? Login']"))).click()
        self.driver.find_element_by_id("email_Id").send_keys("venkatesh.k@xelpmoc.in")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model ='loginPassword']"))).send_keys("78007200a")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@ id = 'signinFields']/div[3]").click()
        time.sleep(20)
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        print("Back End : {} ".format(backendPerformance))
        print("Front End : {} ".format(frontendPerformance))

        for entry in self.driver.get_log('browser'):
            print(entry)
        self.driver.implicitly_wait(10)
        self.driver.close()


    def test_SearchAfterLogin(self):
        self.driver = webdriver.Chrome('../Test1/Driver /chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        self.driver.get("https://www.woovly.com/")
        self.driver.implicitly_wait(10)
        element = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign Up/']")))
        element.click()
        not_a_member= wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Already a Member? Login']")))
        not_a_member.click()
        self.driver.find_element_by_id("email_Id").send_keys("venkatesh.k@xelpmoc.in")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model ='loginPassword']"))).send_keys("78007200a")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@ id = 'signinFields']/div[3]").click()
        time.sleep(20)



        # getiitn elements after searching for travel
        self.driver.find_element_by_xpath('//*[@id="headerCnt"]/div[3]/div/div[3]/div[2]/input').send_keys('Travel')
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        print("Back End : {} ".format(backendPerformance))
        print("Front End : {} ".format(frontendPerformance))
        self.driver.implicitly_wait(15)
        self.driver.close()


    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(10)
    #     cls.driver.close()
    #     cls.driver.quit()
    #     print("Test Completed ")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Test1/Reports'))

    #