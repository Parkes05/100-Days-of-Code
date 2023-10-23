import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# df = pd.read_csv('salaries_by_college_major.csv')
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isna())

# clean_df = df.dropna()
# print(clean_df.tail())
# print(clean_df['Starting Median Salary'])
# print(clean_df['Starting Median Salary'].max())
# print(clean_df['Starting Median Salary'].idxmax())
# print(clean_df['Undergraduate Major'].loc[43])
# print(clean_df.loc[43])

# print(clean_df.columns)
# x = clean_df['Mid-Career Median Salary'].idxmax()
# print(f'Major with the highest mid career salary: {clean_df['Undergraduate Major'].loc[x]}\nWith a salary of: {clean_df['Mid-Career Median Salary'].loc[x]}\n')

# y = clean_df['Starting Median Salary'].idxmin()
# print(f'Major with the lowest starting salary: {clean_df['Undergraduate Major'].loc[y]}\nWith a salary of: {clean_df['Starting Median Salary'].loc[y]}\n')

# z = clean_df['Mid-Career Median Salary'].idxmin()
# print(f'Major with the lowest mid career salary: {clean_df['Undergraduate Major'].loc[z]}\nWith a salary of: {clean_df['Mid-Career Median Salary'].loc[z]}\n')

# diff = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
# clean_df.insert(1, 'Spread', diff)
# print(clean_df.head())

# low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major', 'Spread']])

# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

# highest_risk = clean_df.sort_values('Spread', ascending=False)
# print(highest_risk[['Undergraduate Major', 'Spread']].head())

# print(clean_df['Group'])
# print(clean_df.groupby('Group').count())
# print(clean_df.groupby('Group').mean())

# pd.options.display.float_format = '{:,.2f}'.format 
# print(clean_df.groupby('Group').mean())



def get_table_data(url):
    response = requests.get(url)
    response.raise_for_status()
    web_data = response.text

    soup = BeautifulSoup(web_data, 'html.parser')
    # print(soup.prettify())

    table = soup.find(name='table')
    table_rows = table.select('.data-table__row')
    table_values = [item.select('.data-table__value') for item in table_rows]

    table_list = []
    for i in table_values:
        data = {
            'Rank': i[0].getText(),
            'Major': i[1].getText(),
            'Degree Type': i[2].getText(),
            'Early Career Pay': i[3].getText(), 
            'Mid-Career Pay': i[4].getText(),
            '% High Meaning': i[5].getText(),
        }
        table_list.append(data)
        new_df = pd.DataFrame(table_list)
    return new_df


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')

url = driver.current_url
table_1 = get_table_data(url)
# pd.options.display.max_columns = 4
print(table_1)

driver.find_element(By.XPATH, value='//*[@id="__next"]/div/div[1]/article/div[3]/a[3]').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.url_changes(url))

new_url = driver.current_url
table_2 = get_table_data(new_url)
print(table_2)


driver.quit()