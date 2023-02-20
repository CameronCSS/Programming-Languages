<a name="readme-top"></a>
<div align="center">


  <img src="https://user-images.githubusercontent.com/121735588/219983299-6d97a24d-3b74-49c4-a8cc-3640313e073a.png" height="200">

   <br> <sub><a href="https://cameroncss.com/#contact">:wavy_dash: Contact me :wavy_dash:</a></sub>
<br>
    <br>
     <a href="https://github.com/CameronCSS/PersonalProjects/blob/main/README.md"><strong>« Back to Portfolio</strong></a>
  </p>
</div>

----

## Amazon Web Scraper

**Before we start coding anything we want to decide if we will be using Visual code, or Jupyter Notebook, or any other coding environment.**
<br>
For this project we will be using [Jupyter](https://jupyter.org/)

<sub> If you aren't sure how to install Jupyter you can watch this tutorial by Alex the Analyst. [(Click Here)](https://www.youtube.com/watch?v=WUeBzT43JyY)
  <br>

<div align="left">

  <img src="https://user-images.githubusercontent.com/121735588/219982953-547e5160-a64f-47be-b6e2-13d95aea99d9.png" height="100">

  </div>
  
<br>
  <br>
  
**STEP ONE:**

Lets Import our librarys
  
```python 
# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

# imports the smtplib library so we can email ourselves
import smtplib
```
<br>
  
**STEP TWO:**
  
Next we need to get our **'Headers'** information

This is as simple as going to [http://httpbin.org/get](http://httpbin.org/get) and copy/pasting the information into our jupyer notebook.
  
  **NOTE: We only need the "User-Agent" section of this information*


  <div align="left">

  <img src="https://user-images.githubusercontent.com/121735588/219983662-19e08352-ed40-4a0a-813a-6e93f0cd8061.JPG">

  </div>

Now paste this "User-Agent" info into the following code

```python
# Connect to Website

URL = ' INSERT AMAZON PRODUCT YOU WANT TO EXAMINE '

headers = ' YOUR USER-AGENT INFO ' , ' THE CODE BELOW '

```
  
<br>
  
**PASTE this ```↓``` Code after your User-Agent info (make sure a comma is between the two parts of code!)*

```
"Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
```

<sup>You dont really need to know what this does. But if you are curious you can click below to learn more</sup>

<details>
  <summary>What that code does</summary>
  <li>User-Agent" specifies the name and version of the client software making the request.</li>
 <li>"Accept-Language" specifies the preferred language for the response.</li>
 <li>"Accept-Encoding" specifies the preferred encoding for the response.</li>
 <li>"Accept" specifies the types of content that are acceptable for the response.</li>
 <li>"DNT" is the Do Not Track header, which indicates that the user does not want to be tracked.</li>
 <li>"Connection" specifies the type of connection the client prefers.</li>
 <li>"Upgrade-Insecure-Requests" is a header that requests the server to upgrade a connection to HTTPS.</li>
  </details>

  
###  Our code so far
```python
# Connect to Website

URL = '[https://www.amazon.com/gp/product/B08ZXNDNYQ/ref=ox_sc_act_title_2?smid=AIRTAZFQ2QJOC&psc=1](https://www.amazon.com/DEPSTECH-Autofocus-Microphone-Computer-Streaming/dp/B08ZXNDNYQ/ref=sr_1_4?crid=2CE6Y4BZR17ZG&keywords=4k+webcam&qid=1676853653&sprefix=4k+webcam%2Caps%2C151&sr=8-4&ufe=app_do%3Aamzn1.fos.18630bbb-fcbb-42f8-9767-857e17e03685)'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
  
```

### Now we need to make use of the libraries we imported earlier
  
```python
# Connect to Website and pull in data

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='priceblock_ourprice').get_text()


print(title)
print(price)
  
```
  
### The above code is the old method, which can be found from Alex the Analyst on youtube [(Click Here)](https://www.youtube.com/watch?v=HiOtQMcI5wg)
  <br>

```diff 
- Amazon has changed their policies.
- It is no longer possible to scrape their information using this method

+ I am currently building a new version that will actually work.
```
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

---

### View My Other Projects
    
<details>
  <summary>SQL Queries</summary>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/8%20Week%20SQL%20Challenge%20%23%201" target="new">8 Week SQL Challenge # 1</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Explored complex queries to clean data, compute customer figures, and organize data in unusual ways.
<br>
<br>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/Khan%20Academy%20Advanced%20SQL" target="new">Khan Academy Advanced SQL</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Expand SQL knowledge about combining tables with JOINs and using multiple queries at once.
<br>
<br>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/SQLbolt%20-%20SQL%20lessons" target="new">SQLbolt - SQL lessons</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Refreshed foundational understanding of SQL and discovered context variations among SQL-powered platforms.
<br>

</details>

<details>
<summary>Data Analysis / Visuals Projects</summary>
<a href="https://github.com/CameronCSS/Data-Analysis/tree/main/Power-BI-Dashboards" target="new">Power BI Dashboards</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Collection of my Power BI projects/dashboards with detailed analysis and visually appealing data.
<br>
<br>
<a href="https://cameroncss.github.io/Data-Analysis/Netflix/index.html" target="new">Netflix Movies and TV Shows</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Built out multiple sheets to display on a single visual, and created an interactive dashboard.
<br>	
<br>
<a href="https://github.com/CameronCSS/Data-Analysis/tree/main/SLC%20civilian%20complaints" target="new">SLC civilian complaints</a>
  <br>
&nbsp; &nbsp;:arrow_right_hook: - Utilized API calls to gather data from public sources. Built a local DB to use in Power BI to uncover valuable insights.
  <br>
 </details>
	
<details>
<summary>Programming Projects / Code</summary>
<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/Python%20Wage%20Calculator" target="new">Python Wage Calculator</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Learned the power of Pandas and PyQt5 libraries. Also learned the importance of notating code for Bug fixing in the future.
<br>
<br>
<a href="https://github.com/CameronCSS/Programming-Languages/tree/main/R-Basics" target="new">R* Basics</a>
<br>
&nbsp; &nbsp;:arrow_right_hook: - Made a full breakdown detailing the basic functions and uses of the R* programming language.
<br>
</details>


----

<a name="Contact"></a> 
## <a href="https://cameroncss.com/#contact">Contact Me</a>

  </table>
  <p style="margin-left: auto;">
    <a href="https://docs.google.com/document/d/1idTVL4nRGOejqW6EkpfhsD-dNQRLzmX08y5hI3TYLns/edit?usp=sharing" target="_blank" rel="noopener noreferrer">
      <img src="https://user-images.githubusercontent.com/121735588/215364205-abdfc0ac-53db-4733-8d43-b57c1bafb802.png" alt="Resume button">
    </a>
  </p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
