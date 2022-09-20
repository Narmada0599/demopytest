from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

ser_obj = Service("C:\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://iq-qa.efi.com/iq/#/")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#home-lnk-siin").click()
user_id = driver.find_element(By.CSS_SELECTOR,"#siin-inp-email")
user_id.clear()
sleep(3)
user_id.send_keys("narmada.d@efi.com")
sleep(3)
pass_word = driver.find_element((By.XPATH, '//*[@id="siin-inp-pass"]'))
pass_word.clear()
sleep(3)
pass_word.send_keys("Efihelium@123")
sleep(3)
driver.find_element(By.XPATH, '//button[@id ="siin-lnk-login"]').click()
sleep(3)
act_title = driver.title
print(act_title)
driver.quit()


