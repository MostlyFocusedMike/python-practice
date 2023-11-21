import json
from matplotlib import pyplot as plt
import datetime
import csv
import numpy as np

with open('/Users/mikecronin/Desktop/rpics.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = []
    men = []
    women = []
    line_count = 0
    num = 1000
    for row in csv_reader:
        # id, author, created_utc, title, full_link, url, person_detected, Category, upvote_ratio, score, num_comments
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if row["person_detected"] == 'TRUE' and row["Category"] == 'M' and int(row["score"]) > num and int(row["score"]) > 100:
            line_count += 1
            row['score'] = int(row['score'])
            men.append(row)
        if row["person_detected"] == 'TRUE' and row["Category"] == 'F' and int(row["score"]) > num and int(row["score"]) > 100:
            line_count += 1
            row['score'] = int(row['score'])
            women.append(row)
    print(f'Processed {line_count} lines.')
    women.sort(key=lambda poster: int(poster["score"]))
    men.sort(key=lambda poster: int(poster["score"]))
    # print(men[-1])
    print(men[len(men)//2]['score'])
    print(len(men))
    print(women[len(women)//2]['score'])
    print(len(women))

    data = men + women
    # data.sort(key=lambda poster: int(poster["score"]))
    # data = [val for val in data if val['score'] > 1000]
    x_data = [poster['id'] for poster in data]
    y_data = [poster['score'] for poster in data]


    col = []
    for poster in data:
        if poster["Category"] == 'F':
            col.append('pink')
        elif poster["Category"] == 'M':
            col.append('blue')

    # plt.yscale('log')
    plt.bar(x_data, y_data, color=col)
    # label x-axis with movie Categorys at bar centers
    # both need to be the same length and lists
    plt.title("Posts with over 1000 votes")
    plt.xticks([])
    plt.ylabel("Number of Votes")   # label the y-axis
    plt.xlabel("Posts")   # label the y-axis
    plt.grid(True)

    plt.show()