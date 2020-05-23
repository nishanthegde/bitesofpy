import queue


class Node:

    def __init__(self, val, level):
        self.val = val
        self.level = level


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
    # while not q.empty() and loop_num <= 10:
    while not q.empty():
        # Remove an item from queue
        t = q.get()
        # t = q.popleft()
        # print('val{}'.format(t.val))

        # If the removed item is target number y, return its level
        if (t.val == n):
            return t.level

        # Mark dequeued number as visited
        visit.add(t.val)
        # print(visit)

        # If we can reach n in one more step
        if (t.val * 2 == n or t.val // 3 == n):
            return t.level + 1

        # Insert children of t if not visited already
        if (t.val * 2 not in visit):
            if t.val * 2 not in [q_item.val for q_item in q.queue]:
                # print(10 in [q_item.val for q_item in q.queue])
                q.put(Node(t.val * 2, t.level + 1))
                # print([q_item.val for q_item in q.queue])
        if (t.val // 3 not in visit and t.val // 3 > 0):
            if t.val // 3 not in [q_item.val for q_item in q.queue]:
                q.put(Node(t.val // 3, t.level + 1))
                # print([q_item.val for q_item in q.queue])
        # print('level{}\n'.format(t.level + 1), 'loop{}\n'.format(loop_num))
        loop_num += 1


def main():
    # print('please look after west bengal...')
    # print(num_ops(2))
    # print(num_ops(4))
    # print(num_ops(8))
    print(num_ops(10))
    # print(num_ops(1985))
    # n1 = Node(1, 0)
    # print(n1.val, n1.level)
    # print(type(n1))


if __name__ == '__main__':
    main()
