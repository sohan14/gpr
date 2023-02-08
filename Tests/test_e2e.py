
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.common.alert import Alert

from TestData.crlink import Cardlink
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    #batchnum='resultsfiles.csv'
    @pytest.mark.default
    def test_e2e(self):

        log = self.getLogger()
        xdata = self.get_data('user')
        ydata=self.get_data("db")
        db=ydata[0]

        data = xdata[0]
        data2 = xdata[1]
        apidata= self.get_api('api')[0]
        apidata_timer = self.get_api('api')[1]

        options = webdriver.ChromeOptions()
        options.add_argument('--allow-insecure-localhost')  # differ on driver version. can ignore.
        caps = options.to_capabilities()
        caps["acceptInsecureCerts"] = True


        driver =webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps)
        driver.maximize_window()



        log.info(f"Logging to {data['link']}")

        driver.get(data['link'])

        time.sleep(5)




        driver.find_element(By.ID,"userName").send_keys(data['username'])
        driver.find_element(By.ID,"password").send_keys(data['password'])
        driver.find_element(By.ID, "Submit").click()
        time.sleep(5)
        log.info("Login successfully with MO")
        driver.switch_to.frame("showframeLeft")
        driver.find_element(By.LINK_TEXT,"Prepaid").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,"Card issuance").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,"Request for Cards").click()

        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("showframe")
        time.sleep(3)

        Select(driver.find_element(By.ID,"productId")).select_by_visible_text(data["productname"])
        time.sleep(1)

        driver.find_element(By.ID,"cardRequest").send_keys(int(data["noofcard"]))

        fl ,datat  = self.create_corp(data["productname"],int(data["noofcard"]),False)

        log.info(f'Generating {int(data["noofcard"])} cards for {data["productname"]}')
        log.info(f"CSV file location {fl}")
        driver.find_element(By.ID,"fileName").send_keys(fl)
        time.sleep(5)
        try:
            if data['isPersonalised']=="Yes":
                driver.find_element(By.ID,"isPersonalizedYes").click()
            elif data['isPersonalised']=="No":
                driver.find_element(By.ID,"isPersonalizedNo").click()

        except:
            pass
        driver.find_element(By.ID, "Submit").click()
        time.sleep(5)
        batch = driver.find_element(By.ID,"myText").text
        log.info(batch)

        temp=batch.split(":")

        temp1= temp[1].replace(" ","").split(",")
        print(temp1)
        batchnum=temp1[0]
        res=500
        try:
            res=self.req(apidata['card_requisition'],apidata_timer["card_requisition"])
        except:
            pass

        if res==200:
            print("Success")
        else:
            res = self.req(apidata['card_requisition'],apidata_timer["card_requisition"])

        assert res==200
        log.info(f"Card Requistion API call is success with response code {res}")
        try:
            res = self.req(apidata['topup'],apidata_timer["topup"])
        except:
            pass

        if res == 200:
            print("Success")
        else:
            res = self.req(apidata['topup'],apidata_timer["topup"])

        if res==200:
            log.info(f"Top up api successs with resonsecode {res}")
        time.sleep(5)
        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("showframeLeft")
        driver.find_element(By.LINK_TEXT, "View Batch Summary Details").click()
        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame("showframe")
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@type='text']").send_keys(batchnum)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,batchnum).click()
        # driver.find_element(By.ID,"batchNo").send_keys(batchnum)
        # driver.find_element(By.ID, "Submit").click()
        time.sleep(2)
        bn=driver.find_element(By.ID, "txtHint1").text
        log.info(bn)

        time.sleep(4)
        assert bn == f"File Processing Finished. , Success Count = {int(data['noofcard'])} , Failure Count = 0"
        driver.switch_to.default_content()
        driver.switch_to.frame("header")
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(5)
        log.info("Logout done from MO User")
        # data2=self.get_data("houser")
        driver.get(data2['link'])
        time.sleep(5)
        driver.find_element(By.ID, "userName").send_keys(data2["username"])
        driver.find_element(By.ID, "password").send_keys(data2["password"])
        driver.find_element(By.ID, "Submit").click()
        time.sleep(5)
        log.info("Login succesful with HO")
        driver.switch_to.frame("showframeLeft")
        driver.find_element(By.LINK_TEXT, "Prepaid").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Card issuance").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Approve/Reject Card Request").click()

        time.sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("showframe")
        time.sleep(3)
        driver.find_element(By.ID, "batchNo").send_keys(batchnum)
        time.sleep(2)
        driver.find_element(By.ID, "Submit").click()
        time.sleep(2)
        driver.find_element(By.ID, "comments").send_keys("hiiiiii")
        time.sleep(1)
        driver.find_element(By.ID, "accept").click()
        t1=driver.find_element(By.ID, "myText").text
        assert t1=="Card request approved successfully"
        log.info(f"Approve/Reject card request--{t1} ")
        try:
            res = self.req(apidata['card_generation'],apidata_timer["card_generation"])
        except:
            pass

        if res == 200:
            print("Card gen Success")
        else:
            # res = self.card_req()
            res = self.req(apidata['card_generation'],apidata_timer["card_generation"])
            time.sleep(2)
        log.info(f'Response code for Card generation API is {res}')
        log.info(datat['cardtype'])

        # res = self.embossa_gen()
        if datat['cardtype']== "Physical Card":
            log.info(apidata['gprembosa'])
            try:
                res = self.req(apidata['gprembosa'],apidata_timer['gprembosa'])
            except:
                log.info("Except embossa1")
            #log.info(f'Response code for embossa generation API is {res}')
            if res == 200:
                print("embossa Success")
            else:
                # res = self.card_req()
                res = self.req(apidata['gprembosa'],apidata_timer['gprembosa'])
                log.info(res)
                time.sleep(2)
            log.info(f'Response code for embossa generation API is {res}')

            time.sleep(5)
            time.sleep(1)
            modispatchdetail= True
            def modisdet():
                try:
                    driver.switch_to.default_content()
                    driver.switch_to.frame("showframeLeft")
                    driver.find_element(By.LINK_TEXT, "MO dispatch details").click()
                    time.sleep(2)

                    driver.switch_to.default_content()
                    driver.switch_to.frame("showframe")
                    time.sleep(5)
                    driver.find_element(By.XPATH,"//input[@type='text']").send_keys(batchnum)
                    time.sleep(3)
                    driver.find_element(By.ID, "checkbox").click()
                    driver.find_element(By.ID, "csv").click()
                    time.sleep(4)
                    log.info('CSV downloaded successfully')
                    #driver.find_element(By.ID, "csv").click()

                    time.sleep(5)
                    time.sleep(1)

                    return False
                except:
                    return True
            while modispatchdetail:
                try:
                    res = self.req(apidata['gprembosa'], apidata_timer['gprembosa'])
                    log.info(res)
                except:
                    log.info("except")
                log.info(modispatchdetail)
                time.sleep(5)
                modispatchdetail = modisdet()
                log.info(modispatchdetail)



            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "MO Dispatch File Upload").click()
            time.sleep(2)

            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(5)

            cs =self.cr_file()
            log.info(f"CSV Path {cs}")
            driver.find_element(By.ID,"file").send_keys(cs)
            time.sleep(3)
            driver.find_element(By.NAME,"submit").click()
            alert = Alert(driver)
            alert.accept()
            time.sleep(4)
            t2= driver.find_element(By.ID,"myText").text

            log.info(f'MO FILE DISPATCH RESPONSE : {t2}')
            assert t2=="File uploaded successfully with Total Count : 1 and Success Count : 1 and Rejected Count : 0"





            driver.switch_to.default_content()
            driver.switch_to.frame("header")
            driver.find_element(By.LINK_TEXT, "Logout").click()
            log.info("Logput Done From HO User")
            driver.get(data['link'])
            time.sleep(5)
            driver.find_element(By.ID, "userName").send_keys(data['username'])
            driver.find_element(By.ID, "password").send_keys(data['password'])
            driver.find_element(By.ID, "Submit").click()
            time.sleep(5)
            log.info("login succesfull with MO")
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "Prepaid").click()
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, "Card issuance").click()
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, "MO Card Acknowledge").click()

            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)




            driver.find_element(By.XPATH, "//input[@type='text']").send_keys(batchnum)
            time.sleep(5)
            driver.find_element(By.ID, "checkbox").click()
            time.sleep(2)
            driver.find_element(By.ID, "cardAck").click()

            time.sleep(5)
            t= driver.find_element(By.ID, "myText1").text
            assert  t== "Cards acknowledged successfully"
            log.info(t)



            driver.switch_to.default_content()
            driver.switch_to.frame("header")
            driver.find_element(By.LINK_TEXT, "Logout").click()
            time.sleep(5)
            log.info("LogOut done from MO User")

            f = self.get_crn(batchnum,db)
            #print(int(data["noofcard"]))
            dil =self.create_corp('apidata',int(data["noofcard"]),True)
            log.info(f'fetching data for API {dil}')
            #
            #
            #
            cr= Cardlink()
            #
            d=cr.convd(f)
            log.info(d)
            #

            def test_link(get_data,x):
                #print(get_data)
                log.info(apidata["Cardlink"])
                a,b=self.cr_link(get_data,x,apidata["Cardlink"])
                #print(a)
                if a==200:
                    print("link sucess")
                else:
                    a,b=self.cr_link(get_data,x,apidata["Cardlink"])
                return a ,b

            def test_ac(get_data,x):
                #print(get_data)
                log.info(apidata["CardActivate"])
                a,b = self.cr_ac(get_data,x,apidata["CardActivate"])
                #print(a)
                if a == 200:
                    print("link sucess")
                else:
                    a,b=self.cr_ac(get_data,x,apidata["CardActivate"])
                return a,b
            assert len(d) == len(dil)

            for n in range(int(len(dil))):
                a,b= test_link(d[n]['card_ref_number'],dil[n])
                log.info(f"CARD LINK ---{d[n]['card_ref_number']}-----{a}-----{b}")

                a,b=test_ac(d[n]['card_ref_number'],dil[n])
                log.info(f"CARD ACTIVATE ---{d[n]['card_ref_number']}-----{a}-----{b}")
        else:
            driver.switch_to.default_content()
            driver.switch_to.frame("header")
            driver.find_element(By.LINK_TEXT, "Logout").click()
            log.info("Logput Done From HO User")
            f = self.get_crn(batchnum,db)
            print(int(data["noofcard"]))
            dil = self.create_corp('apidata', int(data["noofcard"]), True)
            log.info(f'fetching data for API {dil}')
            #
            #
            #
            cr = Cardlink()
            #
            d = cr.convd(f)
            log.info(d)

            #

            def test_link(get_data, x):
                #print(get_data)
                log.info(apidata["Cardlink"])
                a, b = self.cr_link(get_data, x)
                #print(a)
                if a == 200:
                    print("link sucess")
                else:
                    a, b = self.cr_link(get_data, x)
                return a, b

            def test_ac(get_data, x):
                #print(get_data)
                log.info(apidata["CardActivate"])
                a, b = self.cr_ac(get_data, x,apidata["CardActivate"])
                #print(a)
                if a == 200:
                    print("link sucess")
                else:
                    a, b = self.cr_ac(get_data, x,apidata["CardActivate"])
                return a, b

            assert len(d) == len(dil)

            for n in range(int(len(dil))):
                a, b = test_link(d[n]['card_ref_number'], dil[n])
                log.info(f"CARD LINK ---{d[n]['card_ref_number']}-----{a}-----{b}")

                a, b = test_ac(d[n]['card_ref_number'], dil[n])
                log.info(f"CARD ACTIVATE ---{d[n]['card_ref_number']}-----{a}-----{b}")






