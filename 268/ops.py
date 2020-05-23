# import queue


# class Node:

#     def __init__(self, val, level):
#         self.val = val
#         self.level = level

from collections import deque


def num_ops_old(n: int) -> int:
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

    # To keep track of visited numbers in BFS
    visited = set()

    # Create a queue and enqueue base into it
    q = queue.Queue()
    # q = deque()
    # x =
    q.put(Node(1, 0))
    # q.append(x)

    loop_num = 1

    # Do BFS starting from x
    while not q.empty() and loop_num <= 20:
        # while not q.empty():
        # Remove an item from queue
        t = q.get()
        print('val{}'.format(t.val))

        # If the removed item is target number y, return its level
        if (t.val == n):
            return t.level

        # Mark dequeued number as visited
        visited.add(t.val)
        print(visited)

        # If we can reach n in one more step
        if (t.val * 2 == n or t.val // 3 == n):
            return t.level + 1

        # Insert children of t if not visited already
        # if (t.val * 2 not in visited):
        if (t.val * 2 not in set([q_item.val for q_item in q.queue])):
            q.put(Node(t.val * 2, t.level + 1))
            print([q_item.val for q_item in q.queue])
        # if (t.val // 3 not in visited and t.val // 3 > 0):
        if (t.val // 3 not in set([q_item.val for q_item in q.queue]) and t.val // 3 > 0):
            q.put(Node(t.val // 3, t.level + 1))
            print([q_item.val for q_item in q.queue])
        print('level{}\n'.format(t.level + 1), 'loop{}\n'.format(loop_num))
        loop_num += 1


def num_ops(n: int) -> int:
    de = deque([(1, 0)])
    visited = set()

    if n < 0:
        return 0
    while de:

        res, num_ops = de.popleft()

        # print(de)

        if res == n:
            return num_ops
        else:
            if res // 3 not in visited:
                de.append((res // 3, num_ops + 1))
                visited.add(res // 3)
                # print(visited)
            if res * 2 not in visited:
                de.append((res * 2, num_ops + 1))
                visited.add(res * 2)
                # print(visited,'\n')

    # return de.pop()


def main():
    # print('please look after west bengal...')
    # print(num_ops(2))
    # print(num_ops(4))
    # print(num_ops(8))
    print(num_ops(1985))
    # print(num_ops(1985))
    # n1 = Node(1, 0)
    # print(n1.val, n1.level)
    # print(type(n1))


if __name__ == '__main__':
    main()
