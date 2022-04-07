
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\\Users\\tugce\\Desktop\\selenium_intro\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie=driver.find_element(By.ID, 'cookie')


pane_items=driver.find_elements(By.CSS_SELECTOR, '#store div')
print(pane_items)
item_ids=[]
for item in pane_items:
    item_ids.append(item.get_attribute("id"))
#print(item_ids)

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie.click()

    if time.time() > timeout:
        print("entered")
        my_dict = {}
        portal= driver.find_element(By.CSS_SELECTOR, '#buyPortal b').text
        portal_cost=portal.split()[2].strip().replace(",", "")
        portal_cost_int=int(portal_cost)

        #portalDiv = driver.find_element(By.CSS_SELECTOR, '#buyPortal')

        #my_dict[portalDiv]
        #print("portal_cost_int", portal_cost_int)

        alchemy=driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text
        alchemy_cost = alchemy.split("-")[1].strip().replace(",", "")
        alchemy_cost_int = int(alchemy_cost)
        #print("alchemy_cost_int", alchemy_cost_int)

        shipment=driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text
        shipment_text_cost = shipment.split("-")[1].strip().replace(",", "")
        shipment_text_cost_int = int(shipment_text_cost)
        #print("shipment_text_cost_int", shipment_text_cost_int)

        mine_text=driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text
        mine_text_cost = mine_text.split("-")[1].strip().replace(",", "")
        mine_text_cost_int = int(mine_text_cost)
        #print("mine_text_cost_int", mine_text_cost_int)

        factory=driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text
        factory_text_cost = factory.split("-")[1].strip().replace(",", "")
        factory_text_cost_int = int(factory_text_cost)
        #print("factory_text_cost_int", factory_text_cost_int)


        grandma=driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text
        grandma_text_cost = grandma.split("-")[1].strip().replace(",", "")
        grandma_text_cost_int = int(grandma_text_cost)
        #print("grandma_text_cost_int", grandma_text_cost_int)

        cursor=driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text
        cursor_text_cost = cursor.split("-")[1].strip().replace(",", "")
        cursor_text_cost_int = int(cursor_text_cost)
        #print("cursor_text_cost_int", cursor_text_cost_int)

        list_of_item_prices=[portal_cost_int, alchemy_cost_int, shipment_text_cost_int, mine_text_cost_int, factory_text_cost_int, grandma_text_cost_int, cursor_text_cost_int]
        #print(list_of_item_prices)

        list_of_item_prices.reverse()

        cookie_upgrades={}
        for i in range(len(list_of_item_prices)):
            cookie_upgrades[list_of_item_prices[i]]=item_ids[i]
        print(cookie_upgrades)

        current_money=driver.find_element(By.XPATH, '//*[@id="money"]').text
        if "," in current_money:
            current_money=current_money.replace(",","")
        current_cookies=int(current_money)


        affordable_upgrades = {}
        for j in range(len(list_of_item_prices)):
            for cost, id in cookie_upgrades.items():
                if current_cookies > cost:
                    affordable_upgrades[cost] = id

        highest_price_element=max(affordable_upgrades.keys())

        highest_element_id=affordable_upgrades[highest_price_element]
        highest_element_id_str=str(highest_element_id)
        driver.find_element(By.ID, highest_element_id_str).click()


        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_second= driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break



