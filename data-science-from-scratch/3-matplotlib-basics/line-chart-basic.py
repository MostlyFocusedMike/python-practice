from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
#          x     y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# add a title
plt.title("Nominal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")

# this open up a window with some limited interactivity that you can run
# will take up terminal if you run it
# plt.show()

# Below would be how to save the image as a file, note that you can't seem to use it when you also use the plt.show() method
# plt.savefig('images/viz_gdp.png')
# plt.gca().clear() if you wanted to clear the same field to keep using it