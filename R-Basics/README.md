<a name="readme-top"></a>

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/219838644-7893dee1-4ef8-4b73-9255-4e75588f5ff5.png" alt="pythonLogo" width="200" height="200">

  <a href="https://github.com/CameronCSS/PersonalProjects"><strong>« Back to Project Portfolio</strong></a>
</div>
<br>


## R Programming Language Basics

R is a programming language and software environment for statistical computing and graphics. Python has gained popularity over the years, but R is still widely used today.
In fact, R is still one of the most popular programming languages for data analysis and machine learning.

<br>

### Why should I use R* ?

---

- FREE and open-source:
<ul>R is a free and open-source language, which means that it can be used by anyone without any licensing fees. This makes it an accessible option for individuals and organizations of all sizes.</ul>

<br>

- Rich ecosystem: 
<ul>R has a very large and active community of developers who contribute to a wide range of packages and tools for data analysis, visualization, and modeling. This means that there are many powerful tools available to R users that are specifically designed for their needs.</ul>

<br>

- Easy to learn:
<ul>R has a relatively easy-to-learn syntax and is designed to be user-friendly for statisticians and data analysts, even those who do not have a strong programming background.</ul>

<br>

- Flexibility:
<ul>R is a highly flexible language that can be used for a wide range of data analysis and modeling tasks, from simple data manipulation to complex machine learning algorithms.</ul>

<br>

- Reproducibility:
<ul>R provides a powerful set of tools for reproducible research, including the ability to create automated reports and share code and data with others.</ul>

----

### The basics of R:
##### *NOTE: This isnt a full collection of everything R can do. Just a summary of the basics*

---

:small_blue_diamond:R is easy to learn!

:small_blue_diamond:R is generally considered to be an easy language to learn and use, 
especially for those who have some background in programming or statistics. 

:small_blue_diamond:Here is some sample R code that demonstrates some basic functionality:


### CODE

```r
# Create a vector of numbers from 1 to 5
my_vector <- c(1, 2, 3, 4, 5)

# Calculate the mean of the vector
mean(my_vector)

# Create a matrix of random numbers
my_matrix <- matrix(rnorm(25), nrow=5, ncol=5)

# Subset the matrix to include only the first two rows and columns
my_subset <- my_matrix[1:2, 1:2]

# Plot the subset as a heatmap
heatmap(my_subset)


```

<br>
<br>

:small_red_triangle_down: Here are some basic items you will encounter in R*.

<br>


<sup> **Click the arrow to view the section* </sup>

<details>
  <summary>DATA TYPES:</summary> 
  
  <br>
 
  | Data Types | Description |
| --- | --- |
| `numeric` | Represents real numbers |
| `character` | Represents text |
| `logical` | Represents Boolean values (`TRUE` or `FALSE`) |
| `factors` | Represents categorical data |
| `vectors` | Represents one-dimensional arrays |
| `matrices` | Represents two-dimensional arrays |
| `arrays` | Represents multi-dimensional arrays |
| `lists` | Represents a collection of objects of different types |

 ---
  
</details>

<details>
  <summary>OPERATORS:</summary> 
  
  <br>

  | Operators | Description |
| --- | --- |
| Arithmetic Operators | |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Exponentiation |
| `%%` | Modulo |
| Logical Operators | |
| `!` | Negation |
| `&` | Element-wise AND |
| `\|` | Element-wise OR |
| `xor()` | Exclusive OR |
| Comparison Operators | |
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |
| Assignment Operators | |
| `<-` or `=` | Assigns a value to a variable |
| `<<-` | Assigns a value to a variable in a parent environment |
| `->` | Assigns a value to a variable, but in the reverse direction |
| `->>` | Assigns a value to a variable in a data frame, but in the reverse direction |

   ---
  
  </details>

<details>
  <summary>FUNCTIONS:</summary>
  
  <br>
  
