from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
def round_down_to_tens(value): return (value // 10) * 10 # this would also work with 100 1000 10000 etc

# We're min(grade, 90) because we want 0-10,11-20...81-90,91-100. Without this 90,
# a grade of 100 would round down to...100, which would then fall into its own bucket instead of 91-100
histogram = Counter(min(round_down_to_tens(grade), 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
        histogram.values(),                 # Give each bar its correct height
        10,                                 # Give each bar a width of 8
        edgecolor=(0, 0, 0))                # Black edges for each bar

# x-axis from -5 to 105, to give us padding since after 10 increments, plt doesn't auto pad
# y-axis from 0 to 5
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()