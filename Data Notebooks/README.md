<a name="readme-top"></a>
<div align="center">

  <img src="https://github.com/CameronCSS/Programming-Languages/assets/121735588/12929bf3-b722-46e8-bb00-39ca8d317858" alt="kaggleLogo" width="200">

  <h2 align="center">Jupyter (Data) Notebooks</h2>
  <p align="center">
  All of my python Notebook code :computer: and practice projects will be here.
   <br> <sub><a href="https://cameroncss.com/#contact">Contact me</a></sub>
<br>
    <br>
     <a href="https://github.com/CameronCSS/Programming-Languages"><strong>« Back to Programming Languages</strong></a>
  </p>
</div>

# Jupyter Notebooks

#### Jupyter Notebooks are highly useful for running Python projects as they allow for the execution of code in a step-by-step manner, visualizing data, documenting the project workflow, and facilitating collaboration, making it ideal for data analysis, prototyping, and presenting results.

<br>

## Price Comparison using Selenium

Using Selenium and python I scraped products and their prices from the first page of two websites based on search input the user enters.

The prices are then averaged and compared from the two websites to see which one has better pricing.

*CODE SNIPPET*
↘️
```python
    print(f"Average price on {website1_name}: ${average_website1:.2f}")
    min_price, max_price = get_min_max(prices_website1)
    if min_price and max_price:
        print(f"Lowest price on {website1_name}: {min_price['name']} at ${min_price['price']:.2f}")
        print(f"Highest price on {website1_name}: {max_price['name']} at ${max_price['price']:.2f}")

    print(f"\nAverage price on {website2_name}: ${average_website2:.2f}")
    min_price, max_price = get_min_max(prices_website2)
    if min_price and max_price:
        print(f"Lowest price on {website2_name}: {min_price['name']} at ${min_price['price']:.2f}")
        print(f"Highest price on {website2_name}: {max_price['name']} at ${max_price['price']:.2f}")
```

Full Notebook and code [HERE](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/Price%20Comparison.ipynb)

------------

## Python Job Scraping

