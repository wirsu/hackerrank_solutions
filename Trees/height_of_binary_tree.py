from collections import defaultdict

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return -1

    depth_left = height(root.left)
    depth_right = height(root.right)
    depth = max(depth_left, depth_right) + 1
    return depth

def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        from collections import defaultdict

        # This class represents a directed graph using
        # adjacency list representation
        class Graph:
            # Constructor
            def __init__(self):
                self.graph = defaultdict(list)
            def addEdge(self, u, v):
                self.graph[u].append(v)
            def DFSUtil(self, v, visited):
                # Mark the current node as visited
                # and print it
                visited[v] = True
                print(v, end=' ')
                # Recur for all the vertices adjacent to this vertex
                for i in self.graph[v]:
                    if visited[i] == False:
                        self.DFSUtil(i, visited)
                        # The function to do DFS traversal. It uses
            def DFS(self, v):
                # Mark all the vertices as not visited
                visited = [False] * (len(self.graph))
                # Call the recursive helper function to print DFS traversal
                self.DFSUtil(v, visited)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    x = root.left
    x.left = Node(4)
    print("Height of tree:", height(root))

main()