#Library import for visualizations
library(ggplot2)

#Reads the file with the data
business_data = read.csv(file.choose())

#Plots a bar chart with state frecuency
ggplot(bussiness_data) + geom_bar(aes(x=state), fill='gray')

#Plots a bar chart with stars given frecuency
ggplot(bussiness_data) + geom_bar(aes(x=stars), fill='gray')
#Plots a pie chart with stars given
ggplot(data=bussiness_data, aes(x=factor(1), fill=factor(stars))) + geom_bar(width=1) + coord_polar(theta="y")


#* SECOND PART *#

#Reads the data
user_data = read.csv(file.choose())

#Creates a new dataser from the general dataset, containing only vote info
user_votes = user_data[,c("cool_votes", "funny_votes", "useful_votes")]

#Is there correlation between the number of fans and the funny votes? Kinda yes.
cor(user_data$funny_votes,user_data$fans)

#A linear model to see how useful_votes is related to fans and revie_count in the user_data dataset.
my.lm = lm(useful_votes ~ review_count + fans,data = user_data)

#Calculatets the coefficients for the created linear model and shows them.
coeffs = coefficients(my.lm)
coeffs
#useful_votes = 1.41 * review_count + 22.68 * review_count - 18.2596
#Plots review_count
ggplot(user_data) + geom_bar(aes(x=review_count), fill='gray')

#Cluster columns 3 to 11 of user_data dataset using k-means technique. k=3
userCluster = kmeans(user_data[,c(3,11),3])

#Plots the cluster. It requires a lot of memory.
ggplot(user_data,aes(review_count,fans, color=userCluster%cluster)) + geom_point()