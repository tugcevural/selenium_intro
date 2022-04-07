from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\\Users\\tugce\\Desktop\\selenium_intro\\chromedriver.exe"
driver2 = webdriver.Chrome(executable_path=chrome_driver_path)
driver2.get("http://secure-retreat-92358.herokuapp.com/")


fname=driver2.find_element(By.NAME, "fName")
fname.send_keys("tugce")

lname=driver2.find_element(By.NAME, "lName")
lname.send_keys("vr")

email=driver2.find_element(By.NAME, "email")
email.send_keys("11asd_f_gh_?@gmail.com")

button=driver2.find_element(By.XPATH, '/html/body/form/button')
button.click()

