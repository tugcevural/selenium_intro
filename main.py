from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\tugce\\Desktop\\selenium_intro\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.trendyol.com/gap/erkek-bebek-ekose-poplin-gomlek-p-46438659?boutiqueId=594587&merchantId=107130")

price = driver.find_element(By.CLASS_NAME, 'prc-dsc')
print(price.text)

box=driver.find_element(By.CLASS_NAME, "search-box")
print(box.get_attribute("placeholder"))

#----------------------------------------------------

driver2 = webdriver.Chrome(executable_path=chrome_driver_path)
driver2.get("https://python.org")