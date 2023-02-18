<a name="readme-top"></a>

<div align="center">
<img src="https://user-images.githubusercontent.com/121735588/219838644-7893dee1-4ef8-4b73-9255-4e75588f5ff5.png" alt="pythonLogo" width="200" height="200">
</div>
<br>


## R Programming Language Basics

R is a programming language and software environment for statistical computing and graphics. Python has gained popularity over the years, but R is still widely used today.
In fact, R is still one of the most popular programming languages for data analysis and machine learning.

<br>

### The basics of R:
NOTE: This isnt a full collection of everything R can do. Just a summary of the basics

---

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
  
  - R is a versatile language and software environment that can be used for a wide range of data analysis and visualization tasks.
  - It is widely used in the data community by users and developers alike. 
  - The language is easy to learn, and has a variety of tools and packages that make it easy to use for data analysis and visualization. 
  - Overall, R is a powerful and versatile tool for data analysts, statisticians, and scientists working with data.

----

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


----

<a href="https://github.com/CameronCSS/Programming-Languages/blob/main/README.md"><strong>« Back to Python Projects</strong></a>
<br>
<br>
<a href="https://github.com/CameronCSS/PersonalProjects/blob/main/README.md"><strong>« Back to Portfolio</strong></a>

## Contact Me

<div style="display: flex;">
  <table style="flex: 1;">
  
||
| --- |
| <a href="mailto:CameronSeamons@gmail.com">![gmail icon](https://user-images.githubusercontent.com/121735588/216516513-1bd223b5-89d4-4d02-860e-b132c18c47d9.png):heavy_minus_sign: CameronSeamons@gmail.com |
| <a href="https://www.linkedin.com/in/cameron-css/">![linkedin](https://user-images.githubusercontent.com/121735588/215363352-ad51a5e1-0de8-48be-8ceb-28c610e5d34d.png)</a> :heavy_minus_sign: https://www.linkedin.com/in/cameron-css/|
| <a href="https://twitter.com/Cameron_CSS">![twitter logo](https://user-images.githubusercontent.com/121735588/215363444-e4b080b6-e122-49cb-8b41-601dab6e10eb.png)</a> :heavy_minus_sign: https://twitter.com/Cameron_CSS |

  </table>
  <p style="margin-left: auto;">
    <a href="https://drive.google.com/file/d/19vkbf2HjEpXpxndWYa4A6Dyt6gsnGv73/view?usp=sharing" target="_blank" rel="noopener noreferrer">
      <img src="https://user-images.githubusercontent.com/121735588/215364205-abdfc0ac-53db-4733-8d43-b57c1bafb802.png" alt="Resume button">
    </a>
  </p>
</div>
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>