| Function  | What it does |
| --- | --- |
| `sum()` | Computes the sum of a set of numeric values. |
| `mean()` | Computes the arithmetic mean (average) of a set of numeric values. |
| `sd()` | Computes the standard deviation of a set of numeric values. |
| `var()` | Computes the variance of a set of numeric values. |
| `min()` | Computes the minimum value in a set of numeric values. |
| `max()` | Computes the maximum value in a set of numeric values. |
| `length()` | Computes the length of a vector (i.e., the number of elements it contains). |
| `sort()` | Sorts the elements of a vector in ascending or descending order. |
| `table()` | Computes a frequency table of the values in a vector or matrix. |
| `unique()` | Computes the unique values in a vector or matrix. |
| `rep()` | Replicates a vector or matrix a specified number of times. |
| `seq()` | Generates a sequence of values from a starting value to an ending value with a specified increment. |
| `paste()` | Concatenates strings or vectors of strings together. |
| `subset()` | Subsets a data frame based on specified conditions. |
| `merge()` | Merges two data frames based on common variables. |

   ---
  
  </details>
  
  
<details>
  <summary>CONTROL STRUCTURES:</summary>

  <br>
  
  | Control Structures | Description |
| --- | --- |
| `if-else` Statements | |
| `if (condition) {`<br>&nbsp;&nbsp;`expression1`<br>`} else {`<br>&nbsp;&nbsp;`expression2`<br>`}` | Executes `expression1` if the `condition` is `TRUE`, otherwise executes `expression2` |
| Loops | |
| `for` Loops | |
| `for (variable in sequence) {`<br>&nbsp;&nbsp;`expression`<br>`}` | Executes `expression` for each element in `sequence`, with `variable` taking on the value of each element |
| `while` Loops | |
| `while (condition) {`<br>&nbsp;&nbsp;`expression`<br>`}` | Executes `expression` as long as `condition` is `TRUE` |
| `repeat` Loops | |
| `repeat {`<br>&nbsp;&nbsp;`expression`<br>&nbsp;&nbsp;`if (condition) {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`break`<br>&nbsp;&nbsp;`}`<br>`}` | Executes `expression` repeatedly until a `break` statement is encountered |
| `switch` Statements | |
| `switch (expression,`<br>&nbsp;&nbsp;`case1 = expression1,`<br>&nbsp;&nbsp;`case2 = expression2,`<br>&nbsp;&nbsp;`...,`<br>&nbsp;&nbsp;`default = default_expression`<br>`)` | Executes `expression1` if `expression` matches `case1`, `expression2` if `expression` matches `case2`, and so on. If no matches are found, executes `default_expression`. |

   ---
  
  </details>

<details>
  <summary>PACKAGES:</summary>
  
  <br>
  
  | Package | Description |
| --- | --- |
| `stats` | Provides basic statistical functions |
| `base` | Provides basic functions for data manipulation |
| `utils` | Provides utility functions for system operations |
| `dplyr` | Provides data manipulation functions |
| `ggplot2` | Provides data visualization functions |
| `tidyr` | Provides data wrangling functions |
| `lubridate` | Provides functions for working with dates and times |
| `stringr` | Provides functions for working with character strings |
| `caret` | Provides machine learning functions |
| `forecast` | Provides functions for time series forecasting |

  
  
  <br>
  
  **R has a vast collection of packages that extend the functionality of the base R environment. 
  These packages can be installed and loaded into R to access additional functions and data sets.*
  
   ---
  
  </details>

<details>
  <summary>GRAPHICS:</summary>
  
  <br>
  
| Graphics | Description |
| --- | --- |
| Base Graphics | Provides a range of plotting functions, including:<br> `plot`, `hist`, `boxplot`, `stripchart`, `barplot`, `dotchart`, `pie`, `contour`, `image`, `persp`, `pairs`, `coplot`, `mosaicplot`, and many more. |
| Lattice Graphics | Provides a powerful system for creating conditioned plots, which are plots that show the relationship between variables for subsets of the data. The key functions are:<br> `xyplot`, `bwplot`, `dotplot`, `histogram`, `densityplot`, `stripplot`, and many more. |
| ggplot2 | Provides a system for creating high-quality graphics based on the grammar of graphics. The key functions are:<br> `ggplot`, `geom_point`, `geom_line`, `geom_bar`, `geom_boxplot`, `facet_wrap`, `scale_x_continuous`, and many more. |

  **The base graphics system provides a range of plotting functions, and there are several packages that extend the capabilities of the graphics system.*
  
   ---
  
   </details>

<details>
  <summary>DATA MANIPULATION:</summary>
  
  <br>
  
  | Data Manipulation | Description |
| --- | --- |
| Subsetting | Selects a subset of a data frame based on specified conditions using the `[]` operator, or the `subset()` function. |
| Merging | Combines two or more data frames into a single data frame using the `merge()` function, or the `dplyr::left_join()`, `dplyr::right_join()`, `dplyr::inner_join()`, or `dplyr::full_join()` functions from the dplyr package. |
| Reshaping | Converts data from long to wide format, or vice versa, using the `reshape()` function, or the `tidyr::gather()` and `tidyr::spread()` functions from the tidyr package. |
| Aggregating | Calculates summary statistics for data using the `aggregate()` function, or the `dplyr::summarize()` function from the dplyr package. |

---
  
   </details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
  
## Summary of R
  
  - R is a versatile language and its software environment can be used for a wide range of data analysis and visualization tasks.
  - It is widely used in the data community by users and developers alike.
  - The language is easy to learn, and has a variety of tools and packages that make it easy to use for data analysis and visualization.
  - Overall, R is a powerful and versatile tool for data analysts, statisticians, and scientists working with data.

----

## Sample Data Project

:bookmark_tabs: __Here's a sample data project example using the 'mtcars' dataset that comes with R that demonstrates some common data analysis and visualization tasks:__
<br>
```r
# Load the required packages
library(dplyr)
library(ggplot2)

