import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns', 200)

df = pd.read_csv('../input/rollercoaster-database/coaster_db.csv')

df.shape

df.head()

df.columns

df.dtypes

df.describe()

df = df[['coaster_name', 
    'Location', 'Status', 
    'Manufacturer', 
    'Opened', 
    'year_introduced', 'latitude', 'longitude', 'Type_Main',
    'opening_date_clean', 
    'speed_mph', 
    'height_ft',
    'Inversions_clean', 'Gforce_clean']].copy()

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

df.isna().sum()

df.loc[df.duplicated()]

df.loc[df.duplicated(subset=['Coaster_Name'])]

df.query('Coaster_Name == "Crystal Beach Cyclone"')

df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date'])] \
    .reset_index(drop=True).copy()

df.head()

df['Year_Introduced'].value_counts()




# PLOTS


ax = df['Year_Introduced'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')

ax = df['Speed_mph'].plot(kind='hist', bins=20, title='Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')

ax = df['Speed_mph'].plot(kind='kde', title='Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')

df.plot(kind='scatter', x='Speed_mph', y='Height_ft', title='Coaster Speed vs Height')
plt.show()

sns.scatterplot(x='Speed_mph', y='Height_ft', data=df, hue='Year_Introduced')
plt.show()

sns.pairplot(data=df, vars=['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce'],
            hue='Type_Main')
plt.show()

df_corr = df[['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce']].dropna().corr()
df_corr

sns.heatmap(df_corr, annot=True)

ax = df.query('Location != "Other"') \
    .groupby('Location')['Speed_mph'] \
    .agg(['mean', 'count']) \
    .query('count >= 10') \
    .sort_values('mean')['mean'] \
    .plot(kind='barh', figsize=(12,5), title='Average Coaster speed by Location w/ 10+ Coasters')
ax.set_xlabel('Average Coaster Speed')
plt.show()

