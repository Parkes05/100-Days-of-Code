import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_btc_search = pd.read_csv('75/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('75/Daily Bitcoin Price.csv')
df_telsa = pd.read_csv('75/TESLA Search Trend vs Price.csv')
df_unemployment = pd.read_csv('75/UE Benefits Search vs UE Rate 2004-20.csv')

# print(df_btc_search.head())
# print(df_btc_price.head())
# print(df_telsa.head())
# print(df_unemployment.head())

# print(df_btc_search.shape)
# print(df_btc_price.shape)
# print(df_telsa.shape)
# print(df_unemployment.shape)

# print(df_telsa.columns)
# print(df_unemployment.columns)


# print(df_telsa['TSLA_WEB_SEARCH'].max())
# print(df_telsa['TSLA_WEB_SEARCH'].min())
# print(df_telsa.describe())


# print(df_btc_search.isna().values.any())
# print(df_btc_price.isna().values.any())
# print(df_telsa.isna().values.any())
# print(df_unemployment.isna().values.any())


# print(df_btc_price.isna().values.sum())
# print(df_btc_price[df_btc_price['CLOSE'].isna()])
df_btc_price.dropna(inplace=True)
# print(df_btc_price.isna().values.any())


# print(type(df_btc_price['DATE'][0]))
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
df_telsa['MONTH'] = pd.to_datetime(df_telsa['MONTH'])
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])
# print(type(df_btc_price['DATE'][0]))


df_btc_monthly = df_btc_price.resample('M', on='DATE') # converts daily data to monthly data
df_btc_last = df_btc_monthly.last() # want the last price - price at the end of the month
df_btc_average = df_btc_monthly.mean() # want the average of the prices
# print(df_btc_last)
# print(df_btc_average)


years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')


plt.figure(figsize=(12,6), dpi=120)
# plt.title('Telsa Web Search vs Price', fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

# ax1.set_xlabel('Month', fontsize=14)
# ax1.set_ylabel('TLSA Stock Price', fontsize=14, c='r')
# ax2.set_ylabel('Search Trend', fontsize=14 , color='blue')

# ax1.set_xlim(df_telsa['MONTH'].min(), df_telsa['MONTH'].max())
# ax1.set_ylim(0, 600)
# ax2.set_ylim(0, 55)


# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)


# ax1.plot(df_telsa['MONTH'], df_telsa['TSLA_USD_CLOSE'], color='#FF0000', linewidth=2)
# ax2.plot(df_telsa['MONTH'], df_telsa['TSLA_WEB_SEARCH'], c='b', linewidth=2)

# plt.show()


plt.title('Bitcoin News Search vs Resampled Price', fontsize=14)

ax1.set_ylabel('BTC price', fontsize=14, c='r')
ax2.set_ylabel('Search Trend', fontsize=14 , color='blue')

ax1.set_xlim(df_btc_search['MONTH'].min(), df_btc_search['MONTH'].max())
ax1.set_ylim(0, 14500)
ax2.set_ylim(0, 150)


# adding grid
ax1.grid(color='red', linestyle='--')
ax2.grid(color='blue', linestyle='--')


# linestyle and markers
# ax1.plot(df_btc_last.index, df_btc_last['CLOSE'], color='#FF0000', linewidth=2, linestyle='--')
# ax2.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], c='b', linewidth=2, marker='o')


# plt.tight_layout(h_pad=5)

# plt.show()


# calculating the rolling average of the data
rolled_last_df = df_btc_last['CLOSE'].rolling(window=6).mean()
rolled_search_df = df_btc_search['BTC_NEWS_SEARCH'].rolling(window=6).mean()
print(rolled_last_df)
print(rolled_search_df)

ax1.plot(df_btc_last.index, df_btc_last['CLOSE'], color='#FF0000', linewidth=2, linestyle='--')
ax2.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], c='b', linewidth=2, marker='o')

plt.show()
