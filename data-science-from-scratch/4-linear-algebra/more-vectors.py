from matplotlib import pyplot as plt
# The new versions of arrows seem not well documented (even though we can see the guy using them in the book)
# https://stackoverflow.com/questions/52612812/make-arrow-head-shape-symmetric-regardless-of-the-angle-of-the-arrow-in-matplotl
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html
def arrow(color='red', full=True):
    head_style = '-|>' if full else '->'
    return dict(
        arrowstyle=f"{head_style},head_width=0.4,head_length=0.8",
        shrinkA=0,
        shrinkB=0,
        color=color
    )

plt.xticks(range(-10,11))
plt.yticks(range(-10,11))
# xy is where it ends, xytext is where it starts...for some reason
plt.annotate("", xy=(2,5), xytext=(0,0), arrowprops=arrow('red'))
plt.annotate("", xy=(3,-3), xytext=(0,0), arrowprops=arrow('blue', False))

plt.show()
# Now close out the window to see the vector moved and the computation carried out
plt.gca().clear()


plt.xticks(range(-10,11))
plt.yticks(range(-10,11))
plt.annotate("", xy=(2,5), xytext=(0,0), arrowprops=arrow('red'))
plt.annotate("", xy=(5,2), xytext=(2,5), arrowprops=arrow('blue', False))
plt.annotate("", xy=(5,2), xytext=(0,0), arrowprops=arrow('green'))
plt.show()

