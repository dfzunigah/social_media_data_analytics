#Libraries import
import matplotlib.pyplot as plt
import pandas as pd

#Reads the data collected
twitter_data = pd.read_csv('results.csv')

#Is there correlation between variables of the dataframe?
print(twitter_data.corr())

twitter_data_subjective = twitter_data[twitter_data['subjectivity']>0.5]

print(twitter_data_subjective.corr())
#plt.scatter(twitter_data.retwc, twitter_data.subjectivity)
