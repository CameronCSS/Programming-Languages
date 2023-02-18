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

