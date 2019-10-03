from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]

# friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
#                (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
#                (6, 7), (6, 8), (6, 9)]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""

    # dict of freinds keys=user id element 1, values=list of user ids element 2
    d = defaultdict(list)
    # max length
    m = 0
    for k, v in friendships:
        d[users.get(k)].append(users.get(v))
    for k, v in friendships:
        d[users.get(v)].append(users.get(k))
    # user1 = [i[0]for i in friendships]
    for d in d.items():
        if len(d[1]) > m:
            m = len(d[1])
            user = d[0]
            friends = d[1]

    return user, friends


# def main():

#     print('here ...')
#     # user, friends = get_friend_with_most_friends()
#     # assert user == 'sara'
#     # assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']

#     user, friends = get_friend_with_most_friends(friendships)
#     assert user == 'joyce'
#     assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
#                                      'rod', 'sara']

#     # print(user, friends)


# if __name__ == '__main__':
#     main()
