import heapq

simple = {
    'a': {'b': 2, 'c': 4, 'e': 1},
    'b': {'a': 2, 'd': 3},
    'c': {'a': 4, 'd': 6},
    'd': {'c': 6, 'b': 3, 'e': 2},
    'e': {'a': 1, 'd': 2}
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

    pq = [(0, start)]

    # While there is something in the priority queue keep doing
    # while len(pq) > 0:
    current_distance, current_vertex = heapq.heappop(pq)
    #     if current_distance > distances[current_vertex]:
    #         continue

    for neighbor, weight in graph[current_vertex].items():
        distance = current_distance + weight
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))
    
    print(pq)

    current_distance, current_vertex = heapq.heappop(pq)
    print(current_distance, current_vertex)
    
    return distances


def main():
    print('thank you for looking after my mama...')
    print(shortest_path(simple, 'a', 'd'))


if __name__ == '__main__':
    main()
