from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.instagram.com/')

def login():
    with open(file='./dete.txt') as f:
        text = f.readlines()[16:18]
        mail = text[0].strip('\n')
        passwrd = text[1].strip('\n')

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(mail)
    driver.find_element(By.NAME, value='password').send_keys(passwrd)
    driver.find_elements(By.TAG_NAME, value='button')[1].click()

    time.sleep(3)
    box = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, '_ac8f')))
    box.find_element(By.TAG_NAME, 'div').click()


def find_followers():
    footer = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, '_a9-z')))
    footer.find_elements(By.TAG_NAME, value='button')[1].click()
    bar = driver.find_element(By.CSS_SELECTOR, value='.segoe')
    name = bar.find_elements(By.TAG_NAME, value='div')[1].get_attribute('id')

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="{name}"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div'))).click()
    
    search = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="{name}"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')))
    search.send_keys('Harry Mack')

    time.sleep(10)
    search.send_keys(Keys.DOWN, Keys.ENTER)

    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="{name}"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'))).click()

    time.sleep(10)
    shield = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
    
    for _ in range(2):
        time.sleep(3)
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", shield)


def follow():  
    test = driver.find_elements(By.TAG_NAME, 'button')
    for i in test:
        if i.text == 'Follow':
            time.sleep(3)
            i.click()

    driver.quit()

login()
find_followers()
follow()