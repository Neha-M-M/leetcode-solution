from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        # Step 1: Build graph + indegree
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 2: Queue for courses with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process courses
        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses processed
        return count == numCourses