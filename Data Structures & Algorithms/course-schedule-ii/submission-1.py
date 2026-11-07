class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            in_degrees[course] += 1
            adj[prereq].append(course)

        q = deque()

        for i, prereq_nr in enumerate(in_degrees):
            if prereq_nr == 0:
                q.append(i)

        res = []
        
        while q:
            prereq = q.popleft()
            res.append(prereq)

            for course in adj[prereq]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    q.append(course)

        return res if len(res) == numCourses else []