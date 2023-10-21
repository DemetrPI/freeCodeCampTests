import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data. Index column is set to 'date'.
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(df.index, df["value"], color="r", linewidth=1)
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
           xlabel="Date",
           ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Group by year and month, calculate average page views
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Define month names for plotting
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(10, 6))
    plt.title("Average Page Views per Year")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks(ticks=range(4), labels=[str(year) for year in range(2016, 2020)])
    plt.legend(title="Months", labels=month_names)

    # Save image and return fig (don't change this part)
    fig.get_figure().savefig('bar_plot.png')
    return fig.get_figure()

def draw_box_plot():
    # Define month names for plotting
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn) with different colors
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0], hue="year", palette="Set1", legend=False)
    axes[0].set(title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views")

    sns.boxplot(x="month", y="value", data=df_box, order=month_names, ax=axes[1], hue="month", palette="Set2", legend=False)
    axes[1].set(title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
