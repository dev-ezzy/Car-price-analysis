#importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
#loading our data
cars = pd.read_csv("data/CarPrice_Assignment.csv")

def sns_xcount(column , data):
    sns.countplot(x = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();

#writting helper function to help us make y-axis countplots in our EDA process
def sns_ycount(column , data):
    sns.countplot(y = column, data = data, hue= column)
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
    
def plot_histograms(data):
    
    sns.set(style="dark")

    num_columns = len(data.columns)

    # Calculating the number of rows and columns for the subplots
    num_rows, num_cols = int(num_columns**0.5), -(-num_columns//int(num_columns**0.5))

    f, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

    for i, column in enumerate(data.columns):
        row, col = i // num_cols, i % num_cols
        sns.plot(data[column], kind = "hist", kde=True, ax=axes[row, col])
        axes[row, col].set_title(f'Histogram of {column}')
        axes[row, col].set_xlabel('Values')

    # Remove any empty subplots
    for i in range(num_columns, num_rows * num_cols):
        f.delaxes(axes.flatten()[i])

    plt.tight_layout()
    plt.show();
    
#plotting box_plots and point plots
def box_pair_plot(column):
    fig, axes = plt.subplots(nrows= 1, ncols= 2, figsize = (15, 5))
    sns.boxplot(y= "price", x = column, data= cars, hue= None, ax= axes[0])
    axes[0].set_title(f"Box_plots of {column} against price")
    sns.pointplot(y= "price", x = column, data= cars, ax= axes[1])
    axes[1].set_title(f"Point_plots of {column} against price")
    plt.show()

    