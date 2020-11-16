import heapq
import networkx as nx

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

    G = nx.Graph()

    for e in shortest_edges:
        G.add_edge(e[0], e[1], distance=e[2])

    path = nx.shortest_path(G, start, end, 'distance')

    return (distances[end], path)

# def main():
#     print('thank you for looking after my mama...')
#     print(shortest_path(simple, 'a', 'd'))
#     print(shortest_path(major, 'a', 'b'))
#
#
# if __name__ == '__main__':
#     main()
