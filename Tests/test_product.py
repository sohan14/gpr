from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.common.alert import Alert

from TestData.crlink import Cardlink
from Utilities.BaseClass import BaseClass
from Utilities.product import product


class TestProduct(BaseClass):

    @pytest.mark.default
    def test_login(self):
        log = self.getLogger()
        xdata = self.get_data_product('user')



        data = xdata[0]
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-insecure-localhost')  # differ on driver version. can ignore.
        caps = options.to_capabilities()
        caps["acceptInsecureCerts"] = True

        driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps)
        driver.maximize_window()
        if int(data['noOfsteps'])>0:
            log.info(f"Logging to {data['link']}")

            driver.get(data['link'])

            time.sleep(5)

            driver.find_element(By.ID, "userName").send_keys(data['username'])
            driver.find_element(By.ID, "password").send_keys(data['password'])
            driver.find_element(By.ID, "Submit").click()
            time.sleep(5)
            log.info("Login successfully ")
            time.sleep(2)
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Product Setup").click()
            time.sleep(2)

            prod = product()
            steps= self.product_clean(re="steps",times=int(data["noOfsteps"]))

            for n in range(0,int(data["noOfsteps"])):
                log.info(f' {n} {steps["steps"][n]} {int(steps["times"][n])}')
                tmpsheet = self.product_clean(re=steps["steps"][n],times=int(steps["times"][n]))
                for i in range(0,int(steps["times"][n])):
                    log.info(f' {n} {steps["steps"][n]} {i+1}')
                    prod.xstate(driver,tmpsheet,i,steps["steps"][n],log)


            driver.switch_to.default_content()
            driver.switch_to.frame("header")
            driver.find_element(By.LINK_TEXT, "Logout").click()
            log.info("Logout Done")


        if data['checker']=="Yes":


            ydata = self.get_data_product('checker')
            data = ydata[0]
            driver.get(data['link'])
            time.sleep(5)
            times=  len(ydata)
            driver.find_element(By.ID, "userName").send_keys(data['username'])
            driver.find_element(By.ID, "password").send_keys(data['password'])
            driver.find_element(By.ID, "Submit").click()
            time.sleep(5)
            log.info("Login successfully ")
            time.sleep(2)
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "Product Setup").click()
            time.sleep(2)

            for i in range(0,times):

                time.sleep(3)
                if i>0:
                    driver.switch_to.default_content()
                    driver.switch_to.frame("showframeLeft")
                driver.find_element(By.LINK_TEXT, "Product Configuration Maker/Checker").click()
                driver.switch_to.default_content()
                driver.switch_to.frame("showframe")
                time.sleep(2)
                try:
                    driver.find_element(By.XPATH,"//input[@type='text']").click()
                    driver.find_element(By.XPATH,"//input[@type='text']").clear()
                    time.sleep(2)
                    driver.find_element(By.XPATH,"//input[@type='text']").send_keys(ydata[i]["product"])
                    time.sleep(5)
                    driver.find_element(By.LINK_TEXT ,ydata[i]["product"]).click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"Submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"Submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"submit").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"Approve").click()
                    time.sleep(2)
                    driver.find_element(By.ID,"remark").click()

                    driver.find_element(By.ID,"remark").clear()

                    driver.find_element(By.ID,"remark").send_keys("good")
                    self.accept_next_alert = True
                    driver.find_element(By.ID,"updateActionStatusForProductConfig").click()
                    if ydata[i]["status"]=="Approve":

                        driver.find_element(By.ID,"Approve").click()
                        time.sleep(2)
                    elif ydata[i]["status"]=="Reject":
                        driver.find_element(By.ID,"Reject").click()
                        time.sleep(2)

                    alert = Alert(driver)

                    alert.accept()
                    time.sleep(10)

                    try:
                        a = driver.find_element(By.ID, "txtHintNew").text
                        log.info(a)
                    except:
                        pass

                    try:
                        a = driver.find_element(By.ID, "txtHint").text
                        log.info(a)
                    except:
                        pass

                    try:
                        a = driver.find_element(By.ID, "myText").text
                        log.info(a)
                    except:
                        pass
                except Exception as e:
                    log.info(e)

            driver.switch_to.default_content()
            driver.switch_to.frame("header")
            driver.find_element(By.LINK_TEXT, "Logout").click()
            log.info("Logout Done")







