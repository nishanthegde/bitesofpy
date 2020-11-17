import heapq

simple = {
    'a': {'b': 2, 'c': 4, 'e': 1},
    'b': {'a': 2, 'd': 3},
    'c': {'a': 4, 'd': 6},
    'd': {'c': 6, 'b': 3, 'e': 2},
    'e': {'a': 1, 'd': 2}
}

major = {
    'a': {'w': 14, 'x': 7, 'y': 9},
    'b': {'w': 9, 'z': 6},
    'w': {'a': 14, 'b': 9, 'y': 2},
    'x': {'a': 7, 'y': 10, 'z': 15},
    'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
    'z': {'b': 6, 'x': 15, 'y': 11},
}


def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    # Dict with shortest distances from start to all the nodes
    # Initialized to infinity for all other vertices and 0 for start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Initialize priority queue
    pq = [(0, start)]
    # Initialize list to store shortest edges
    shortest_edges = []

    while len(pq) > 0:
        # While there is something in the priority queue keep doing
        current_distance, current_vertex = heapq.heappop(pq)

        # If current  distance in queue is greater than shortest distances skip
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                shortest_edges.append((current_vertex, neighbor, weight))
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    d = []
    get_paths(start, end, shortest_edges, 0, distances[end], d)
    path = [end] + d

    return distances[end], path[::-1]


def get_paths(start, end, l, cost, total_cost, path):
    for j in [x for x in l if x[1] == end]:
        cost_to_next = cost + j[2]
        if cost_to_next <= total_cost:
            cost += j[2]
            # print(j[0], cost)
            path.append(j[0])
            get_paths(start, j[0], l, cost, total_cost, path)


# def main():
#     print('thank you for looking after my mama...')
#     print(shortest_path(simple, 'a', 'd'))
#     print(shortest_path(major, 'a', 'b'))
#
#
# if __name__ == '__main__':
#     main()
