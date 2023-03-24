install.packages("gapminder") #install gapminder dataset if its not already installed
library(gapminder)

summary(gapminder)
mean(gapminder$gdpPercap)
x <- mean(gapminder$gdpPercap)
x #test that x took the data

attach(gapminder) #attach makes it so you dont have to keep defining the db
median(pop)
hist(log(pop))
boxplot(lifeExp ~ continent)
plot(lifeExp ~ log(gdpPercap))

install.packages("dplyr") #install dplyr if its not already installed
library(dplyr)
install.packages("ggplot2") #install ggplot2 if its not already installed
library(ggplot2)

#create a df called df1 to run the t test
df1 <- gapminder %>% 
  select(country, lifeExp) %>% 
  filter(country == "South Africa" |
           country == "Ireland")

t.test(data = df1, lifeExp ~ country)


gapminder %>% 
  filter(gdpPercap < 50000) %>% 
  ggplot(aes(x=log(gdpPercap), y=lifeExp, col=year, size=pop)) +
  geom_point(alpha=0.3)+
  geom_smooth(method = lm)+
  facet_wrap(~continent)

summary(lm(lifeExp ~ gdpPercap+pop))
