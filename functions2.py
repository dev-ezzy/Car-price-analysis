import seaborn as sns
import matplotlib.pyplot as plt
def sns_ycount(column , data):
    sns.countplot(y = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();
    
#plotting scatter plots
def scatter_plots(y, X):
    plots = X.shape[1]
    cols = 4
    rows = (plots + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 6))
    fig.suptitle(f"Scatter plot of Independent variables vs {y.name}")

    for i, ax in enumerate(axes.flat):
        if i < plots:
            x_col_name = X.columns[i]
            sns.scatterplot(x=X.iloc[:, i], y=y,ax=ax, alpha = 0.8)
            ax.set_xlabel(x_col_name)
            ax.set_ylabel(y.name)
            ax.set_title(f"{x_col_name} vs {y.name}")
            