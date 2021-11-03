def Dijkstra(network, start, end, mat):
    path = []
    n = len(network)
    fmax = 999
    s = mat.index(start) + 1
    d = mat.index(end) + 1
    w = [[0 for i in range(n)] for j in range(n)]
    book = [0 for i in range(n)]
    dis = [fmax for i in range(n)]
    book[s - 1] = 1
    midpath = [-1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if network[i][j] != 0:
                w[i][j] = network[i][j]
            else:
                w[i][j] = fmax
            if i == s - 1 and network[i][j] != 0:
                dis[j] = network[i][j]
    for i in range(n - 1):
        min = fmax
        for j in range(n):
            if book[j] == 0 and dis[j] < min:
                min = dis[j]
                u = j
        book[u] = 1
        for v in range(n):
            if dis[v] > dis[u] + w[u][v]:
                dis[v] = dis[u] + w[u][v]
                midpath[v] = u + 1
    j = d - 1
    path.append(mat[d - 1])
    while (midpath[j] != -1):
        path.append(mat[midpath[j] - 1])
        j = midpath[j] - 1
    path.append(mat[s - 1])
    path.reverse()
    print(path)


def readfile_weight():
    try:
        with open(r'C:\Users\蒋明峰\Desktop\weight.txt', 'r') as f:
            line = f.readlines()
            l = []
            for w in line:
                str = w.rstrip('\n').split(',')
                l.append(str)

    except:
        print('invalid file')
        exit(0)
    mat = []
    for i in l:
        temp = []
        for j in i:
            temp.append(int(j))
        mat.append(temp)
    return mat


network = readfile_weight()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
Dijkstra(network, 'A', 'F', vertices)
