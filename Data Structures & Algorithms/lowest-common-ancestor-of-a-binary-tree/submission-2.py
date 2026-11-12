# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # parent of a is mp[a]
        mp = {root: None}

        qu = deque([root])

        while qu:
            node = qu.popleft()
 
            if node.left:
                qu.append(node.left)
                mp[node.left] = node
            if node.right:
                qu.append(node.right)
                mp[node.right] = node

        ancestors = set()
        while p:
            ancestors.add(p)
            print(f"{p.val} {mp[p].val if mp[p] else ""}")
            p = mp[p]


        while q not in ancestors:
            q = mp[q]

        return q










