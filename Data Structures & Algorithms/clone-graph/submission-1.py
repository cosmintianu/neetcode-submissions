"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = [node]

        while q:
            curr = q.pop(0)

            for neigh in curr.neighbors:
                if neigh not in oldToNew:
                    q.append(neigh)
                    oldToNew[neigh] = Node(neigh.val)
                oldToNew[curr].neighbors.append(oldToNew[neigh])

        return oldToNew[node]
        

        return dfs(node) if node else None

