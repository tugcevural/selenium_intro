from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\tugce\\Desktop\\selenium_intro\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.trendyol.com/gap/erkek-bebek-ekose-poplin-gomlek-p-46438659?boutiqueId=594587&merchantId=107130")

price = driver.find_element(By.CLASS_NAME, 'prc-dsc')
print(price.text)
box=driver.find_element(By.CLASS_NAME, "search-box")

#print(box.get_attribute("placeholder"))

#----------------------------------------------------

driver2 = webdriver.Chrome(executable_path=chrome_driver_path)
driver2.get("https://python.org")
python_logo=driver2.find_element(By.CLASS_NAME, "python-logo")
#print(python_logo.size)

#driver2.find_element(By.CSS_SELECTOR)

bug_link=driver2.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


stg=driver2.find_element(By.XPATH, '//*[@id="success-stories"]/a')
print(stg.text)


xxx=driver2.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[1]/h2')
print(xxx.text)



event_times=driver2.find_elements(By.CSS_SELECTOR, ".event-widget time" )
print(event_times)
for time in event_times:
    print(time.text)

event_names=driver2.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in event_names:
    print(name.text)

events={}
for n in range(len(event_times)):
    events[n]={
        "time":event_times[n].text,
        "name":event_names[n].text}

print(events)
