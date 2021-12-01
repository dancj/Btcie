import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.ticker import MultipleLocator

def plot_series(x, y, title="Price over Time"):
    plt.figure()
    plt.title(title)
    plt.plot(x, y)
    plt.ylabel("Price")
    plt.xlabel("Time")

    ax = plt.gca().get_xaxis()

    ax.set_major_locator(dates.MonthLocator(interval=12))
    ax.set_major_formatter(dates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()

    for item in ax.get_ticklabels():
        item.set_rotation(45)

    plt.show()
    plt.close()