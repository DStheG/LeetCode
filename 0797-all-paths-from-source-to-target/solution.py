class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ret = []
        visit = [False] * len(graph)
        def travle(i, path):
            if (visit[i]):
                return
            if (i == len(graph) - 1):
                ret.append(path + [i])
                return
            visit[i] = True
            for j in graph[i]:
                travle(j, path + [i])
            visit[i] = False
        travle(0, [])
        return ret