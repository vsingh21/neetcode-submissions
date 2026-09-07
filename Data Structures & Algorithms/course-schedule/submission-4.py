class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:set() for i in range(numCourses)}
        for start, end in prerequisites:
            adj[start].add(end)
        print(adj)
        visited = set()
        def dfs(path, i):
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)
            for j in adj[i]:
                if not dfs(path, j):
                    return False
            path.remove(i)
            visited.add(i)
            return True

        for i in range(numCourses):
            if not dfs(set(), i):
                return False
        return True