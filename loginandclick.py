from typing import KeysView

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable_infobars")
    options.add_argument("start-maximised")
    options.add_argument("disable-dev-shm-user")
    options.add_argument("no-sandbox")
    options.add_experimental_option ( "excludeSwitches",
                                    ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    #https://automated.pythonanywhere.com
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def main():
    driver=get_driver()
    time.sleep(2)
    driver.find_element(By.ID,value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, value="id_password").send_keys("automated"+KEYS.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, value="html/body/nav/div/a").click()
    time.sleep(2)
    dynamic_element = driver.find_element(By.ID,value="displaytimer")
    return clean_text(dyanmic_element.text)

print(main())