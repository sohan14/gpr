from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

class product:

    def xstate(self,driver,balance,i,name,log):
        if name=="balanceProfile":
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "Balance Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID, "name").click()
                driver.find_element(By.ID, "name").send_keys(balance["profilename"][i])
                driver.find_element(By.ID, "offlineBal").click()
                Select(driver.find_element(By.ID, "offlineBal")).select_by_visible_text(balance["OfflineBalanceActive"][i])
                Select(driver.find_element(By.ID, "offlineUpdateOnHost")).select_by_visible_text(
                    balance["OfflineUpdateOn HostActive"][i])
                Select(driver.find_element(By.ID, "autoTopUpMech")).select_by_visible_text(balance["AutoMoneyAddMechanism"][i])

                driver.find_element(By.ID, "autoTopUpVal").click()
                driver.find_element(By.ID, "autoTopUpVal").clear()
                driver.find_element(By.ID, "autoTopUpVal").send_keys(balance["AutoMoneyAddValue"][i])

                driver.find_element(By.ID, "minThreshold").send_keys(balance["MinimumThreshold"][i])
                driver.find_element(By.ID, "maxOffLineLimit").click()
                driver.find_element(By.ID, "maxOffLineLimit").clear()
                driver.find_element(By.ID, "maxOffLineLimit").send_keys(balance["MaximumOfflineLimit"][i])
                if balance["Offlinewalletchip"][i] == "Yes":
                    driver.find_element(By.ID, "offlineStatementAllowedYes").click()
                else:
                    driver.find_element(By.ID, "offlineStatementAllowedNo").click()
                driver.find_element(By.ID, "name").click()
                driver.find_element(By.ID, "Submit").click()
                time.sleep(5)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                try:
                    a=driver.find_element(By.ID, "nameSpan").text
                    log.info(a)
                except:
                    pass
                try:
                    a=driver.find_element(By.ID, "txtHint").text
                    log.info(a)
                except:
                    pass

                try:
                    a = driver.find_element(By.ID, "myText").text
                    log.info(a)
                except:
                    pass
            except Exception as e:
                log.info(f'{balance["profilename"][i]} is failed \n {e}')





        elif name=="binProfile":

            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Bin Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH,"//form[@id='command']/button").click()
                driver.find_element(By.ID,"binProfileName").click()
                driver.find_element(By.ID,"binProfileName").send_keys(balance["NetworkScheme"][i])
                driver.find_element(By.ID,"binProfileDesc").click()
                driver.find_element(By.ID,"binProfileDesc").send_keys(balance["ISBinNCMCenable"][i])
                driver.find_element(By.ID,"bin").click()
                driver.find_element(By.ID,"bin").send_keys(int(balance["Bin"][i]))
                driver.find_element(By.ID,"binTypeNetworkScheme").click()
                Select(driver.find_element(By.ID,"binTypeNetworkScheme")).select_by_visible_text(balance["Network Scheme"][i])
                Select(driver.find_element(By.ID,"isNCMCEnable")).select_by_visible_text(balance["IS Bin NCMC enable"][i])
                Select(driver.find_element(By.ID,"cardType")).select_by_visible_text(balance["InstrumentType"][i])
                Select(driver.find_element(By.ID,"interface")).select_by_visible_text(balance["Interface"][i])
                Select(driver.find_element(By.ID,"embossaLine4")).select_by_visible_text(balance["Embossa Line 4"][i])
                driver.find_element(By.ID,"formDiv").click()
                Select(driver.find_element(By.ID,"activation")).select_by_visible_text(balance["Activation"][i])
                driver.find_element(By.ID,"expiry").click()
                driver.find_element(By.ID,"expiry").clear()
                driver.find_element(By.ID,"expiry").send_keys(int(balance["Expiry"][i]))
                Select(driver.find_element(By.ID,"pinGeneration")).select_by_visible_text(balance["PIN Generation"][i])
                driver.find_element(By.ID,"pinAttemptAllowed").click()
                driver.find_element(By.ID,"pinAttemptAllowed").clear()
                driver.find_element(By.ID,"pinAttemptAllowed").send_keys(int(balance["Pin Attempt Allowed"][i]))
                Select(driver.find_element(By.ID,"embossingMode")).select_by_visible_text(balance["Embossing Mode"][i])
                driver.find_element(By.ID,"minKyc").click()
                driver.find_element(By.ID,"minKyc").clear()
                driver.find_element(By.ID,"minKyc").send_keys(int(balance["Max Balance for Min KYC"][i]))
                driver.find_element(By.ID,"maxKyc").click()
                driver.find_element(By.ID,"maxKyc").clear()
                driver.find_element(By.ID,"maxKyc").send_keys(int(balance["Max Balance for Full KYC"][i]))
                driver.find_element(By.ID,"dorminancePeriod").click()
                driver.find_element(By.ID,"dorminancePeriod").clear()
                driver.find_element(By.ID,"dorminancePeriod").send_keys(int(balance["Dorminance Period"][i]))
                Select(driver.find_element(By.ID,"allowNegativeBalance")).select_by_visible_text(balance["Allow Negative Balance"][i])
                driver.find_element(By.ID,"serviceCode").click()
                driver.find_element(By.ID,"serviceCode").clear()
                driver.find_element(By.ID,"serviceCode").send_keys(int(balance["Service Code"][i]))
                Select(driver.find_element(By.ID,"ImageCode")).select_by_visible_text(str(int(balance["Image Code"][i])))
                Select(driver.find_element(By.ID,"currencyCode")).select_by_visible_text(balance["Currency Code"][i])
                Select(driver.find_element(By.ID,"region")).select_by_visible_text(balance["Region"][i])
                Select(driver.find_element(By.ID,"vendorId")).select_by_visible_text(balance["Card Perso Vendor name"][i])
                driver.find_element(By.ID,"subBinLengthId").click()
                driver.find_element(By.ID,"subBinLengthId").clear()
                driver.find_element(By.ID,"subBinLengthId").send_keys(int(balance["Sub Bin Length"][i]))
                driver.find_element(By.XPATH,"//div[@id='formDiv']/div[9]/div").click()
                time.sleep(5)
                driver.find_element(By.ID,"Submit").click()
                time.sleep(5)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                try:
                    a=driver.find_element(By.ID, "nameSpan").text
                    log.info(a)
                    a = driver.find_element(By.ID, "binSpan").text
                    log.info(a)
                except:
                    pass
                try:
                    a=driver.find_element(By.ID, "txtHint").text
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


        elif name=="feeProfile":
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Fee Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)

            try:
                driver.find_element(By.XPATH,"//form[@id='command']/button").click()
                driver.find_element(By.ID,"name").click()
                driver.find_element(By.ID,"name").clear()
                driver.find_element(By.ID,"name").send_keys(balance["Fee Profile Name"][i])
                driver.find_element(By.ID, "feeProfileDesc").click()
                driver.find_element(By.ID, "feeProfileDesc").click()
                driver.find_element(By.ID, "feeProfileDesc").clear()
                driver.find_element(By.ID, "feeProfileDesc").send_keys(balance["Fee Profile Desc"][i])

                for j in range(0,int(balance["subTimes"][i])):
                    driver.find_element(By.ID, "feeName").click()
                    driver.find_element(By.ID, "feeName").clear()
                    driver.find_element(By.ID, "feeName").send_keys(balance["Fee Name"][i].split("|")[j])

                    Select(driver.find_element(By.ID,"feeAmountType")).select_by_visible_text(str(balance["Fee Amount Type"][i]).split("|")[j])
                    driver.find_element(By.ID,"feeAmount").click()
                    driver.find_element(By.ID,"feeAmount").clear()
                    driver.find_element(By.ID,"feeAmount").send_keys(int(str(balance["Fee Amount"][i]).split("|")[j]))
                    Select(driver.find_element(By.ID,"feeType")).select_by_visible_text(balance["Fee Type"][i].split("|")[j])
                    driver.find_element(By.ID,"markupFeeAmount").click()
                    driver.find_element(By.ID,"markupFeeAmount").clear()
                    driver.find_element(By.ID,"markupFeeAmount").send_keys(int(str(balance["Markup Fee"][i]).split("|")[j]))
                    driver.find_element(By.XPATH,"//div[@id='formDiv']/div[3]/div[3]/div[2]").click()
                    if balance["Tax Inclusive"][i].split("|")[j]=="Yes":
                        driver.find_element(By.ID,"taxInclusive1").click()
                    else:
                        driver.find_element(By.ID,"taxInclusive2").click()
                    driver.find_element(By.XPATH,"//div[@id='formDiv']/div[3]/div[4]/div[2]").click()
                    if balance["Post in Queue"][i].split("|")[j]=="Yes":
                        driver.find_element(By.ID,"postInQueue1").click()
                    else:
                        driver.find_element(By.ID,"postInQueue2").click()

                    Select(driver.find_element(By.ID,"feeWaiverAppFrequency")).select_by_visible_text((str(balance["Fee Waiver Application Frequency"][i]).split("|")[j]))
                    driver.find_element(By.ID,"feeTxnWaiverCnt").click()
                    driver.find_element(By.ID,"feeTxnWaiverCnt").clear()
                    driver.find_element(By.ID,"feeTxnWaiverCnt").send_keys(int(str(balance["Fee Transaction Waiver Count"][i]).split("|")[j]))
                    driver.find_element(By.XPATH,"//div[@id='formDiv']/div[5]").click()
                    Select(driver.find_element(By.ID,"isGST")).select_by_visible_text(balance["Is GST Applicable"][i].split("|")[j])
                    time.sleep(2)
                    if balance["Is GST Applicable"][i].split("|")[j]=="Yes":
                        driver.find_element(By.ID,"gstAmt").click()
                        driver.find_element(By.ID,"gstAmt").clear()
                        driver.find_element(By.ID,"gstAmt").send_keys(balance["GST Amount in Percentage"][i].split("|")[j])
                    driver.find_element(By.XPATH,"//div[@id='formDiv']/div[5]").click()


                    driver.find_element(By.ID,"Add").click()

                    time.sleep(5)
                    try:
                        a = driver.find_element(By.ID, "txtHintNew").text
                        log.info(a)
                    except:
                        pass
                    try:

                        a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                        for b in a:
                            c=b.text
                            log.info(c)
                    except Exception as e:
                        log.info(e)
                driver.find_element(By.ID,"submit").click()
                time.sleep(5)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                try:
                    a = driver.find_element(By.ID, "txtHint").text
                    log.info(a)
                except:
                    pass
                else:
                    try:
                        driver.find_element(By.XPATH, "//input[@value='Back']").click()
                    except:
                        pass
                try:
                    a = driver.find_element(By.ID, "myText").text
                    log.info(a)
                except:
                    pass
            except Exception as e:
                log.info(e)

        elif name == "limitProfile":

            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Limit Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH,"//form[@id='command']/button").click()
                driver.find_element(By.ID,"name").clear()
                driver.find_element(By.ID,"name").send_keys(balance["Profile Name"][i])

                if balance["ATM cash withdrawal"][i]=="Yes":
                    driver.find_element(By.ID,"4").click()
                if balance["Topup"][i]=="Yes":
                    driver.find_element(By.ID,"33").click()
                if balance["Purchase"][i] == "Yes":
                    driver.find_element(By.ID,"34").click()
                driver.find_element(By.ID,"Submit").click()
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
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
                else:
                    try:
                        driver.find_element(By.XPATH, "//input[@value='Back']").click()
                    except:
                        pass
                try:
                    a = driver.find_element(By.ID, "myText").text
                    log.info(a)
                except:
                    pass


                time.sleep(5)

                try:
                    if balance["Purchase"][i]=='Yes':
                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        try:
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").clear()
                            driver.find_element(By.ID,"totalLifetimeAmount").send_keys(int(balance["Purchase Total Life Time Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"totalLifetimeCount").clear()
                            driver.find_element(By.ID,"totalLifetimeCount").send_keys(int(balance["Purchase Total Lifetime Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomSingleAmount").clear()
                            driver.find_element(By.ID,"onusDomSingleAmount").send_keys(int(balance["Purchase Onus Dom Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomDailyAmount").clear()
                            driver.find_element(By.ID,"onusDomDailyAmount").send_keys(int(balance["Purchase Onus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomDailyCount").clear()
                            driver.find_element(By.ID,"onusDomDailyCount").send_keys(int(balance["Purchase Onus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyAmount").send_keys(int(balance["Purchase Onus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyCount").send_keys(int(balance["Purchase Onus-Dom-Monthly Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"onusDomAnnualAmount").send_keys(int(balance["Purchase Onus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomAnnualCount").clear()
                            driver.find_element(By.ID,"onusDomAnnualCount").send_keys(int(balance["Purchase Onus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomCommissionRate").clear()
                            driver.find_element(By.ID,"onusDomCommissionRate").send_keys(int(balance["Purchase Onus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").send_keys(int(balance["Purchase Onus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomSingleAmount").clear()
                            driver.find_element(By.ID,"offusDomSingleAmount").send_keys(int(balance["Purchase Offus-Dom-Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomDailyAmount").clear()
                            driver.find_element(By.ID,"offusDomDailyAmount").send_keys(int(balance["Purchase Offus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomDailyCount").clear()
                            driver.find_element(By.ID,"offusDomDailyCount").send_keys(int(balance["Purchase Offus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyAmount").send_keys(int(balance["Purchase Offus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyCount").send_keys(int(balance["Purchase Offus-Dom-Mon Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"offusDomAnnualAmount").send_keys(int(balance["Purchase Offus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomAnnualCount").clear()
                            driver.find_element(By.ID,"offusDomAnnualCount").send_keys(int(balance["Purchase Offus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomCommissionRate").clear()
                            driver.find_element(By.ID,"offusDomCommissionRate").send_keys(int(balance["Purchase Offus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").send_keys(int(balance["Purchase Offus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID,"Submit").click()
                            time.sleep(2)
                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)

                        
                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        try:
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").clear()
                            driver.find_element(By.ID, "totalLifetimeAmount").send_keys(
                                int(balance["Purchase Total Life Time Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "totalLifetimeCount").clear()
                            driver.find_element(By.ID, "totalLifetimeCount").send_keys(
                                int(balance["Purchase Total Lifetime Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomSingleAmount").clear()
                            driver.find_element(By.ID, "onusDomSingleAmount").send_keys(
                                int(balance["Purchase Onus Dom Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomDailyAmount").clear()
                            driver.find_element(By.ID, "onusDomDailyAmount").send_keys(
                                int(balance["Purchase Onus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomDailyCount").clear()
                            driver.find_element(By.ID, "onusDomDailyCount").send_keys(
                                int(balance["Purchase Onus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyAmount").send_keys(
                                int(balance["Purchase Onus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyCount").send_keys(
                                int(balance["Purchase Onus-Dom-Monthly Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "onusDomAnnualAmount").send_keys(
                                int(balance["Purchase Onus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomAnnualCount").clear()
                            driver.find_element(By.ID, "onusDomAnnualCount").send_keys(
                                int(balance["Purchase Onus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionRate").clear()
                            driver.find_element(By.ID, "onusDomCommissionRate").send_keys(
                                int(balance["Purchase Onus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").send_keys(
                                int(balance["Purchase Onus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomSingleAmount").clear()
                            driver.find_element(By.ID, "offusDomSingleAmount").send_keys(
                                int(balance["Purchase Offus-Dom-Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomDailyAmount").clear()
                            driver.find_element(By.ID, "offusDomDailyAmount").send_keys(
                                int(balance["Purchase Offus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomDailyCount").clear()
                            driver.find_element(By.ID, "offusDomDailyCount").send_keys(
                                int(balance["Purchase Offus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyAmount").send_keys(
                                int(balance["Purchase Offus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyCount").send_keys(
                                int(balance["Purchase Offus-Dom-Mon Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "offusDomAnnualAmount").send_keys(
                                int(balance["Purchase Offus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomAnnualCount").clear()
                            driver.find_element(By.ID, "offusDomAnnualCount").send_keys(
                                int(balance["Purchase Offus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomCommissionRate").clear()
                            driver.find_element(By.ID, "offusDomCommissionRate").send_keys(
                                int(balance["Purchase Offus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").send_keys(
                                int(balance["Purchase Offus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID, "Submit").click()
                            time.sleep(2)

                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)

                    if balance["Topup"][i]=="Yes":
                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        try:
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").clear()
                            driver.find_element(By.ID,"totalLifetimeAmount").send_keys(int(balance["Topup Total Life Time Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"totalLifetimeCount").clear()
                            driver.find_element(By.ID,"totalLifetimeCount").send_keys(int(balance["Topup Total Lifetime Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomSingleAmount").clear()
                            driver.find_element(By.ID,"onusDomSingleAmount").send_keys(int(balance["Topup Onus Dom Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomDailyAmount").clear()
                            driver.find_element(By.ID,"onusDomDailyAmount").send_keys(int(balance["Topup Onus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomDailyCount").clear()
                            driver.find_element(By.ID,"onusDomDailyCount").send_keys(int(balance["Topup Onus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyAmount").send_keys(int(balance["Topup Onus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyCount").send_keys(int(balance["Topup Onus-Dom-Monthly Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"onusDomAnnualAmount").send_keys(int(balance["Topup Onus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomAnnualCount").clear()
                            driver.find_element(By.ID,"onusDomAnnualCount").send_keys(int(balance["Topup Onus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomCommissionRate").clear()
                            driver.find_element(By.ID,"onusDomCommissionRate").send_keys(int(balance["Topup Onus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").send_keys(int(balance["Topup Onus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomSingleAmount").clear()
                            driver.find_element(By.ID,"offusDomSingleAmount").send_keys(int(balance["Topup Offus-Dom-Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomDailyAmount").clear()
                            driver.find_element(By.ID,"offusDomDailyAmount").send_keys(int(balance["Topup Offus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomDailyCount").clear()
                            driver.find_element(By.ID,"offusDomDailyCount").send_keys(int(balance["Topup Offus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyAmount").send_keys(int(balance["Topup Offus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyCount").send_keys(int(balance["Topup Offus-Dom-Mon Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"offusDomAnnualAmount").send_keys(int(balance["Topup Offus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomAnnualCount").clear()
                            driver.find_element(By.ID,"offusDomAnnualCount").send_keys(int(balance["Topup Offus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomCommissionRate").clear()
                            driver.find_element(By.ID,"offusDomCommissionRate").send_keys(int(balance["Topup Offus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").send_keys(int(balance["Topup Offus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID,"Submit").click()
                            time.sleep(2)
                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)

                        
                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        
                        try:
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").click()
                            driver.find_element(By.ID,"totalLifetimeAmount").clear()
                            driver.find_element(By.ID,"totalLifetimeAmount").send_keys(int(balance["Topup Total Life Time Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"totalLifetimeCount").clear()
                            driver.find_element(By.ID,"totalLifetimeCount").send_keys(int(balance["Topup Total Lifetime Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomSingleAmount").clear()
                            driver.find_element(By.ID,"onusDomSingleAmount").send_keys(int(balance["Topup Onus Dom Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomDailyAmount").clear()
                            driver.find_element(By.ID,"onusDomDailyAmount").send_keys(int(balance["Topup Onus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomDailyCount").clear()
                            driver.find_element(By.ID,"onusDomDailyCount").send_keys(int(balance["Topup Onus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyAmount").send_keys(int(balance["Topup Onus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"onusDomMonthlyCount").send_keys(int(balance["Topup Onus-Dom-Monthly Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"onusDomAnnualAmount").send_keys(int(balance["Topup Onus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomAnnualCount").clear()
                            driver.find_element(By.ID,"onusDomAnnualCount").send_keys(int(balance["Topup Onus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomCommissionRate").clear()
                            driver.find_element(By.ID,"onusDomCommissionRate").send_keys(int(balance["Topup Onus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"onusDomCommissionAmtFixed").send_keys(int(balance["Topup Onus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomSingleAmount").clear()
                            driver.find_element(By.ID,"offusDomSingleAmount").send_keys(int(balance["Topup Offus-Dom-Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomDailyAmount").clear()
                            driver.find_element(By.ID,"offusDomDailyAmount").send_keys(int(balance["Topup Offus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomDailyCount").clear()
                            driver.find_element(By.ID,"offusDomDailyCount").send_keys(int(balance["Topup Offus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyAmount").send_keys(int(balance["Topup Offus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomMonthlyCount").clear()
                            driver.find_element(By.ID,"offusDomMonthlyCount").send_keys(int(balance["Topup Offus-Dom-Mon Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomAnnualAmount").clear()
                            driver.find_element(By.ID,"offusDomAnnualAmount").send_keys(int(balance["Topup Offus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomAnnualCount").clear()
                            driver.find_element(By.ID,"offusDomAnnualCount").send_keys(int(balance["Topup Offus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomCommissionRate").clear()
                            driver.find_element(By.ID,"offusDomCommissionRate").send_keys(int(balance["Topup Offus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID,"offusDomCommissionAmtFixed").send_keys(int(balance["Topup Offus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID,"Submit").click()
                            time.sleep(2)
                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)

                    if balance["ATM cash withdrawal"][i]=="Yes":
                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        try:
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").clear()
                            driver.find_element(By.ID, "totalLifetimeAmount").send_keys(
                                int(balance["ATM Total Life Time Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "totalLifetimeCount").clear()
                            driver.find_element(By.ID, "totalLifetimeCount").send_keys(
                                int(balance["ATM Total Lifetime Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomSingleAmount").clear()
                            driver.find_element(By.ID, "onusDomSingleAmount").send_keys(
                                int(balance["ATM Onus Dom Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomDailyAmount").clear()
                            driver.find_element(By.ID, "onusDomDailyAmount").send_keys(
                                int(balance["ATM Onus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomDailyCount").clear()
                            driver.find_element(By.ID, "onusDomDailyCount").send_keys(
                                int(balance["ATM Onus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyAmount").send_keys(
                                int(balance["ATM Onus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyCount").send_keys(
                                int(balance["ATM Onus-Dom-Monthly Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "onusDomAnnualAmount").send_keys(
                                int(balance["ATM Onus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomAnnualCount").clear()
                            driver.find_element(By.ID, "onusDomAnnualCount").send_keys(
                                int(balance["ATM Onus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomCommissionRate").clear()
                            driver.find_element(By.ID, "onusDomCommissionRate").send_keys(
                                int(balance["ATM Onus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").send_keys(
                                int(balance["ATM Onus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomSingleAmount").clear()
                            driver.find_element(By.ID, "offusDomSingleAmount").send_keys(
                                int(balance["ATM Offus-Dom-Single Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomDailyAmount").clear()
                            driver.find_element(By.ID, "offusDomDailyAmount").send_keys(
                                int(balance["ATM Offus-Dom-Daily Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomDailyCount").clear()
                            driver.find_element(By.ID, "offusDomDailyCount").send_keys(
                                int(balance["ATM Offus-Dom-Daily Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyAmount").send_keys(
                                int(balance["ATM Offus-Dom-Monthly Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyCount").send_keys(
                                int(balance["ATM Offus-Dom-Mon Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "offusDomAnnualAmount").send_keys(
                                int(balance["ATM Offus-Dom-Annual Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomAnnualCount").clear()
                            driver.find_element(By.ID, "offusDomAnnualCount").send_keys(
                                int(balance["ATM Offus-Dom-Annual Count"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomCommissionRate").clear()
                            driver.find_element(By.ID, "offusDomCommissionRate").send_keys(
                                int(balance["ATM Offus-Dom-Comm Rate"][i].split("|")[0]))
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").send_keys(
                                int(balance["ATM Offus-Dom-Comm Amt"][i].split("|")[0]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID, "Submit").click()
                            time.sleep(2)
                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)

                        driver.find_element(By.LINK_TEXT,"Set Limits").click()
                        try:
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").click()
                            driver.find_element(By.ID, "totalLifetimeAmount").clear()
                            driver.find_element(By.ID, "totalLifetimeAmount").send_keys(
                                int(balance["ATM Total Life Time Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "totalLifetimeCount").clear()
                            driver.find_element(By.ID, "totalLifetimeCount").send_keys(
                                int(balance["ATM Total Lifetime Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomSingleAmount").clear()
                            driver.find_element(By.ID, "onusDomSingleAmount").send_keys(
                                int(balance["ATM Onus Dom Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomDailyAmount").clear()
                            driver.find_element(By.ID, "onusDomDailyAmount").send_keys(
                                int(balance["ATM Onus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomDailyCount").clear()
                            driver.find_element(By.ID, "onusDomDailyCount").send_keys(
                                int(balance["ATM Onus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyAmount").send_keys(
                                int(balance["ATM Onus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "onusDomMonthlyCount").send_keys(
                                int(balance["ATM Onus-Dom-Monthly Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "onusDomAnnualAmount").send_keys(
                                int(balance["ATM Onus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomAnnualCount").clear()
                            driver.find_element(By.ID, "onusDomAnnualCount").send_keys(
                                int(balance["ATM Onus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionRate").clear()
                            driver.find_element(By.ID, "onusDomCommissionRate").send_keys(
                                int(balance["ATM Onus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").send_keys(
                                int(balance["ATM Onus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomSingleAmount").clear()
                            driver.find_element(By.ID, "offusDomSingleAmount").send_keys(
                                int(balance["ATM Offus-Dom-Single Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomDailyAmount").clear()
                            driver.find_element(By.ID, "offusDomDailyAmount").send_keys(
                                int(balance["ATM Offus-Dom-Daily Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomDailyCount").clear()
                            driver.find_element(By.ID, "offusDomDailyCount").send_keys(
                                int(balance["ATM Offus-Dom-Daily Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomMonthlyAmount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyAmount").send_keys(
                                int(balance["ATM Offus-Dom-Monthly Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomMonthlyCount").clear()
                            driver.find_element(By.ID, "offusDomMonthlyCount").send_keys(
                                int(balance["ATM Offus-Dom-Mon Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomAnnualAmount").clear()
                            driver.find_element(By.ID, "offusDomAnnualAmount").send_keys(
                                int(balance["ATM Offus-Dom-Annual Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomAnnualCount").clear()
                            driver.find_element(By.ID, "offusDomAnnualCount").send_keys(
                                int(balance["ATM Offus-Dom-Annual Count"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomCommissionRate").clear()
                            driver.find_element(By.ID, "offusDomCommissionRate").send_keys(
                                int(balance["ATM Offus-Dom-Comm Rate"][i].split("|")[1]))
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").clear()
                            driver.find_element(By.ID, "offusDomCommissionAmtFixed").send_keys(
                                int(balance["ATM Offus-Dom-Comm Amt"][i].split("|")[1]))
                            driver.find_element(By.ID, "onusDomCommissionAmtFixed").click()
                            time.sleep(0)
                            driver.find_element(By.ID, "Submit").click()
                            time.sleep(2)
                            try:

                                a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                                for b in a:
                                    c = b.text
                                    log.info(c)
                            except Exception as e:
                                log.info(e)
                        except Exception as e:
                            print(e)
                except:
                    pass
            except Exception as e:
                log.info(e)

        elif name=="topupProfile":
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Topup Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID,"profileName").send_keys(balance["Profile Name"][i])
                driver.find_element(By.ID,"topupProfileDesc").click()
                driver.find_element(By.ID,"topupProfileDesc").click()
                driver.find_element(By.ID,"topupProfileDesc").clear()
                driver.find_element(By.ID,"topupProfileDesc").send_keys(balance["Topup Profile Description"][i])
                Select(driver.find_element(By.ID,"loadType")).select_by_visible_text(balance["Load Type"][i])
                Select(driver.find_element(By.ID,"multiplier")).select_by_visible_text(balance["Multiplier"][i])
                if balance["Multiplier"][i]=="Enable":
                    driver.find_element(By.ID,"multiplierValue").click()
                    driver.find_element(By.ID,"multiplierValue").clear()
                    driver.find_element(By.ID,"multiplierValue").send_keys(balance["Multiplier Value"][i])
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

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
                else:
                    try:
                        driver.find_element(By.XPATH, "//input[@value='Back']").click()
                    except:
                        pass
                try:
                    a = driver.find_element(By.ID, "myText").text
                    log.info(a)
                except:
                    pass
            except Exception as e:
                log.info(e)
        elif name=="cardImageCodeMaster":

            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Card Image Code Master").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID,"imgName").send_keys(balance["Image Name"][i])
                driver.find_element(By.ID,"frontImg").clear()
                driver.find_element(By.ID,"frontImg").send_keys(str(balance["UploadImage"][i]))
                Select(driver.find_element(By.ID,"fontColour")).select_by_visible_text(balance["Font Colour "][i])
                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
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
                else:
                    try:
                        driver.find_element(By.XPATH, "//input[@value='Back']").click()
                    except:
                        pass
                try:
                    a = driver.find_element(By.ID, "myText").text
                    log.info(a)
                except:
                    pass
            except Exception as e:
                log.info(e)



        elif name == "transactionFeeMaster":
            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Transaction and Fee master").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            driver.find_element(By.XPATH, "//form[@id='command']/button").click()
            try:
                time.sleep(2)
                driver.find_element(By.ID,"txnType").send_keys(balance["Transaction Id"][i])
                driver.find_element(By.ID,"txnName").send_keys(balance["Transaction Name"][i])
                Select(driver.find_element(By.ID,"isScheme")).select_by_visible_text(balance["Is Scheme"][i])
                Select(driver.find_element(By.ID,"drCr")).select_by_visible_text(balance["Debit Credit Flag"][i])
                Select(driver.find_element(By.ID,"txnGroup")).select_by_visible_text(balance["Transaction Group"][i])
                if balance["Transaction Group"][i]=="Fee":
                    Select(driver.find_element(By.ID,"isGST")).select_by_visible_text(balance["Is GST Applicable"][i])
                    if balance["Is GST Applicable"][i]=="Yes":
                        driver.find_element(By.ID,"gstAmt").click()
                        driver.find_element(By.ID,"gstAmt").clear()
                        driver.find_element(By.ID,"gstAmt").send_keys(balance["GST Amount in Percentage"][i])
                    Select(driver.find_element(By.ID,"allowQueue")).select_by_visible_text(balance["Allow Queue Mechanism"][i])
                    driver.find_element(By.ID,"subtxnName").click()
                driver.find_element(By.ID,"subtxnName").clear()
                for z in range(0,int(balance["sub transaction times"][i])):

                    driver.find_element(By.ID,"subtxnName").send_keys(balance["Sub Transaction Name"][i].split("|")[z])
                    driver.find_element(By.ID,"txnMode").click()
                    driver.find_element(By.ID,"txnMode").clear()
                    driver.find_element(By.ID,"txnMode").send_keys(str(balance["Transaction Entry Mode"][i]).split("|")[z])
                    if int(balance["sub transaction times"][i])==1:
                        pass
                    else:
                        driver.find_element(By.ID,"Add").click()
                        time.sleep(2)
                        try:

                            a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                            for b in a:
                                c = b.text
                                log.info(c)
                        except Exception as e:
                            log.info(e)
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                driver.find_element(By.ID,"submit").click()

                time.sleep(5)
                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

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


        elif name=="mccMaster":

            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"MCC Master").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID,"mccCode").send_keys(balance["MCC Code"][i])
                driver.find_element(By.ID,"MCCName").send_keys(balance["MCC Name"][i])

                Select(driver.find_element(By.ID,"isSurcharge")).select_by_visible_text(balance["Surcharge Enable"][i])
                if balance["Surcharge Enable"][i]=="Yes":
                    Select(driver.find_element(By.ID,"surchargeType")).select_by_visible_text(balance["Surcharge Type"][i])
                    driver.find_element(By.ID,"surchargeValue").clear()
                    driver.find_element(By.ID,"surchargeValue").send_keys(balance["Surcharge Fee Value"][i])

                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)

                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

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


        elif name=="walletManagement":

            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Wallet Management").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID, "walletName").send_keys(balance["Wallet Name"][i])
                driver.find_element(By.ID, "walletTypeIdentifier").send_keys(balance["Wallet Type Identifier"][i])

                Select(driver.find_element(By.ID,"keyIdentifierId")).select_by_visible_text(balance["Key identifier"][i])
                Select(driver.find_element(By.ID, "mccGroupId")).select_by_visible_text(balance["MCC Group Allowed Type"][i])
                if balance["Offline Enabled"][i]=="Yes":
                    driver.find_element(By.ID,"isTransitEnable").click()

                Select(driver.find_element(By.ID,"isGeneralWallet")).select_by_visible_text(balance["Is General Wallet"][i])
                try:
                    Select(driver.find_element(By.ID,"isWalletBlockingAllowed")).select_by_visible_text(balance["wallet blocking"][i])
                except:
                    pass
                driver.find_element(By.ID,"walletSave").click()

                driver.find_element(By.ID,"submit").click()

                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

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

        elif name=="contactCenter":

            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Contact Center Onboarding").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH, "//form[@id='command']/button").click()
                time.sleep(2)

                driver.find_element(By.ID,"contactCenterName").clear()
                driver.find_element(By.ID,"contactCenterName").send_keys(balance["Contact Center Name"][i])
                driver.find_element(By.ID,"serviceName").click()
                driver.find_element(By.ID,"serviceName").clear()
                driver.find_element(By.ID,"serviceName").send_keys(balance["Service Name"][i])
                driver.find_element(By.ID,"servicePlan").click()
                driver.find_element(By.ID,"servicePlan").clear()
                driver.find_element(By.ID,"servicePlan").send_keys(balance["Plan Type"][i])
                driver.find_element(By.ID,"address1").click()
                driver.find_element(By.ID,"address1").clear()
                driver.find_element(By.ID,"address1").send_keys(balance["Address Line1"][i])
                driver.find_element(By.ID,"address2").click()
                driver.find_element(By.ID,"address2").clear()
                driver.find_element(By.ID,"address2").send_keys(balance["Address Line2"][i])
                driver.find_element(By.ID,"contactPerson").click()
                driver.find_element(By.ID,"contactPerson").clear()
                driver.find_element(By.ID,"contactPerson").send_keys(balance["Contact Person"][i])
                driver.find_element(By.ID,"phoneNumber").click()
                driver.find_element(By.ID,"phoneNumber").clear()
                driver.find_element(By.ID,"phoneNumber").send_keys(balance["Phone Number"][i])
                driver.find_element(By.ID,"contactCenterSave").click()
                driver.find_element(By.ID,"mobileNumber").clear()
                driver.find_element(By.ID,"mobileNumber").send_keys(balance["Mobile Number"][i])
                driver.find_element(By.ID,"emailId").click()
                driver.find_element(By.ID,"emailId").clear()
                driver.find_element(By.ID,"emailId").send_keys(balance["Email Id"][i])
                driver.find_element(By.ID,"contactCenterNumber").click()
                driver.find_element(By.ID,"contactCenterNumber").clear()
                driver.find_element(By.ID,"contactCenterNumber").send_keys(balance["Contact Center Number"][i])
                driver.find_element(By.ID,"submit").click()

                try:

                    a=driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c=b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

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

        elif name=="productConfiguration":


            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Product Configuration").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            driver.find_element(By.XPATH, "//form[@id='command']/button").click()
            time.sleep(2)
            try:
                Select(driver.find_element(By.ID,"institutionId")).select_by_visible_text(balance["Institution Name"][i])
                Select(driver.find_element(By.ID,"partnerId")).select_by_visible_text(balance["Partner Name"][i])
                Select(driver.find_element(By.ID,"issuerId")).select_by_visible_text(balance["Issuer Name"][i])
                driver.find_element(By.ID,"productName").click()
                driver.find_element(By.ID,"productName").clear()
                driver.find_element(By.ID,"productName").send_keys(balance["Product Name"][i])
                driver.find_element(By.ID,"cardProductName").click()
                driver.find_element(By.ID,"cardProductName").clear()
                driver.find_element(By.ID,"cardProductName").send_keys(balance["Card Product Display Name"][i])
                driver.find_element(By.ID,"productDesc").click()
                driver.find_element(By.ID,"productDesc").clear()
                driver.find_element(By.ID,"productDesc").send_keys(balance["Product Description"][i])
                Select(driver.find_element(By.ID,"mccRestrictGroupId")).select_by_visible_text(balance["MCC Restrict Group"][i])
                Select(driver.find_element(By.ID,"contactCenterId")).select_by_visible_text(balance["Contact Center"][i])

                driver.find_element(By.ID,"institutionBank").send_keys(int(balance["Institution-Bank"][i]))
                driver.find_element(By.ID,"payCraft").clear()
                driver.find_element(By.ID,"payCraft").send_keys(balance["Paycraft"][i])
                driver.find_element(By.ID,"issuerClient").clear()
                driver.find_element(By.ID,"issuerClient").send_keys(balance["Issuer-Client"][i])
                driver.find_element(By.ID,"anyOther").clear()
                driver.find_element(By.ID,"anyOther").send_keys(balance["Any other"][i])
                driver.find_element(By.ID,"institutionBank").send_keys(int(balance["Institution-Bank"][i]))
                driver.find_element(By.ID,"productManagement").click()
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)



                Select(driver.find_element(By.ID,"balanceProfileOption")).select_by_visible_text(balance["Balance Management Profile"][i])
                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)



                Select(driver.find_element(By.ID,"BinProfileId")).select_by_visible_text(balance["Bin Profile Name"][i])
                Select(driver.find_element(By.ID,"crnType")).select_by_visible_text(balance["CRN Type"][i])
                driver.find_element(By.ID,"submit").click()

                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                Select(driver.find_element(By.ID,"topupProfileId")).select_by_visible_text(balance["Topup Profile Name"][i])
                driver.find_element(By.ID,"submit").click()

                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                Select(driver.find_element(By.ID,"name")).select_by_visible_text(balance["Fee Profile Name"][i])

                driver.find_element(By.ID,"submit").click()

                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                Select(driver.find_element(By.ID,"txnProfileName")).select_by_visible_text(balance["Txn Profile Name"][i])
                driver.find_element(By.ID,"submit").click()

                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                Select(driver.find_element(By.ID,"profileName")).select_by_visible_text(balance["Limit Profile Name"][i])
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                Select(driver.find_element(By.ID,"mccGroupId")).select_by_visible_text(balance["Allowed MCC Group Name"][i])
                driver.find_element(By.ID,"submit").click()

                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)

                try:
                    Select(driver.find_element(By.ID,"isMultiWallet")).select_by_visible_text(balance["Multi-Wallet Enabled"][i])
                    self.accept_next_alert = True
                    Select(driver.find_element(By.ID,"walletProfileId")).select_by_visible_text(balance["Wallet Profile Group"][i])
                except:
                    pass
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)

                # self.assertRegexpMatches(self.close_alert_and_get_its_text(),
                #                          r"^Are you sure you want to proceed further for creating product[\s\S]$")

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
                log.info(f" Product setup failed for product name {balance['Product Name'][i]}.Recheck data /n{e}  ")
                print(e)

        elif name=="transactionProfile":
            time.sleep(3)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT,"Transaction Profile").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            driver.find_element(By.XPATH, "//form[@id='command']/button").click()
            time.sleep(2)
            try:
                driver.find_element(By.ID,"name").click()
                driver.find_element(By.ID,"name").clear()
                driver.find_element(By.ID,"name").send_keys(balance['Txn Profile Name'][i])
                driver.find_element(By.ID,"txnProfileDesc").click()
                driver.find_element(By.ID,"txnProfileDesc").clear()
                driver.find_element(By.ID,"txnProfileDesc").send_keys(balance['Txn Profile Desc'][i])
                for j in range(0,int(balance['subtimes'][i])):

                    driver.find_element(By.ID,"txnType").click()
                    Select(driver.find_element(By.ID,"txnType")).select_by_visible_text(balance['Transaction Type'][i].split("|")[j])
                    if balance['Enable Txn Type'][i].split("|")[j]=="Yes":
                        driver.find_element(By.ID,"enableDisable1").click()
                    elif balance['Enable Txn Type'][i].split("|")[j] == "No":
                        driver.find_element(By.ID, "enableDisable2").click()
                    driver.find_element(By.ID,"Add").click()
                    time.sleep(2)
                    try:

                        a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                        for b in a:
                            c = b.text
                            log.info(c)
                    except Exception as e:
                        log.info(e)
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
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


        if name=="MCCGroups":
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "MCC Groups").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH,"//form[@id='command']/button").click()
                time.sleep(2)
                driver.find_element(By.ID,"mccGroupName").click()
                driver.find_element(By.ID,"mccGroupName").clear()
                driver.find_element(By.ID,"mccGroupName").send_keys(balance['mccGroupName'][i])
                driver.find_element(By.ID,"restrictType").click()
                Select(driver.find_element(By.ID,"restrictType")).select_by_visible_text(balance['restrictType'][i])
                tmp=balance['mcc'][i].split("|")
                for n in range(0,len(tmp)):
                    Select(driver.find_element(By.ID,"leftList")).select_by_visible_text(tmp[n])
                    time.sleep(1)
                    driver.find_element(By.XPATH,"//input[@value='>']").click()
                time.sleep(2)
                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)
                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                time.sleep(2)
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
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

        if name == "WalletProfileGroup":
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame("showframeLeft")
            driver.find_element(By.LINK_TEXT, "Wallet Profile Group").click()
            driver.switch_to.default_content()
            driver.switch_to.frame("showframe")
            time.sleep(3)
            try:
                driver.find_element(By.XPATH,"//form[@id='command']/button").click()
                driver.find_element(By.ID,"walletProfileName").send_keys(balance['walletProfileName'][i])
                tmp = balance['wallet'][i].split("|")
                for n in range(0, len(tmp)):
                    Select(driver.find_element(By.ID,"leftList")).select_by_visible_text(tmp[n])
                    time.sleep(1)
                    driver.find_element(By.XPATH,"//input[@value='>']").click()
                time.sleep(2)
                driver.find_element(By.ID,"Submit").click()
                time.sleep(2)


                try:

                    a = driver.find_elements(By.XPATH, "//font[@color='red']/b/div")
                    for b in a:
                        c = b.text
                        log.info(c)
                except Exception as e:
                    log.info(e)
                time.sleep(2)
                driver.find_element(By.ID,"submit").click()
                time.sleep(2)
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












