from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\\Users\\tugce\\Desktop\\selenium_intro\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_count=driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(article_count.text)
#article_count.click()
all_portals=driver.find_element(By.LINK_TEXT, "All portals")
#all_portals.click()

search=driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

#------------------------------


