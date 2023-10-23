from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def next():
    time.sleep(3)
    next_text = driver.find_element(By.CSS_SELECTOR, value='.pv4')
    next_text.find_element(By.TAG_NAME, value='button').click()
    

with open(file='./dete.txt') as f:
    text = f.readlines()[14:16]
    mail = text[0].strip('\n')
    passwrd = text[1].strip('\n')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get(url='https://www.linkedin.com/jobs/search/?currentJobId=3720000533&f_AL=true&f_E=2&geoId=101165590&keywords=graduate%20python%20developer&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true')

time.sleep(5)
sign_in_button = driver.find_elements(By.TAG_NAME, value='a')
for i in sign_in_button:
    if i.text == 'Sign in':
        i_class = i.get_attribute('class').split(' ')[-1]
        driver.find_element(By.CLASS_NAME, value=i_class).click()
        break

time.sleep(5)
email = driver.find_element(By.NAME, value='session_key')
email.send_keys(mail)
password = driver.find_element(By.NAME, value='session_password')
password.send_keys(passwrd)
driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(5)
job_list = driver.find_element(By.CLASS_NAME, value='scaffold-layout__list-container')
list_container = job_list.find_elements(By.TAG_NAME, value='li')

for posting in list_container:
    posting.click()
    time.sleep(3)
    click = driver.find_element(By.CLASS_NAME, value='jobs-apply-button--top-card')
    apply_text = click.find_element(By.CLASS_NAME, value='artdeco-button__text').text
    print(apply_text)
    if apply_text != 'Easy Apply':
        continue
    else:
        button = click.find_element(By.TAG_NAME, value='button')
        button.click()
        next()
        break


driver.quit()
