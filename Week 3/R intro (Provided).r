#Loads the plotting library
library(ggplot2)

#Loads the data
custdata = read.table(file.choose(), header=TRUE, sep='\t')

#Plots an histogram of the ages in the data
ggplot(custdata) + geom_histogram(aes(x=age), binwidth = 5)

#Plots a bar chart of the marital status in the data
ggplot(custdata) + geom_bar(aes(x=marital.stat))

#Is there correlation between age and income?
cor(custdata$age,custdata$income)#Not too much

#Create a new dataframe
custdata2 = subset(custdata,(custdata$age>0 & custdata$age<100 & custdata$income>0))
