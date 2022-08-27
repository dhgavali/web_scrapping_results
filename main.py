from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.alert import Alert
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=options,executable_path='J:\stuff\soft\chromedriver.exe')

web.get('https://msbte.org.in/DISRESLIVE2021CRSLDSEP/frmALYSUM21PBDisplay.aspx')

# variable to store the result
dict = {}

web.implicitly_wait(30)
resultCount = 0
sem = "FINAL SEMESTER"
course1 = "Diploma In Information Technology"
course2 = "Diploma In Computer Engineering"

rlstart = 156
rlend = 157500

try:
    pdl  = web.current_window_handle
    for x in range(rlstart, rlend):
        
        web.find_element_by_xpath('//*[@id="txtEnrollSeatNo"]').clear()
        inp = web.find_element_by_xpath('//*[@id="txtEnrollSeatNo"]')
        print(x)
        # inp = web.find_element_by_xpat h('//*[@id="txtEnrollSeatNo"]')  
        inp.send_keys(x)
        try: 
            web.find_element_by_xpath('//*[@id="btnSubmit"]').click()
            handles =  web.window_handles
            
            for handle in handles:
                if(handle != pdl):
                    
                    web.switch_to.window(handle)

                    getyear = web.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[2]/td[7]/strong').text
                    # getyear = web.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[2]/td[7]/strong').text
                    getdept = web.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[3]/td[2]').text
                    getname = web.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[1]/td[2]/strong').text

                    # if(getyear == sem && (getdept == course1 or getdept == course2)):
                 
                    if(getyear == sem):

                        
                        getresult = web.find_element_by_css_selector('body > div > div:nth-child(3) > div:nth-child(4) > table > tbody > tr:nth-child(5) > td:nth-child(3) > strong').text
                        enrollment = web.find_element_by_xpath('/html/body/div/div[2]/table/tbody/tr[2]/td[2]').text    
                        if(float(getresult) > 96.00):
                        
                            resultCount += 1
                            dict[enrollment] = {"name" : getname, "per" : getresult, "dept": getdept}
                            web.close()
                            web.switch_to.window(pdl)
                        else:
                            web.close()
                            web.switch_to.window(pdl)
                    else:
                        web.close()
                        web.switch_to.window(pdl)

        except UnexpectedAlertPresentException: 
            web.switch_to_alert().accept()
            x = x + 1
            inp.send_keys(x)
            submit.click()

finally:
   
    web.quit()
    print(dict)