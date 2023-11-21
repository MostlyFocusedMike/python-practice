from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars, color="green")

# label x-axis with movie names at bar centers
# both need to be the same length and lists
plt.xticks(range(len(movies)), movies)

plt.title("My Favorite Movies")     # add a title
plt.ylabel("# of Academy Awards")   # label the y-axis


plt.show()


# plt.savefig('im/viz_movies.png')

# plt.gca().clear() if you wanted to clear the same field to keep using it