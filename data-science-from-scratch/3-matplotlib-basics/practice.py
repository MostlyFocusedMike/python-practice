from matplotlib import pyplot as plt
import math

max_num = 11
x_data = range(max_num)
y_data = [(r ** 2) * math.pi for r in range(0,max_num)]
y_data2 = [2 * r * math.pi for r in range(0,max_num)]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [y_data]
plt.plot(x_data, y_data, color="blue", label='Area')
plt.plot(x_data, y_data2, color="green", label='Circ')

# label x-axis with movie names at bar centers
# both need to be the same length and lists
plt.legend(loc=9)
plt.axis([0,max_num, 0,350])
plt.title("My Favorite Movies")     # add a title
plt.xlabel("Area of circle")   # label the y-axis
plt.ylabel("Circumfrence")   # label the y-axis


plt.show()