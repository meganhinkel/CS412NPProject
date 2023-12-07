"""
    Exact Solution for Longest Path Project
    Name:  Megan Hinkel 
    Date:  11/29/2023  
    References: https://www.geeksforgeeks.org/longest-path-in-a-directed-acyclic-graph-dynamic-programming/
    I used the website above as a reference for my solution, changing it to match the input of our
    problem and to calculate the longest path based on weights (rather than number of edges).

"""


def dfs(node, graph, dp, vis, path): 
    # Convert node to corresponding integer index
    currNodeIndex = ord(node) - 96
    # Mark as visited
    vis[currNodeIndex] = True

    # Traverse for all its children 
    if node in graph:
        for key in graph[node].keys():
            childNodeIndex = ord(key) - 96
            if not vis[childNodeIndex]:
                dfs(key, graph, dp, vis, path)

            # Store the max of the paths
            if graph[node][key] + dp[childNodeIndex] > dp[currNodeIndex]:
                dp[currNodeIndex] = graph[node][key] + dp[childNodeIndex]
                path[currNodeIndex] = path[childNodeIndex] + [key]


# Function that returns the longest path 
def findLongestPath(graph, n): 
    # Dp array 
    dp = [0] * (n + 1) 

    # Visited array to know if the node has been visited previously or not 
    vis = [False] * (n + 1)

    # Path array to store the longest path for each node
    path = [[] for _ in range(n + 1)]

    # Call DFS for every unvisited vertex 
    for key in graph.keys():  
        if not vis[ord(key) - 96]: 
            dfs(key, graph, dp, vis, path)

    # Traverse and find the maximum of all dp[i] 
    longestLength = 0
    for i in range(1, n + 1):  
        longestLength = max(longestLength, dp[i]) 
      
    # Reverse (backtrack) path
    path[dp.index(longestLength)].append(chr(dp.index(longestLength) + 96))
    longestPath = list(reversed(path[dp.index(longestLength)]))

    return longestLength, longestPath


def main():
    numVertices, numEdges = [int(x) for x in input().split()]
    graph = {}

    for i in range(numEdges):
        u, v, w = [x for x in input().split()]
        w = int(w)
        if u not in graph:
            graph[u] = { v: w }
        else:
            graph.get(u)[v] = w

    longestLength, longestPath = findLongestPath(graph, numVertices)
    print(longestLength)
    print(*longestPath)
    pass


if __name__ == "__main__":
    main()