Using Beautiful soup and requests_html I was able to scrape python job data from [https://pythonjobs.github.io/](https://pythonjobs.github.io/)

This is the first project I used pagination to explore linked pages to gather even more information about each job.

*CODE SNIPPET*
↘️
```python
job_card = soup.find_all('div', class_='job')

for job_element in job_card:
    title_element = job_element.find("h1")
    location_element = job_element.find_all("span", class_="info")
    company_element = location_element[3].get_text(strip=True) if len(location_element) > 3 else "N/A" # all the "i class" spans are called the same thing. The fourth one is the company so we specify [3]
    detail_element = job_element.find("p", class_="detail")

    print("Title:", title_element.text.strip())
    print("Location:", location_element[0].text.strip()) # all the "i class" spans are called the same thing. The first one is the actual location
    print("Company:", company_element)
    print("Details:", detail_element.text.strip())
    print()  # Add an empty line for spacing between job listings
```

You can explore the full Notebook and code [HERE](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/Python%20Job%20scraping.ipynb)


--------------

# Kaggle Notebooks
〰️ I have really started to enjoy using Kaggle Notebooks because of the ability to load them up no matter where I am. 
Dont need to install anything. Also you can instally load in data sets from Kaggle. Its a really convenient tool.

## 🔹Roller Coaster data exploration

##### ▶️ [View the full Notebook code](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/Kaggle_Coasters.ipynb)

Explored a database of roller coaster information that dates back to the early 1900s.

↘️ First we load in the data
```python
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('max_columns', 200)
df = pd.read_csv('../input/rollercoaster-database/coaster_db.csv')
```

Few random data points from exploring the data
---

### Top years coasters were introduced

```python
ax = df['Year_Introduced'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')
```
<img src="https://user-images.githubusercontent.com/121735588/230255659-dfda620d-7e13-43b9-8ab4-3c3b293a57bf.png" alt="kaggleLogo" width="400">


### Speed vs Height
```python
df.plot(kind='scatter', x='Speed_mph', y='Height_ft', title='Coaster Speed vs Height')
plt.show()
```
<img src="https://user-images.githubusercontent.com/121735588/230255743-d0c73d31-986d-414d-bd99-0cc27a0d17ae.png" alt="kaggleLogo" width="400">

### Average speed

```python
ax = df.query('Location != "Other"') \
    .groupby('Location')['Speed_mph'] \
    .agg(['mean', 'count']) \
    .query('count >= 10') \
    .sort_values('mean')['mean'] \
    .plot(kind='barh', figsize=(12,5), title='Average Coaster speed by Location w/ 10+ Coasters')
ax.set_xlabel('Average Coaster Speed')
plt.show()
```
<img src="https://user-images.githubusercontent.com/121735588/230256322-5ed9d29f-ae77-44a6-8eed-78dae704ede6.png" alt="kaggleLogo" height="250">

##### ▶️ [View the full Notebook code](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/Kaggle_Coasters.ipynb)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

----

## 🔹'Rob sleep predictions' Kaggle competition to predict his sleep patterns using a sample dataset.
You can find Rob's profile on kaggle [here](https://www.kaggle.com/robikscube)

This is the first Kaggle competition I have entered, and the first time I have tried using predictive models.

##### ▶️ You can view the full current model and output of my Entry [HERE](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/rob-sleep-predictions.ipynb)

*I have gone through about 30 iterations of this model. Trying to Both increase my overall score, 
AND figure out what the heck I am doing.*

### When we first look at the data we can see there is an outlier. 
Its bad enough that we need to fix it. It turns out the data during this time was doubled.

```python
plt.figure(figsize=(10, 8))
sns.lineplot(data=train, x='date', y='sleep_hours')
plt.xlabel('Date')
plt.ylabel('Sleep Hours')
plt.title('Sleep Hours over Time')
plt.grid()


plt.show()
```
<img src="https://user-images.githubusercontent.com/121735588/230258657-fcfaed1e-3537-483d-b1af-ec7f2c74b19d.png" alt="kaggleLogo" height="300">

↘️ We need to find these dates so we can remove them
```python
sleep_over_13 = train[train.sleep_hours > 13]


min_date = sleep_over_13.date.min()
max_date = sleep_over_13.date.max()

print(f"Minimum date where sleep time was over 13 hours: {min_date}")
print(f"Maximum date where sleep time was over 13 hours: {max_date}")
```
```
RESULTS:
Minimum date where sleep time was over 13 hours: 2017-09-29 00:00:00
Maximum date where sleep time was over 13 hours: 2018-06-12 00:00:00
```

🔸 Lets remove these dates
```python
train_copy = train.copy()

doubled_hours = train_copy[(train_copy.date >= '2017-09-28') & (train_copy.date <= '2018-06-12')]

train_copy.loc[doubled_hours.index, 'sleep_hours'] = doubled_hours.sleep_hours / 2
```

### ↘️Results:
<img src="https://user-images.githubusercontent.com/121735588/230259336-fd52c606-95b4-4478-903d-a8e0d637064d.png" alt="kaggleLogo" height="200">

### I then adjusted hours for Holidays and weekends manually. I played with these values until I got something that gave me the best results.

##### ▶️ You can view the full current model and output of my Entry [HERE](https://github.com/CameronCSS/Programming-Languages/blob/main/Data%20Notebooks/rob-sleep-predictions.ipynb)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

----

### View My Other Projects
 <sub>**Click arrow to view content*</sub>
 
 <details>
<summary>Programming Projects / Code</summary>

  ## Python Projects
<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/Python%20Wage%20Calculator" target="new">Python Wage Calculator</a>

&nbsp; &nbsp; - Learned the power of Pandas and PyQt5 libraries. Also learned the importance of notating code for Bug fixing in the future.

## R* Projects
<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/Comparing%20Phone%20Prices%20in%20R" target="new">Comparing Phone Prices in R</a>

&nbsp; &nbsp; - Explored and cleaned a cell phone price dataset found on [Kaggle](https://www.kaggle.com/datasets/rkiattisak/mobile-phone-price).

<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/R-Basics" target="new">R* Basics</a>

&nbsp; &nbsp; - Made a full breakdown detailing the basic functions and uses of the R* programming language.

## Javascript Projects
<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/Javascript" target="new">Javascript Code</a>

&nbsp; &nbsp; - A repo full of my Javascript code. Lots of custom stuff made to work on Carrd websites.
</details>

<details>
  <summary>SQL Queries</summary>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/8%20Weeks%20of%20SQL" target="new">8 Weeks of SQL</a>
<br>
&nbsp; &nbsp; - Explored complex queries to clean data, compute customer figures, and organize data in unusual ways.
<br>
<br>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/Data%20Lemur%20SQL%20Questions" target="new">Data Lemur SQL Questions</a>
<br>
&nbsp; &nbsp; - SQL interview questions using CTEs, multiple joins, subqueries, aggregations, and other advanced SQL functions.
<br>
<br>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/Khan%20Academy%20Advanced%20SQL" target="new">Khan Academy Advanced SQL</a>
<br>
&nbsp; &nbsp; - Expand SQL knowledge about combining tables with JOINs and using multiple queries at once.
<br>
<br>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/SQLbolt%20-%20SQL%20lessons" target="new">SQLbolt - SQL lessons</a>
<br>
&nbsp; &nbsp; - Refreshed foundational understanding of SQL and discovered context variations among SQL-powered platforms.
<br>

</details>

<details>
<summary>Data Analysis / Visuals Projects</summary>
<a href="https://github.com/CameronCSS/Data-Analysis/tree/main/Power-BI-Dashboards" target="new">Power BI Dashboards</a>
<br>
&nbsp; &nbsp; - Collection of my Power BI projects/dashboards with detailed analysis and visually appealing data.
<br>
<br>
<a href="https://cameroncss.github.io/Data-Analysis/Netflix/index.html" target="new">Netflix Movies and TV Shows</a>
<br>
&nbsp; &nbsp; - Built out multiple sheets to display on a single visual, and created an interactive dashboard.
<br>	
<br>
<a href="https://github.com/CameronCSS/Data-Analysis/tree/main/SLC%20civilian%20complaints" target="new">SLC civilian complaints</a>
  <br>
&nbsp; &nbsp; - Utilized API calls to gather data from public sources. Built a local DB to use in Power BI to uncover valuable insights.
  <br>
 </details>


----

<a name="Contact"></a> 
## <a href="https://cameroncss.com/#contact">Contact Me</a>

  </table>
  <p style="margin-left: auto;">
    <a href="https://drive.google.com/file/d/1YaM4hDtt2-79ShBVTN06Y3BU79LvFw6J/view?usp=sharing" target="_blank" rel="noopener noreferrer">
      <img src="https://user-images.githubusercontent.com/121735588/215364205-abdfc0ac-53db-4733-8d43-b57c1bafb802.png" alt="Resume button">
    </a>
  </p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
