import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def sns_xcount(column , data):
    sns.countplot(x = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();

#writting helper function to help us make y-axis countplots in our EDA process
def sns_ycount(column , data):
    sns.countplot(y = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();
    
    
def plotting_trends(data, column):
    #set rating_timestamp as the index
    #set rating_timestamp as the index
    trends_data = data.set_index("column")
    #yearly resampling 
    yearly_trend = trends_data.resample("Y").size()
    #plotting the trend
    plt.figure(figsize= (15, 6))
    yearly_trend.plot(marker = "o", linestyle = "--", color = "red")
    plt.title("The trend of ratings yearly over the years")
    plt.xlabel("rating_timestamp")
    plt.ylabel("count")
    plt.show();