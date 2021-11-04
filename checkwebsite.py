from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def findserverstatus():

    s = Service("C:/Selenium/chromedriver.exe")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=s, chrome_options=options)
    driver.get("https://www.newworld.com/en-us/support/server-status")
    myPageTitle=driver.title

    ap_southeast = driver.find_element(By.XPATH, "/html/body/main/section/div/div[3]/a[4]/div")
    ap_southeast.click()

    erythia = driver.find_element(By.XPATH, "/html/body/main/section/div/div[5]/div[4]/div[29]/div[1]/div").get_attribute("title")

    print(erythia)

    return erythia

    assert "New World" in myPageTitle

