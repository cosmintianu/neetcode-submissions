class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = 0
        in_degrees = [0] * numCourses
        adj = defaultdict(list)
        q = deque()
        
        for course, prereq in prerequisites:
            in_degrees[course] += 1
            adj[prereq].append(course)
        # print(in_degrees) 
        # print(adj)

        for i, c in enumerate(in_degrees):
            if c == 0:
                q.append(i)

        while q:
            prereq = q.popleft()
            res += 1
            for course in adj[prereq]:
                    in_degrees[course] -= 1
                    if in_degrees[course] == 0:
                        q.append(course)

        return res == numCourses