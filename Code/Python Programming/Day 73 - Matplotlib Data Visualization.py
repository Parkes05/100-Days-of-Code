import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('QueryResults.csv', header=0, names=['DATE', 'TAG', 'POSTS'])

df['DATE'] = pd.to_datetime(df['DATE'])

# print(df.head())
# print(df.tail())
# print(df.shape)
# # for i in df.columns:
# #     print(i)
# #     print(df[i].count())
# print(df.count())

# group = df.groupby('TAG')
# print(group.sum())
# print(group.count())
# # print(group.count().idxmin())


# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5]})
# print(test_df)
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

reshaped_df = pd.pivot(df, values='POSTS', index='DATE', columns='TAG')
# print(reshaped_df)
# print(reshaped_df.shape)
# print(reshaped_df.head())
# print(reshaped_df.tail())
# print(reshaped_df.columns)
# print(reshaped_df.count())

reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.isna().values.any())
# pd.options.display.max_columns = 14
# print(reshaped_df)

rolled_df = reshaped_df.rolling(window=12).mean()



# .figure() - allows us to resize our chart
# .xticks() - configures our x-axis
# .yticks() - configures our y-axis
# .xlabel() - add text to the x-axis
# .ylabel() - add text to the y-axis
# .ylim() - allows us to set a lower and upper bound

plt.figure(figsize=(12,7))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of posts', fontsize=14)
plt.ylim(bottom=0, top=35000)
# # plt.plot(reshaped_df.index, reshaped_df['java'])
# # plt.plot(reshaped_df.index, reshaped_df['python'])
# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
for column in reshaped_df.columns:
    plt.plot(rolled_df.index, rolled_df[column], linewidth=2, label=rolled_df[column].name)
plt.legend(fontsize=14)

plt.show()
