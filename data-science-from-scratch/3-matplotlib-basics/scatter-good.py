from matplotlib import pyplot as plt

test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes Are Comparable")
# The distortion is a quick fix by making the x/y at least as big as each other
plt.axis("equal") # This is what makes it good
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")

plt.show()