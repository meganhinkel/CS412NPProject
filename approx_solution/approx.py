def greedyLongestPath():
    global visited, adj, V

    dist = {v: -float('inf') for v in adj}


    for s in adj:

        dist[s] = 0

        for u in adj:
            # ALWAYS TAKE THE LARGEST WEIGHT
            if dist[u] != -float('inf'):
                for v, w in adj[u]:
                    if dist[v] < dist[u] + w:
                        dist[v] = dist[u] + w

        max_dist = max(dist.values())

        if max_dist >= 0:
            print(f"Yes, a path exists with distance {max_dist}")
            break
    else:

        print("No path exists.")


def main():
    n, m = map(int, input().split())
    V, visited = n, [False for i in range(n)]
    adj = {chr(ord('a') + i): [] for i in range(n)}

    for _ in range(m):
        u, v, w = input().split()
        adj[u].append([v, int(w)])

    greedyLongestPath()


if __name__ == '__main__':
    main()
