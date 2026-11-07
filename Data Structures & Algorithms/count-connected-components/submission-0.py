class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0 

        visited = set()

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            nonlocal res
            if node in visited:
                # res += 1
                return

            visited.add(node)
            for neigh in adj[node]:
                dfs(neigh)


        for n in range(n):
            if n not in visited:
                dfs(n)
                res +=1

        return res

            