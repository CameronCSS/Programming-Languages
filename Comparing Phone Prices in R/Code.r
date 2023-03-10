# This is the code used to clean and explore phone prices

phone_price <- read.csv("F:\\Data Analyst\\data sets\\Mobile phone price.csv" , header=TRUE, sep=",")

head(phone_price)
colnames(phone_price)


phone_price$Camera <- gsub(" \\+ ", ",", phone_price$Camera)  # Replace " + " with ","
phone_price$Camera <- as.numeric(phone_price$Camera)  # Convert to numeric
phone_price$Price <- gsub(",", "", phone_price$Price)
phone_price$Price <- as.numeric(phone_price$Price)


# Add "GB" to values in Storage column that don't already have it
phone_price$Storage <- ifelse(grepl("GB", phone_price$Storage), 
                              phone_price$Storage, 
                              paste0(phone_price$Storage, "GB"))

# Remove the space in the GB values in Storage column soo all values have the same format
phone_price$Storage <- gsub(" ", "", phone_price$Storage)


ggplot(phone_price, aes(Screen.Size, Price, color = Brand)) + geom_point() +
labs(title = "Price by Screen Size")

ggplot(phone_price, aes(Battery.Capacity, Price, color = Brand)) + geom_point() +
labs(title = "Price by Battery Capacity")

ggplot(phone_price, aes(x = Brand, y = Price)) +
  geom_boxplot() +
  labs(title = "Price by Brand",
       x = "Brand",
       y = "Price")


ggplot(phone_price, aes(x = factor(Storage, levels = c("32GB", "64GB", "128GB", "256GB")), Price)) + 
  geom_point() +
  labs(x = "Storage", y = "Price") +
  ggtitle("Storage vs Price")



ggplot(phone_price, aes(x = factor(Storage, levels = c("32GB", "64GB", "128GB", "256GB")), Price)) + 
  geom_point() +
  labs(x = "Storage", y = "Price") +
  ggtitle("Storage vs Price") +
facet_wrap(~Brand)



ggplot(phone_price, aes(Main_camera, Price)) + 
  geom_point(size=3) +
  geom_segment(aes(x=Main_camera, 
                   xend=Main_camera, 
                   y=0, 
                   yend=Price)) +
  labs(x = "Camera MP", y = "Price", 
       title = "Camera MP vs Price")

  
  
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
