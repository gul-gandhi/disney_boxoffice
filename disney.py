import pandas as pd
import seaborn as sns
data = pd.read_csv('disney_movies_total_gross.csv', parse_dates=['release_date'])
print(data.head())

#sorting in descending order 
datad = gross.sort_values(by='inflation_adjusted_gross', ascending=False) 
print(datad.head(10))

#extracting year
data['release_year'] = pd.DatetimeIndex(data['release_date']).year
#mean per genre per year
group = data.groupby(['genre','release_year']).mean()
genre_yearly = group.reset_index()
print(genre_yearly.head(10))

#sns.relplot(kind='line', x='release_year', y='inflation_adjusted_gross', hue='genre', data=genre_yearly)

genre_dummies =  pd.get_dummies(data['genre'], drop_first=True)
print(genre_dummies.head())

