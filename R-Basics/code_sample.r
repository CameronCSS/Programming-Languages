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

