import os
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from colorama import Fore, Back, Style
from termcolor import colored
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
    #
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
        load_start_time = time.time()
        self.driver.get("https://www.woovly.com/")
        load_end_time = time.time()
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign Up/']"))).click()
        self.driver.implicitly_wait(10)
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Already a Member? Login']"))).click()
        self.driver.find_element_by_id("email_Id").send_keys("venkatesh.k@xelpmoc.in")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model ='loginPassword']"))).send_keys("78007200a")
        login_start_time = time.time()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@ id = 'signinFields']/div[3]").click()
        login_end_time = time.time()
        time.sleep(20)
        # navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        # responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        # domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        # backendPerformance = responseStart - navigationStart
        # frontendPerformance = domComplete - responseStart
        # print("Back End : {} ".format(backendPerformance))
        # print("Front End : {} ".format(frontendPerformance))
        #
        loadTime = load_end_time - load_start_time
        logInTime = login_end_time-login_start_time
        print("Time taken to from login to home page {}s ".format(logInTime))
        print("----------------------------------------")
        print("Time taken for the site to load landing page {}s".format(loadTime))
        self.driver.implicitly_wait(10)
        self.driver.close()


    def test_SearchAfterLogin(self):
        self.driver = webdriver.Chrome('../Test1/Driver /chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        load_start_time = time.time()
        self.driver.get("https://www.woovly.com/")
        load_end_time = time.time()
        self.driver.implicitly_wait(10)
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign Up/']"))).click()
        not_a_member= wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Already a Member? Login']")))
        not_a_member.click()
        self.driver.find_element_by_id("email_Id").send_keys("venkatesh.k@xelpmoc.in")
        wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@ng-model ='loginPassword']"))).send_keys("78007200a")
        login_start_time = time.time()
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@ id = 'signinFields']/div[3]").click()
        login_end_time = time.time()
        # getiitn elements after searching for travel
        # //*[@id="headerCnt"]/div[3]/div/div[3]/div[2]/input
        self.driver.implicitly_wait(10)
        # /html/body/div[1]/div[1]/div[7]/div[3]/div/div[2]/div[1]/div[3]/input
        self.driver.find_element_by_xpath('//*[@id="headerCnt"]/div[3]/div/div[3]/div[2]/input').send_keys('Travel')
        start_time = time.time()
        try:
            wait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='headerCnt']/div[3]/div/div[3]/div[2]/div/div[3]/div[1]/div[2]/a[3]/div")))
        except TimeoutException:
            pass
        
        # self.driver.find_element_by_xpath("//*[@id='headerCnt']/div[3]/div/div[3]/div[2]/div/div[3]/div[1]/div[2]/a[3]/div").click()

        # wait(self.driver,10).until(EC.visibility_of_element_located(By.XPATH,"//*[@id='headerCnt']/div[3]/div/div[3]/div[2]/div/div[3]/div[1]/div[2]/a[3]/div")).click()
        stop_time = time.time()
        # navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        # responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        # domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        # backendPerformance = responseStart - navigationStart
        # frontendPerformance = domComplete - responseStart
        # print("Back End : {} ms".format(backendPerformance))
        # print("Front End : {} ms".format(frontendPerformance))
        logInTime = login_end_time-login_start_time
        loadTime = load_end_time - load_start_time
        SearchTime = stop_time - start_time

        if start_time < 8 :
            print("Time taken for the search to load {}s ".format(SearchTime))
        else:
            print("Time taken for the search to load {}s ".format(SearchTime))
        print('------------------')
        print("Time taken for the site to load landing page {}s".format(loadTime))
        print('------------------')
        print("Time taken to from login to home page {}s ".format(logInTime))
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