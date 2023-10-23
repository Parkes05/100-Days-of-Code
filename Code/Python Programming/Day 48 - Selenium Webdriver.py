from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get(url='https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')

price = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
price_cent = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text

print(f'{price}, {price_cent}')

driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)

my_dict = {}
driver.get(url='https://www.python.org/')
for num in range(1, 6):
    date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/time')
    event = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/a')
    my_dict[num-1] = {
            'time': date.text,
            'name': event.text,
    }

print(my_dict)


driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

wiki = driver.find_element(By.ID, value='articlecount')
num = wiki.text.split()[0]
print(num)

link = driver.find_element(By.LINK_TEXT, value=num)
# link.click()

send = driver.find_element(By.NAME, value='search')
send.send_keys('Python')
send.send_keys(Keys.ENTER)


driver1 = webdriver.Chrome()
driver1.get(url='https://manganato.com/bookmark')
driver1.find_element(By.CLASS_NAME, value='user-register').click()

password = driver1.find_element(By.NAME, value='password')
password.send_keys('pass')



##### Project ######
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get(url='https://orteil.dashnet.org/cookieclicker/')

time.sleep(7)
driver.find_element(By.ID, value='langSelect-EN').click()

time.sleep(7)
cookie = driver.find_element(By.ID, value='bigCookie')
stop_bot = time.time() + (60 * 1)
buy_upgrades = time.time() + 5

while time.time() < stop_bot:
    cookie.click()
    if time.time() >= buy_upgrades:
        # prices = driver.find_elements(By.CLASS_NAME, value='price')
        # prices_text = [item.text for item in prices]
        # # print(prices_text)
        # int_prices = [''.join(item.split(',')) for item in prices_text if item != '']
        # # print(int_prices)

        available_products = driver.find_elements(By.CSS_SELECTOR, value='.enabled')
        available_products_text = [item.text for item in available_products]
        # print(available_products_text)
        cleaned_products_text = [item for item in available_products_text if item != '']
        further_cleaned_products_text = [item for item in cleaned_products_text if item != 'Mute']
        # print(further_cleaned_products_text)

        my_dict = {further_cleaned_products_text.index(item): item.split('\n')[1] 
                for item in further_cleaned_products_text}
        # print(my_dict)

        cookie_amount = driver.find_element(By.ID, value='cookies').text.split(' ')[0]
        int_cookie = int(''.join(cookie_amount.split(',')))
        # print(int_cookie)

        check = True
        for num in range(len(my_dict), 0, -1):
            if int_cookie >= int(my_dict[num-1]) and check:
                driver.find_element(By.ID, f'product{num-1}').click()
                check = False

        buy_upgrades = time.time() + 5

result = driver.find_element(By.ID, value='cookies').text.split(' ')[-1]
print(f'cookies/second: {result}')