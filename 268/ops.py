# import math

# def _is_power_of_2(n: int) -> bool:

#     x = 1

#     if n == 1:
#         return True
#     else:
#         while math.pow(2, x) <= n:
#             if math.pow(2, x) == n:
#                 return True
#             x += 1
#     return False

import queue
from collections import deque

class Node:

    def __init__(self, val, level):
        self.val = val
        self.level = level


# class ImprovedQueue(queue.Queue):

#     def to_list(self):
#         """
#         Returns a copy of all items in the queue without removing them.
#         """
#         with self.mutex:
#             return list(self.queue)


def num_ops(n: int) -> int:
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    # you code

    # base = 1  # base
    # ops = 0  # number of ops

    # result = base * 2
    # # print(result)
    # ops += 1
    # i = 1
    # # while result != n and i < 20:
    # while result != n:
    #     if result < n:
    #         result *= 2
    #         ops += 1
    #         print(result, ops, 'x')
    #     if result > n:
    #         result = result // 3
    #         ops += 1
    #         print(result, ops, '//')
    #     i += 1

    # return ops

    # To keep track of visited numbers in BFS
    visit = set()

    # Create a queue and enqueue base into it
    q = queue.Queue()
    # q = deque()
    # x =
    q.put(Node(1, 0))
    # q.append(x)

    loop_num = 1

    # Do BFS starting from x
    # while not q.empty() and loop_num <= 100:
    while not q.empty():
        # while q:

        # print(q.qsize())
        # Remove an item from queue
        t = q.get()
        # t = q.popleft()
        print('val{}'.format(t.val))

        # If the removed item is target number y, return its level
        if (t.val == n):
            return t.level

        # Mark dequeued number as visited
        visit.add(t.val)
        print(visit)

        # If we can reach n in one more step
        if (t.val * 2 == n or t.val // 3 == n):
            return t.level + 1

        # Insert children of t if not visited already
        if (t.val * 2 not in visit):
            # print('here')
            # x.val = t.val * 2
            # x.level = t.level + 1
            # print(x.val, x.level)
            # q.put(x)
            q.put(Node(t.val * 2, t.level + 1))
            # print(x.val, x.level)
            # q.append(x)
            # q.append(Node(t.val * 2, t.level + 1))
            # print([e.val for e in q])
            # print([elem.val for elem in list(q)])
            # print([q_item.val for q_item in q.queue])
        if (t.val // 3 > 0 and t.val // 3 not in visit):
            # print('here2')
            # x.val = t.val // 3
            # x.level = t.level + 1
            # print(x.val, x.level)
            # q.put(x)
            q.put(Node(t.val // 3, t.level + 1))
            # print(x.val, x.level)
            # q.append(x)
            # q.append(Node(t.val // 3, t.level + 1))
            # print([e.val for e in q])
            # print([elem.val for elem in list(q)])
            # print([q_item.val for q_item in q.queue])
        # print('level{}\n'.format(t.level + 1), 'loop{}\n'.format(loop_num))
        loop_num += 1


def main():
    # print('please look after west bengal...')
    print(num_ops(3012))
    # n1 = Node(1, 0)
    # print(n1.val, n1.level)
    # print(type(n1))


if __name__ == '__main__':
    main()
