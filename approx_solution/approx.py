"""
    Approximation Solution for Longest Path Project
    Name:  Jordan Martin
    Date:  11/29/2023  
    References: https://www.geeksforgeeks.org/longest-path-in-a-directed-acyclic-graph-dynamic-programming/
    I used the website above as a reference for my solution, removing most of the code and only changing the
    comparison parts to always take the largest weight.

"""


# import time

def greedyLongestPath():
    global visited, adj, V

    # start_time = time.perf_counter_ns()  # Record start time in nanoseconds

    dist = {v: -float('inf') for v in adj}
    path = {v: [] for v in adj}

    for s in adj:
        dist[s] = 0
        for u in adj:
            # ALWAYS TAKE THE LARGEST WEIGHT
            if dist[u] != -float('inf'):
                for v, w in adj[u]:
                    if dist[v] < dist[u] + w:
                        dist[v] = dist[u] + w
                        path[v] = path[u] + [u]

        max_dist = max(dist.values())

        if max_dist >= 0:
            print(f"Yes, a path exists with distance {max_dist}")
            break
    else:
        print("No path exists.")

    # end_time = time.perf_counter_ns()  # Record end time in nanoseconds
    # elapsed_time = end_time - start_time
    # print(f"Time taken by greedyLongestPath: {elapsed_time} nanoseconds")

    # Print the path taken
    if max_dist >= 0:
        max_dist_vertex = max(dist, key=dist.get)
        path_taken = path[max_dist_vertex] + [max_dist_vertex]
        print("Path taken:", path_taken)


if __name__ == '__main__':
    n, m = map(int, input().split())
    V, visited = n, [False for i in range(n)]
    adj = {chr(ord('a') + i): [] for i in range(n)}

    for _ in range(m):
        u, v, w = input().split()
        adj[u].append([v, int(w)])

    greedyLongestPath()
