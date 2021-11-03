temp1 = dict()
temp = dict()

def make_set(point):
    temp1[point] = point
    temp[point] = 0
def find(point):
    if temp1[point] != point:
        temp1[point] = find(temp1[point])
    return temp1[point]
def merge(point1, point2):
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if temp[r1] > temp[r2]:
            temp1[r2] = r1
        else:
            temp1[r1] = r2
            if temp[r1] == temp[r2]:
                temp[r2] += 1
def kruskal(vertices,edges):

    for vertice in vertices:
        make_set(vertice)
    minu_tree = []
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            merge(vertice1, vertice2)
            minu_tree.append(edge)
    return minu_tree
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges = [[10, 'A', 'B'],
            [7, 'A', 'D'],
            [12, 'B', 'C'],
            [7, 'B', 'E'],
            [4, 'C', 'E'],
            [10, 'C', 'F'],
            [8, 'D', 'E'],
            [7, 'D', 'G'],
            [10, 'E', 'F'],
            [5, 'E', 'H'],
            [8, 'F', 'I'],
            [22, 'G', 'H'],
            [6, 'H', 'I'],
            ]
print(kruskal(vertices,edges))
