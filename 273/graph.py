import heapq

simple = {
    'a': {'b': 2, 'c': 4, 'e': 1},
    'b': {'a': 2, 'd': 3},
    'c': {'a': 4, 'd': 6},
    'd': {'c': 6, 'b': 3, 'e': 2},
    'e': {'a': 1, 'd': 2}
}


def shortest_path(graph: dict, start: str, end: str) -> tuple():
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    distance = 0
    explored = []

    queue = [[start]]
    # heapq.heapify(queue)

    if start == end:
        return (distance, explored)

    while queue:
        path = queue.pop(0)
        # print(path)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    print("Shortest path = ", new_path)
                    for p in list(zip(new_path, new_path[1:])):
                        n = graph[p[0]]
                        print(n)
                        distance += n[p[1]]
                    return (distance, new_path)

            explored.append(node)


def main():
    print('thank you for looking after my mama...')
    print(shortest_path(simple, 'a', 'd'))


if __name__ == '__main__':
    main()
