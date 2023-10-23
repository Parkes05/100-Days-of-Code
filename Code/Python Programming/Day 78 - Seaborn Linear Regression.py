import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


df = pd.read_csv('cost_revenue_dirty.csv')
pd.options.display.max_columns = 6
# print(df)
# print(df.info())
# print(df.isna().values.any())
# print(df.duplicated().values.any())

# # df['USD_Production_Budget'] = df['USD_Production_Budget'].astype(str).str.replace('$', '')
# # df['USD_Worldwide_Gross'] = df['USD_Worldwide_Gross'].astype(str).str.replace('$', '')
# # df['USD_Domestic_Gross'] = df['USD_Domestic_Gross'].astype(str).str.replace('$', '')
# # df['USD_Production_Budget'] = df['USD_Production_Budget'].astype(str).str.replace(',', '')
# # df['USD_Worldwide_Gross'] = df['USD_Worldwide_Gross'].astype(str).str.replace(',', '')
# # df['USD_Domestic_Gross'] = df['USD_Domestic_Gross'].astype(str).str.replace(',', '')

# # df['USD_Production_Budget'] = pd.to_numeric(df['USD_Production_Budget'])
# # df['USD_Worldwide_Gross'] = pd.to_numeric(df['USD_Production_Budget'])
# # df['USD_Domestic_Gross'] = pd.to_numeric(df['USD_Production_Budget'])
# # df['Release_Date'] = pd.to_datetime(df['Release_Date'])

columns = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']
remove_char = ['$', ',']

for i in columns:
  for j in remove_char:
    df[i] = df[i].astype(str).str.replace(j, '')
  df[i] = pd.to_numeric(df[i])
df['Release_Date'] = pd.to_datetime(df['Release_Date'])

# print(df)
# print(df.info())
# print(df['USD_Production_Budget'].describe())
# print(df['USD_Production_Budget'].mean())
# print(df['USD_Worldwide_Gross'].mean())
# print(df['USD_Worldwide_Gross'].min())
# print(df['USD_Domestic_Gross'].min())
# print(df['USD_Production_Budget'].max())
# print(df['USD_Worldwide_Gross'].max())
# print(df['USD_Production_Budget'].min())
# print(df.sort_values(by='Rank').head(1))
# print(df.sort_values(by='Rank').tail(1))

domestic_gross_zero = df[df['USD_Domestic_Gross'] == 0]
# print(domestic_gross_zero.count())
# print(domestic_gross_zero.sort_values(by='USD_Production_Budget', ascending=False).head())

worldwide_gross_zero = df[df['USD_Worldwide_Gross'] == 0]
# print(worldwide_gross_zero.count())
# print(worldwide_gross_zero.sort_values(by='USD_Production_Budget', ascending=False).head())

international_releases = df.loc[(df['USD_Domestic_Gross'] == 0) & (df['USD_Worldwide_Gross'] != 0)]
# print(international_releases.head())

international = df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
# print(international.head())

release_date = pd.Timestamp('2018-5-1')
future_releases = df[df['Release_Date'] > release_date]
# print(future_releases)
# print(len(future_releases))


data_clean = df.drop(future_releases.index)
# print(data_clean)
# print(data_clean.describe())
made_loss = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
# # percentage = len(made_loss) / len(data_clean)
# percentage = made_loss.shape[0] / data_clean.shape[0]
# print(percentage)


# plt.figure(figsize=(8,4), dpi=200)

# with sns.axes_style('darkgrid'): # set styling on a single chart - ('whitegrid', 'dark',  or 'ticks')
#   ax = sns.scatterplot(data=data_clean, x='USD_Production_Budget', y='USD_Worldwide_Gross', 
#                       hue='USD_Worldwide_Gross', # color
#                       size='USD_Worldwide_Gross') # dot size

# ax.set(ylim=(0, 3000000000), xlim=(0, 450000000), ylabel='Revenue in $ billions', xlabel='Budget in $100 millions')

# plt.show()


# plt.figure(figsize=(8,4), dpi=200)
 
# with sns.axes_style("darkgrid"):
#     ax = sns.scatterplot(data=data_clean, x='Release_Date', y='USD_Production_Budget', hue='USD_Worldwide_Gross', size='USD_Worldwide_Gross',)
 
#     ax.set(ylim=(0, 450000000), xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()), xlabel='Year', ylabel='Budget in $100 millions')
  
# plt.show()


dt_index = pd.DatetimeIndex(data_clean['Release_Date'])
years = dt_index.year

# print(1999//10)
# print(199*10)

decades = years//10 * 10
data_clean['Decade'] = decades

old_films = data_clean.query('Decade <= 1970')
new_films = data_clean.query('Decade > 1970')

# print(old_films)
# print(new_films)


# sns.regplot(data=old_films, x='USD_Production_Budget', y='USD_Worldwide_Gross')


# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#   sns.regplot(data=old_films, x='USD_Production_Budget', y='USD_Worldwide_Gross',scatter_kws = {'alpha': 0.4}, line_kws = {'color': 'black'})


# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style('darkgrid'):
#   ax = sns.regplot(data=new_films, x='USD_Production_Budget', y='USD_Worldwide_Gross', color='#2f4b7c', scatter_kws = {'alpha': 0.3}, line_kws = {'color': '#ff7c43'})
#   ax.set(ylim=(0, 3000000000), xlim=(0, 450000000), ylabel='Revenue in $ billions', xlabel='Budget in $100 millions') 



regression = LinearRegression()
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

# Find the best-fit line
regression.fit(X, y)

# R-squared
regression.score(X, y)


22821538 + 1.64771314 * 350000000
budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')