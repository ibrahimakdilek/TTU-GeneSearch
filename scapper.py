from configs import Config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

class Search():

    def __init__(self):
        self.config = Config()
        self.driver = self.config.ChromeSetUp()
        

    def GetLinkTree(self, igLink):
        data = []
        self.driver.get(igLink)

        try:
            WebDriverWait(self.driver, 5).until(Ec.presence_of_element_located((By.NAME, "username"))).send_keys("ftudios.digital")
            self.driver.find_element(By.NAME, "password").send_keys("21dreamstudio")
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').submit()
            time.sleep(5)
            self.driver.get(igLink)
            for item in self.driver.find_elements(By.TAG_NAME, "a"):
                if "linktr.ee" in item.get_attribute("innerHTML"):
                    self.driver.get(item.get_attribute("href"))
                    for items in self.driver.find_elements(By.CLASS_NAME, "sc-pFZIQ.StyledButton-sc-686c3k-0.ldGKnQ.dLjCyh"):
                        link = items.get_attribute("href")
                        text = items.find_element(By.CLASS_NAME, "sc-hKgILt.Button__StyledText-sc-uh5tyw-0.kVCYxL.rsIfq").get_attribute("innerHTML")
                        data.append(f"{text} : {link}")
                    break

        except TimeoutException:
            try:
                self.driver.get(igLink)
                for item in self.driver.find_elements(By.TAG_NAME, "a"):
                    if "linktr.ee" in item.get_attribute("innerHTML"):
                        self.driver.get(item.get_attribute("href"))
                        for items in self.driver.find_elements(By.CLASS_NAME, "sc-pFZIQ.StyledButton-sc-686c3k-0.ldGKnQ.dLjCyh"):
                            link = items.get_attribute("href")
                            text = items.find_element(By.CLASS_NAME, "sc-hKgILt.Button__StyledText-sc-uh5tyw-0.kVCYxL.rsIfq").get_attribute("innerHTML")
                            data.append(f"{text} : {link}")
                        break

            except NoSuchElementException:
                print("error occured")
                pass
        
        return data

    def GetDataLinks(self, searchName):
       
        data = []
        try:
            self.driver.get("https://www.google.com")
            self.driver.maximize_window()
            time.sleep(5)
            WebDriverWait(self.driver, 30).until(Ec.presence_of_all_elements_located((By.TAG_NAME, "input")))[0].send_keys(searchName)
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(Ec.presence_of_all_elements_located((By.TAG_NAME, "input")))[3].click()
            time.sleep(2)
    
            i = 1
            while i < 3:
                nextPages = self.GetData(driver=self.driver)
                nextBtn = WebDriverWait(self.driver, 5).until(Ec.presence_of_element_located((By.ID, "pnnext"))).click()
                time.sleep(2)
                i += 1
                data.append(nextPages)
                
        except:
            print("error occured")
            pass

        return data

    def GetData(self, driver):
        holder = []
        dataHolder = WebDriverWait(driver, 6).until(Ec.presence_of_all_elements_located((By.CLASS_NAME, "g.tF2Cxc")))
        for data in dataHolder:
            links = data.find_element(By.CLASS_NAME, "yuRUbf").find_element(By.TAG_NAME, "a").get_attribute("href")
            names = data.find_element(By.CLASS_NAME, "VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf").find_element(By.TAG_NAME, "span").get_attribute("innerHTML").split(" ")
            for name in names:
                if "@" in name:

                    if name.startswith("@"):
                        pass
                    else:
                        email = name.split("@")[0] + "@gmail.com"
                        pair = (f"{links} : {email}")
                        holder.append(pair)
        return holder
        
if __name__ == "__main__":
    serch = Search()
    #serch.GetDataLinks('model los angeles "linktr.ee/" @gmail.com site:instagram.com')
    serch.GetLinkTree("https://www.instagram.com/thesydneymartin/")