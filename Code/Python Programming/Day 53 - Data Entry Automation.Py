import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
response = requests.get(url='https://shorturl.at/dvzEI', headers=my_header)

response.raise_for_status()
web_text = response.text

soup = BeautifulSoup(web_text, 'html.parser')
# print(soup.prettify())

time.sleep(10)
ul_list = soup.find(name='ul', class_='photo-cards')
housing_list = ul_list.find_all(name='li')
address_list = [item.getText() for item in housing_list if len(item.getText()) > 19]
link_list = ul_list.find_all('a', href=True)

addresses = []
costing = []
links = []

for i in address_list:
    try:
        addresses.append(i.split('|')[1].split('$')[0])
        costing.append(f"${i.split('|')[1].split('$')[1].split('+')[0].split('/mo1')[0]}")
    except IndexError:
        addresses.append(i.split('$')[0])
        costing.append(f"${i.split('$')[1].split('+')[0].split('/mo1')[0]}")

start = 'https://www.zillow.com'
for i in link_list:
    if start in i.get('href'):
        links.append(i.get('href'))
    else:
        links.append(f'{start}{i.get("href")}')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

driver.get(url='https://forms.gle/aZeqZCen9NQ8bbD26')

for i in range(len(addresses)):
    time.sleep(2)
    inputs = driver.find_elements(By.TAG_NAME, 'input')[3:6]
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(costing[i])
    inputs[2].send_keys(links[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    
    time.sleep(2)
    driver.find_element(By.TAG_NAME, 'a').click()


driver.quit()