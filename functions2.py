import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#loading our data
cars = pd.read_csv("data/CarPrice_Assignment.csv")
def sns_ycount(column , data):
    sns.countplot(y = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();
    
#plotting scatter plots
def scatter_plots(y, X):
    plots = X.shape[1]
    cols = 4
    rows = (plots + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    fig.suptitle(f"Scatter plot of Independent variables vs {y.name}")

    for i, ax in enumerate(axes.flat):
        if i < plots:
            x_col_name = X.columns[i]
            sns.scatterplot(x=X.iloc[:, i], y=y,ax=ax, alpha = 0.8)
            ax.set_xlabel(x_col_name)
            ax.set_ylabel(y.name)
            ax.set_title(f"{x_col_name} vs {y.name}")
            fig.subplots_adjust(wspace=0.4, hspace=0.4)
            plt.tight_layout()
            plt.show()
            
#scatter plots of two variables
def scatter(X, y):
    sns.scatterplot(x = X, y= y, data= cars)
    plt.title(f"Relationship of {X} and {y}")
    
#plotting box_plots and point plots
def box_pair_plot(column):
    fig, axes = plt.subplots(nrows= 1, ncols= 2, figsize = (15, 5))
    sns.boxplot(y= "price", x = column, data= cars, hue= None, ax= axes[0])
    # axes[0].title(f"Box_plots of {column} against price")
    sns.pointplot(y= "price", x = column, data= cars, ax= axes[1])
    # axes[1].title(f"Point_plots of {column} against price")
    plt.show()