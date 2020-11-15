import heapq
import networkx as nx

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

        """simple = {
            'a': {'b': 2, 'c': 4, 'e': 1},
            'b': {'a': 2, 'd': 3},
            'c': {'a': 4, 'd': 6},
            'd': {'c': 6, 'b': 3, 'e': 2},
            'e': {'a': 1, 'd': 2}
        }"""

    print(shortest_edges)

    G = nx.Graph()

    for e in shortest_edges:
        G.add_edge(e[0], e[1], weight=e[2])

    for path in nx.all_simple_paths(G, source=start, target=end):
        print(path)

    return distances


def trace_path(shortest_edges: list, current_vertex: str, start: str, distance_covered: int,
               shortest_distance: int) -> tuple():
    previous_vertex = [v for v in shortest_edges if v[0] == current_vertex][0][1]
    distance_previous = [v for v in shortest_edges if v[0] == current_vertex][0][2]
    distance_covered += distance_previous

    print(previous_vertex, distance_covered, shortest_distance)

    if distance_covered <= shortest_distance:
        trace_path(shortest_edges, previous_vertex, start, distance_covered, shortest_distance)

    print(previous_vertex, distance_previous, distance_covered)


def main():
    print('thank you for looking after my mama...')
    print(shortest_path(simple, 'a', 'd'))
    print(shortest_path(major, 'a', 'b'))


if __name__ == '__main__':
    main()
