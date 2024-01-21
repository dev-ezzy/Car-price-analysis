import seaborn as sns
import matplotlib.pyplot as plt
def sns_ycount(column , data):
    sns.countplot(y = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();