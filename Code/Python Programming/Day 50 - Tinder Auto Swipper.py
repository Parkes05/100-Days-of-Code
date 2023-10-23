from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, ElementClickInterceptedException
import time


with open(file='./dete.txt') as f:
    text = f.readlines()[15:17]
    mail = text[1].strip('\n')
    passwrd = text[0].strip('\n')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get(url='https://tinder.com/')

time.sleep(10)
login_in = driver.find_elements(By.TAG_NAME, value='a')[16]
login_in.click()

time.sleep(10)
driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()

time.sleep(10)

###### switching windows ######
all_windows = driver.window_handles
base_window = driver.window_handles[0]
new_window = driver.window_handles[1]
driver.switch_to.window(base_window)
print(driver.title)
driver.switch_to.window(new_window)
print(driver.title)
###### switching windows ######

email = driver.find_element(By.ID, value='email')
email.send_keys(mail)
password = driver.find_element(By.ID, value='pass')
password.send_keys(passwrd)
driver.find_element(By.NAME, value='login').click()

time.sleep(10)
try:
    driver.find_element(By.XPATH, value='//*[@id="mount_0_0_q5"]/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/div/div').click()
except NoSuchElementException:
    print('No Continue button to click')
except NoSuchWindowException:
    print('No Window to navigate')

time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div[1]/div/div/div[3]/button[1]').click()

time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div/div/div/div[3]/button[2]').click()

time.sleep(3)
driver.find_element(By.XPATH, value='//*[@id="s1477815459"]/div/div[2]/div/div/div[1]/div[2]/button').click()

for _ in range(20):
    time.sleep(3)
    buttons = driver.find_elements(By.TAG_NAME, value='button')
    for i in buttons:
        if i.text == 'LIKE':
            try:
                i.click()
            except ElementClickInterceptedException:
                try:
                    back = driver.find_elements(By.TAG_NAME, value='button')
                    for j in back:
                        if j.text == 'Back to Tinder':
                            j.click()
                except NoSuchElementException:
                    pass

    
driver.quit()