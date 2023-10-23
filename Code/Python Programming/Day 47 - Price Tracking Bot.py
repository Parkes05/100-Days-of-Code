import requests, lxml
import smtplib
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# https://myhttpheader.com/
response = requests.get(url='https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6',
                        headers=header)
response.raise_for_status()
web_data = response.text
# print(web_data)

soup = BeautifulSoup(web_data, 'lxml')
# print(soup)

price = soup.find_all(class_='a-price-whole')[1].text.strip('.')
# print(price)

if int(price) < 100:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user='', password='')
        connection.sendmail(from_addr='', to_addrs='', msg='')