# Load the data into R (use mtcars dataset as an example)
data <- mtcars

# Examine the structure of the data
str(data)

# View the first few rows of the data
head(data)

# Calculate summary statistics for a numeric variable
summary(data$mpg)

# Create a scatterplot to visualize the relationship between two variables
ggplot(data, aes(x = wt, y = mpg)) +
  geom_point()

# Create a histogram to visualize the distribution of a variable
ggplot(data, aes(x = mpg)) +
  geom_histogram()

# Filter the data to include only rows that meet a certain condition
filtered_data <- filter(data, cyl == 6)

# Group the data by a categorical variable and calculate summary statistics for each group
grouped_data <- group_by(data, cyl) %>%
  summarize(mean_mpg = mean(mpg))

# Create a bar chart to visualize the summary statistics for each group
ggplot(grouped_data, aes(x = cyl, y = mean_mpg)) +
  geom_bar(stat = "identity")


```
<br>


### Sample Output

<br>

```
Attaching package: 'dplyr'

The following objects are masked from 'package:stats':

    filter, lag

The following objects are masked from 'package:base':

    intersect, setdiff, setequal, union

'data.frame':	32 obs. of  11 variables:
 $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
 $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
 $ disp: num  160 160 108 258 360 ...
 $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
 $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
 $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
 $ qsec: num  16.5 17 18.6 19.4 17 ...
 $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
 $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
 $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
 $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
                   mpg cyl disp  hp drat    wt  qsec vs am gear carb
Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  10.40   15.43   19.20   20.09   22.80   33.90 
`stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
`summarise()` ungrouping output (override with `.groups` argument)
```


<br>

<div align=>
<img src="https://user-images.githubusercontent.com/121735588/219881951-fd165485-10f7-466e-b54b-6079d83a83ff.png" width="400" height="400">
</div>

<br>

<div align=>
<img src="https://user-images.githubusercontent.com/121735588/219881964-72ba02da-a5c2-4508-b162-c042c0993527.png" width="400" height="400">
</div>

<br>

<div align=>
<img src="https://user-images.githubusercontent.com/121735588/219881980-5e851ac4-a0ae-4b5b-85b9-b98631b08977.png" width="400" height="400">
</div>

<br>

This code loads the required libraries, dplyr and ggplot2. Then, it loads the mtcars dataset and examines the structure of the data and the first few rows. It calculates summary statistics for a numeric variable, mpg, and creates a scatterplot to visualize the relationship between weight (wt) and mpg. It also creates a histogram to visualize the distribution of mpg. The code then filters the data to include only rows where the number of cylinders (cyl) is equal to 6. Next, it groups the data by the number of cylinders and calculates the mean mpg for each group. Finally, it creates a bar chart to visualize the summary statistics for each group.



----

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
