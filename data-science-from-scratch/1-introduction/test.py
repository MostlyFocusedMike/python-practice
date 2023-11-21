from collections import Counter

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Gref'},
    {'id': 8, 'name': 'Bill'},
    {'id': 9, 'name': 'Bo'},
]
# This creates a graph of user friendships
friendship_pairs = [(0,1), (0, 2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7),(6,8), (7,8), (8,9)]
# friendship_pairs = [(1,2), (1, 3), (2,3), (2,4), (3,4), (4,5), (5,6), (6,7), (6,8),(7,9), (8,9), (9,10)]

# This is a list comprehension it makes it: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
# newlist = [expression for item in iterable if condition == True], with the if condition being optional
# newdict = [expression_with_colon for item in iterable if condition == True], with the conditional being optional
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j) # add j as a friend of user i
    friendships[j].append(i) # add i as a friend to user j


def get_num_of_friends(user):
    """How many friends does _user_ have"""
    return len(friendships[user['id']])

total_connections = sum(get_num_of_friends(user) for user in users)
avg_connections = total_connections / len(users)

num_of_friends_by_id = [{'id': user['id'], 'popularity': get_num_of_friends(user)} for user in users]
num_of_friends_by_id.sort(reverse=True, key=lambda val : val['popularity'])


def get_mutual_friend_ids_bad(user):
    # This is a layered list comprehension and it will return duplicates in the array, which we want to count in the better function
    return [
        mutual_friend_id
        for friend_id in friendships[user['id']]
        for mutual_friend_id in friendships[friend_id]
    ]

def get_mutual_friend_ids_good(user):
    user_id = user['id']
    # Counter takes a list (or other things) and will out put {user_id: num_of_mutual_friends}
    return Counter(
        mutual_friend_id
        for friend_id in friendships[user_id]             # For each of my friends
        for mutual_friend_id in friendships[friend_id]    # find their friends
        if mutual_friend_id != user_id                    # that is not me
        and mutual_friend_id not in friendships[user_id]  # and arent my direct friends
    )


print('-------------------------------------------------------------------------------------------------------------------------')
# This is how you do string interpolation
print(num_of_friends_by_id)
print(f'What is the total number of friends? {total_connections}')
print(f'What is the average number of friends? {avg_connections}')
# We're dealing with a graph network here, and determining "popularity", is really determining the network metric of "degree centrality"
# ie how important of a node is a user?
popular_user = users[num_of_friends_by_id[0]['id']]
print(f'Who is the most popular person? {popular_user}')


print(f'{get_mutual_friend_ids_good(users[4])}')