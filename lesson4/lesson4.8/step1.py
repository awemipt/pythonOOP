from typing import List, Union

import math


class Vertex:
    def __init__(self):
        self._links = []
        self._linked = []

    @property
    def links(self):
        return self._links

    @property
    def linked(self):
        return self._linked

    pass


class Link:
    def __init__(self, v1: Vertex, v2: Vertex):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
        v1._links.append(self)
        v2._links.append(self)
        v1.linked.append(v2)
        v2.linked.append(v1)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value: Union[int, float]):
        self._dist = value

    pass


class LinkedGraph:
    def __init__(self):
        self._links: List[Link] = []
        self._vertex: List[Vertex] = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        flag = True
        for l in self._links:
            if l.v1 == link.v1 and l.v2 == link.v2 or link.v2 == l.v1 and link.v1 == l.v2:
                flag = False
                break
        if flag:
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)

            self._links.append(link)

    @staticmethod
    def find_min(u, d):
        m = math.inf
        res = 0
        for i, dist in enumerate(d):
            if not u[i] and dist <= m:
                m = dist
                res = i
        return res

    @staticmethod
    def connected(vertex, m):
        for i, d in enumerate(m[vertex]):
            if d > 0:
                yield i

    def find_path(self, start_v, stop_v):
        m = [[0] * len(self._vertex) for _ in range(len(self._vertex))]
        for link in self._links:
            i = self._vertex.index(link.v1)
            j = self._vertex.index(link.v2)
            m[i][j] = link.dist
            m[j][i] = link.dist
        d = [math.inf] * len(self._vertex)
        start_indx = self._vertex.index(start_v)
        stop_indx = self._vertex.index(stop_v)
        d[start_indx] = 0
        u = [False] * len(self._vertex)
        paths = {}
        # print(d)
        while not all(u):
            tmp = self.find_min(u, d)

            u[tmp] = True
            for vertex in self.connected(tmp, m):
                if d[tmp] + m[tmp][vertex] < d[vertex]:
                    d[vertex] = d[tmp] + m[tmp][vertex]
                    paths[vertex] = tmp
        end = stop_indx
        path = []
        while end != start_indx:
            path.append(end)
            end = paths[end]
        path.append(start_indx)
        res1 = list(reversed([self._vertex[i] for i in path]))
        res2 = []
        for i in range(len(res1)-1):
            for link in self._links:
                if link.v1 == res1[i] and link.v2 == res1[i+1] or link.v2 == res1[i] and link.v1 == res1[i+1]:
                    res2.append(link)
                    break
        return res1, res2

class Station(Vertex):
    def __init__(self, name):
        super(Station, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super(LinkMetro, self).__init__(v1, v2)
        self.dist = dist


v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")
map_metro = LinkedGraph()
map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)
print(path)# от сретенского бульвара до китай-город 1
# map_metro.print_m()
# print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7

print([l.v1 for l in v7.links])
