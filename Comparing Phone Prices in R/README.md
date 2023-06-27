<a name="readme-top"></a>

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/219838644-7893dee1-4ef8-4b73-9255-4e75588f5ff5.png" alt="pythonLogo" width="200" height="200">

  <a href="https://github.com/CameronCSS/PersonalProjects"><strong>« Back to Project Portfolio</strong></a>
</div>
<br>


## Comparing Phone Prices in *R

I found a public dataset on [Kaggle](https://www.kaggle.com/datasets/rkiattisak/mobile-phone-price) that has details about mobile phones and their prices by Brand.
While doing some exploring through the data in R I found a few suprising pieces of information.

<br>

### Data Cleaning
---

Before I could explore anything I had to clean the data. When I first dove in there were some glaring problems with the way it was reading in R.

Examples:

#### Every phone had ALL its cameras (front,back,zoom,etc) in a single column, seperated by a "+" :arrow_heading_down:


<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224199126-13f5fe56-9f0d-49ba-b608-4001e2822a2e.png" alt="pythonLogo" width="600">
</div>


<br>

<br>

#### The Storage column had multiple different formats that needed to be combined. :arrow_heading_down:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224199146-48592e56-368c-4e4b-9af5-b176548d6547.png" alt="pythonLogo" width="600">
</div>



### CLEANING
---
Cleaning was done with a combination of both R and Excel. Depending on the exact item that needed to be cleaned.

Here is an example of some cleaning code done in R. :arrow_heading_down:

```r
phone_price$Camera <- gsub(" \\+ ", ",", phone_price$Camera)  # Replace " + " with ","
phone_price$Camera <- as.numeric(phone_price$Camera)  # Convert to numeric
phone_price$Price <- gsub(",", "", phone_price$Price) # Remove the comma from the price
phone_price$Price <- as.numeric(phone_price$Price)  # set the price as a numeric

# Add "GB" to values in Storage column that don't already have it
phone_price$Storage <- ifelse(grepl("GB", phone_price$Storage), 
                              phone_price$Storage, 
                              paste0(phone_price$Storage, "GB"))

# Remove the space in the GB values in Storage column soo all values have the same format
phone_price$Storage <- gsub(" ", "", phone_price$Storage)

```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br>

## :negative_squared_cross_mark: Discoveries


### Price by Storage

Regardless of brand or style of phone. Storage seems to be the biggest factor in determing the price.

### Code
```r
ggplot(phone_price, aes(x = factor(Storage, levels = c("32GB", "64GB", "128GB", "256GB")), Price)) + 
  geom_point() +
  labs(x = "Storage", y = "Price") +
  ggtitle("Storage vs Price")
```
### Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224203734-88b3c269-0964-4f47-8f84-32f22953284e.png" alt="pythonLogo" width="600">
</div>

----

### Price by Camera

Camera had almost no relation to cost of the Phone. The average camera was around 48MP.

### Code
```r
ggplot(phone_price, aes(Main_camera, Price)) + 
  geom_point(size=3) +
  geom_segment(aes(x=Main_camera, 
                   xend=Main_camera, 
                   y=0, 
                   yend=Price)) +
  labs(x = "Camera MP", y = "Price", 
       title = "Camera MP vs Price")
```
### Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224204097-a053f2db-9303-4f29-afd9-8f7f3fcddbd9.png" alt="pythonLogo" width="600">
</div>

----

### Price by Battery Capacity

Battery also had no relation to cost. The lower and highest capacities both shared the lowest cost.

### Code
```r
ggplot(phone_price, aes(Battery.Capacity, Price, color = Brand)) + geom_point() +
labs(title = "Price by Battery Capacity")
```
### Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224204930-6a6a5a50-110b-4af2-af90-989728c69f6b.png" alt="pythonLogo" width="600">
</div>

----

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<br>

### Price by Screen Size

Screen size had a small factor in price. But nothing notable that makes it a key for manufacturers to raise the price.

### Code
```r
ggplot(phone_price, aes(Screen.Size, Price, color = Brand)) + geom_point() +
labs(title = "Price by Screen Size")
```
### Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224207698-3f8b11ed-4c72-49bc-8111-f6ee577c8ac6.png" alt="pythonLogo" width="600">
</div>

----

### Phone Brand Prices

Despite the common trope that Apple is the most expensive. Apple is actually the most average with their phones having a good spread across the middle.

### All Prices Code
```r
  ggplot(phone_price, aes(Brand, Price, color = Brand)) + 
    geom_point( size=3) +   # Draw points
    geom_segment(aes(x=Brand, 
                     xend=Brand, 
                     y=min(Price), 
                     yend=max(Price)), 
                 linetype="dashed", 
                 size=0.1) +   # Draw dashed lines
    labs(title="Brand Vs Price", 
         caption="source: Kaggle: Mobile Phone Price dataset")
```
### All Prices Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224206039-e885020b-c317-4fd7-ac58-35565882af92.png" alt="pythonLogo" width="600">
</div>


### Avg Price Code
```r
  ggplot(phone_price, aes(Brand, Price, color = Brand)) + 
    stat_summary(fun = "mean", geom = "point", size = 5) +
    geom_segment(aes(x=Brand, 
                     xend=Brand, 
                     y=min(Price), 
                     yend=max(Price)), 
                 linetype="dashed", 
                 size=0.1) +   # Draw dashed lines
    labs(title="Avg. Brand Price", 
         caption="source: Kaggle: Mobile Phone Price dataset")
```
### Avg Price Results :arrow_lower_right:

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/224206033-341b9a5e-1fa9-4660-8e60-4535fe5d3f79.png" alt="pythonLogo" width="600">
</div>


----

# Key Takeaway

Cameras, screen size, battery capacity and all the other gadgets may seem like they play a big role in price. 
But according to this Data storage is the biggest factor in price.

<br>

**I am on the hunt for more data about phone prices to compare these findings...*


---

### View My Other Projects
<sub>**Click arrow to view content*</sub>   
    
<details>
  <summary>SQL Queries</summary>
<a href="https://github.com/CameronCSS/SQL-Queries/tree/main/8%20Week%20SQL%20Challenge%20%23%201" target="new">8 Week SQL Challenge # 1</a>
<br>4
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


----

<a href="https://github.com/CameronCSS/Programming-Languages/blob/main/README.md"><strong>« Back to Programming Projects</strong></a>
<br>
<br>
<a href="https://github.com/CameronCSS/PersonalProjects/blob/main/README.md"><strong>« Back to Portfolio</strong></a>

## <a href="https://cameroncss.com/#contact">Contact Me</a>

  </table>
  <p style="margin-left: auto;">
    <a href="https://drive.google.com/file/d/1YaM4hDtt2-79ShBVTN06Y3BU79LvFw6J/view?usp=sharing" target="_blank" rel="noopener noreferrer">
      <img src="https://user-images.githubusercontent.com/121735588/215364205-abdfc0ac-53db-4733-8d43-b57c1bafb802.png" alt="Resume button">
    </a>
  </p>
</div>
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>
