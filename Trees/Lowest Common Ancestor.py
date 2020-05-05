class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def lca(root, v1, v2):
    if v1 > v2:
        v_big, v_small = v1, v2
    else:
        v_big, v_small = v2, v1

    current = root
    while True:
        if current.info > v_big:
            current = current.left
        elif current.info < v_small:
            current = current.right
        elif current.info >= v_small and current.info <= v_big:
            return current