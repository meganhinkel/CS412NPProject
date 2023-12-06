"""
    Exact Solution for Longest Path Project
    name:  Megan Hinkel 
    date:  11/29/2023  

"""


def dfs(node, graph, dp, vis): 
    # Mark as visited (Convert node to corresponding integer index)
    vis[ord(node) - 97] = True

    # Traverse for all its children 
    for key in graph[node].keys():
        if not vis[ord(key) - 97]:
            dfs(key, graph, dp, vis)


# Function that returns the longest path 
def findLongestPath(graph, n): 
    # Dp array 
    dp = [0] * (n + 1) 
    # Visited array to know if the node has been visited previously or not 
    vis = [False] * (n + 1)
    # Start at first node
    dfs(list(graph.keys())[0], graph, dp, vis)



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

    print(graph)
    findLongestPath(graph, numVertices)

    pass

if __name__ == "__main__":
    main()