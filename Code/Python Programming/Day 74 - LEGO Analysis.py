import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/colors.csv')
# print(df.head())
# print(df['name'].nunique())

# print(df.groupby('is_trans').size())
# print(df['is_trans'].value_counts())
# mask = df['is_trans'] == 'f'
# count = len(df[mask])
# print(count)


df_sets = pd.read_csv('data/sets.csv')
# pd.options.display.max_columns = 5
# print(df_sets)

# sorted_df = df_sets.sort_values(by=['year'])
# print(sorted_df.head())
# print(sorted_df[sorted_df['year'] == 1949])

# parts = df_sets.sort_values(by=['num_parts'], ascending=False)
# print(parts.head())


sets_by_year = df_sets.groupby('year').count()
# print(sets_by_year['set_num'].head())
# print(sets_by_year[sets_by_year.index == 1995])
# print(sets_by_year[sets_by_year.index == 2019])

# sliced_year = sets_by_year.index[0:-2]
# sliced_set = sets_by_year['set_num'][0:-2]
# print(sliced_year)
# print(sliced_set)

# plt.plot(sliced_year, sliced_set)
# plt.show()


themes_by_year = df_sets.groupby('year').agg({'theme_id': pd.Series.nunique})
# print(themes_by_year.head())
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
# print(themes_by_year.head())
# print(themes_by_year.tail())

# ax1 = plt.gca() # get current axis
# ax2 = ax1.twinx() # create another axis that share the same x-axis

# ax1.plot(themes_by_year.index[0:-2], themes_by_year['nr_themes'][0:-2], color='g', label='Number of Themes')
# ax2.plot(themes_by_year.index[0:-2], sets_by_year['set_num'][0:-2], 'r')

# # add styling
# ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('Number of Themes', color='g', fontsize=14)
# ax2.set_ylabel('Number of Sets', color='r', fontsize=14)

# ax1.legend(fontsize=14)

# plt.show()


# parts_by_set = df_sets.groupby('year').agg({'num_parts': pd.Series.mean})
# print(parts_by_set)

# plt.scatter(parts_by_set.index[0:-2], parts_by_set['num_parts'][0:-2])
# plt.show()


set_theme_count = df_sets['theme_id'].value_counts()
# print(set_theme_count)
set_theme = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
# print(set_theme)


themes_set = pd.read_csv('data/themes.csv')
# # print(themes_set.head())
star_wars = themes_set[themes_set['name'] == 'Star Wars']
# # print(star_wars)
# for id in star_wars['id']:
#     print(df_sets[df_sets['theme_id'] == id])


merged_df = pd.merge(set_theme, themes_set, on='id')
# print(merged_df)
# print(merged_df[0:3])

aggregated_df = merged_df.groupby('name').agg({'set_count': pd.Series.sum})
aggregated_df.sort_values(by='set_count', ascending=False, inplace=True)
# print(aggregated_df)

plt.figure(figsize=(12,6))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)

plt.bar(aggregated_df.index[0:10], aggregated_df['set_count'][0:10])
plt.tight_layout(pad=1.08)
# aggregated_df[:10].plot('name', 'set_count', kind='bar', xlabel='Theme Name', ylabel='Nr of Sets', rot=45, legend=False)

plt.show()