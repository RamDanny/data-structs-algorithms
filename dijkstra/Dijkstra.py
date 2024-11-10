#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:

    def Dijkstra_alg(self, n, e, mat, s):
        INF = 9999
        d, usp, visited = [], [], []
        for i in range(n):
            d.append(INF)
            usp.append(None)
            visited.append(False)
        d[s-1], usp[s-1] = 0, 1
        for loop in range(n):
            # find the elt with smallest dist
            minelt, minval = -1, INF
            for i in range(n):
                if d[i] < minval and not visited[i]:
                    minelt = i
                    minval = d[i]
            visited[minelt] = True
            # relax all its neighbours
            for i in range(e):
                u, v, w = mat[i]
                if u == minelt+1 and not visited[v-1]:
                    if d[u-1] + w < d[v-1]:
                        d[v-1] = d[u-1] + w
                        usp[v-1] = 1
                    elif d[u-1] + w == d[v-1]:
                        usp[v-1] = 0
                elif v == minelt+1 and not visited[u-1]:
                    if d[v-1] + w < d[u-1]:
                        d[u-1] = d[v-1] + w
                        usp[u-1] = 1
                    elif d[v-1] + w == d[u-1]:
                        usp[u-1] = 0
        # compute paths
        ans = []
        for i in range(n):
            ans.append([d[i], usp[i]])
        return ans

