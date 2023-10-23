from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with open(file='./dete.txt') as f:
    text = f.readlines()[14:16]
    mail = ''
    passwrd = text[1].strip('\n')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

def get_internet_speed():
    driver = webdriver.Chrome(chrome_options)
    driver.get('https://www.speedtest.net/')
    driver.find_element(By.CLASS_NAME, value='start-button').click()
    time.sleep(60)
    down = driver.find_element(By.CSS_SELECTOR, '.download-speed').text
    up = driver.find_element(By.CSS_SELECTOR, '.upload-speed').text
    print(f'down: {down}\nup: {up}')

    driver.quit()
    return (down, up)
    
def send_tweet():
    driver = webdriver.Chrome(chrome_options)   
    driver.get(url='https://twitter.com/')
    time.sleep(7)
    driver.find_elements(By.CSS_SELECTOR, value='.r-1ipicw7')[-1].click()

    time.sleep(7)
    email = driver.find_element(By.NAME, value='text')
    email.send_keys(mail)
    driver.find_elements(By.CSS_SELECTOR, value='.r-13qz1uu')[10].click()

    time.sleep(7)
    phone = driver.find_element(By.TAG_NAME, value='input')
    phone.send_keys('')
    driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()

    time.sleep(7)
    password = driver.find_element(By.NAME, value='password')
    password.send_keys(passwrd)
    driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()

    time.sleep(7)
    tweet = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
    tweet.send_keys(f'My current download speed is {down} and up load speed is {up} @Spectranet_NG')
    driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div').click()

speed = get_internet_speed()
up = speed[1]
down = speed[0]
send_tweet()