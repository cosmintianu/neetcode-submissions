# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"
        q = deque()
        q.append(root)
        s = []

        while q:
            node = q.popleft()

            if node is None:
                s.append('#')
                continue

            s.append(str(node.val))

            q.append(node.left)
            q.append(node.right)

        return "!".join(s)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("!")
        print(arr)
        if arr[0] == '#':
            return None
        root = TreeNode(int(arr[0]))

        i = 1
        q = deque([root])

        while q:
            node = q.popleft()
            
            if arr[i] != '#':
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i+=1

            if arr[i] != '#':
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i+=1
        return root

        
