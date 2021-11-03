import re
import tkinter as tk
from tkinter import messagebox

route = ['鼋头渚', '三国城', '水浒城', '太湖', '荡口古镇', '惠山古镇', '灵山大佛', '拈花湾', '蠡园']
guide_route = ['鼋头渚', '三国城', '水浒城', '太湖', '荡口古镇']

#  读取文件中的邻接矩阵
route_file = 'weight.txt'
guide_route_file = 'guide_route.txt'


def readfile_weight(file):
    try:
        with open(file, 'r', encoding='UTF-8') as f:
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


# 通过邻接矩阵生成邻接表
def graph_create(mat, route):
    graph = {}

    for i in range(len(route)):
        val = []
        for num in range(len(mat[i])):
            if mat[i][num] != 0:
                val.append(route[num])
                # print(route[num])
        graph[route[i]] = val
    return graph


# 通过邻接矩阵生成所有的路径
def edge_create(mat, route):
    edge = []
    for i in range(len(route)):
        for num in range(i + 1):
            if mat[i][num] != 0:
                ele = []
                ele.append(mat[i][num])
                ele.append(route[num])
                ele.append(route[i])
                edge.append(ele)
    return edge


#  邻接矩阵
network = readfile_weight(route_file)
guide_network = readfile_weight(guide_route_file)

#
# for i in guide_network:
#     print(i)
################################################
#  删除元素
# def delete(line, spot, mat):
#     if spot in line:
#         count = line.index(spot)
#         line.remove(spot)
#         # mat.pop(count)
#         mat[count] = [0,0,0,0,0,0,0,0,0]
#         for i in mat:
#             i[count] = 0
#     # else:
#     print('invalid input')
# delete_route.extend(route)
# delete_network.extend(mat)
# print(delete_route)
# print(delete_network)

#
# def delete_all(route, spot, mat):
# delete(delete_route, '太湖', delete_network)
# #     if spot in guide_route:
# #         delete(guide_route, spot, guide_network)
#
# print(delete_network)
# print(delete_route)
# print(route)
#
# spot = input()
# delete_all(route, spot, network)
# print(route)
# for i in guide_network:
#     print(i)

#  添加元素
################################################
#  邻接表
graph_route = graph_create(network, route)
# print(graph_route)
graph_guide_route = graph_create(guide_network, guide_route)
# print(graph)
edges = edge_create(network, route)


# print(edges)


################################################
#  找到两点之间的所有路径
def findAllPath(graph, start, end):
    path = []
    stack = []
    stack.append(start)
    visited = set()
    visited.add(start)
    seen_path = {}
    while (len(stack) > 0):
        start = stack[-1]
        nodes = graph[start]
        if start not in seen_path.keys():
            seen_path[start] = []
        g = 0
        for w in nodes:
            if w not in visited and w not in seen_path[start]:
                g = g + 1
                stack.append(w)
                visited.add(w)
                seen_path[start].append(w)
                if w == end:
                    path.append(list(stack))
                    old_pop = stack.pop()
                    visited.remove(old_pop)
                break
        if g == 0:
            old_pop = stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    return path


# path = findAllPath(graph, start='周立', end='周立5')
# path = findAllPath(graph, start='A', end='F')
# print(path)
# print('输入起点：')
# start = input()
# print('输入终点：')
# end = input()
# path = findAllPath(graph, start, end)
# path = findAllPath(graph, 'A', 'I')
# print(path)

################################################
#  判断两条路之间有无相同的景点
def jdg_same(a, b):
    a = set(a)
    b = set(b)
    for i in a:
        if i in b:
            return 0
            break
    return 1


#  寻找两点之间的所有回路
def find_loop(graph, start, end):
    loop = []
    temp = []
    path = []
    seen = set()
    seen.add(start)
    path = findAllPath(graph, start, end)
    flag = 0
    # print(len(path))
    for i in range(len(path)):
        for j in range(len(path)):
            temp = path[i][0:-1] + path[j][::-1]
            # print(temp)
            res = jdg_same(path[i][1:-1], path[j][1:-1])
            # print(res)
            if res == 1 and len(temp) > 3:
                # print('true')
                # path[i].pop()
                # print(path[i])
                return temp
                # flag = 1
                # return flag
                # # loop.append(path)
        #         # break
        # if flag == 1:
        #     break

        # else:
        # print('false')
    if flag == 0:
        # print("there's no loop exist")
        # return loop
        pass


#
# start = 'A'
# end = 'F'
# flag = find_loop(graph, start, end)


# print(flag)


################################################
#  寻找所有的回路
def all_loop(route):
    count = 0
    temp = []
    for i in route:
        for j in route[1:]:
            temp.append(find_loop(graph_guide_route, i, j))
    #         print(flag)
    #         if flag == 0:
    #             count = count + 1
    #         break
    # if count == len(route):
    #     return None
    return temp[8]


all_loop(guide_route)


################################################
#  深度优先搜索
def DFS(graph, s):
    stack = []
    stack.append(s)
    v = set()
    v.add(s)
    path = []
    dfs = []
    flag = 0
    # try:
    while len(stack) > 0:
        flag = 0
        vertex = stack[-1]
        nodes = graph[vertex]
        for w in nodes:
            if w not in v:
                stack.append(w)
                v.add(w)
                flag = 1
                    # print(w, end=' ')
                print(vertex + '->' + w)
                path.append(vertex)
                path.append(w)

                break
        if flag == 0:
            stack.pop()
    return path
    # except:
    #     pass



# dfs_path = DFS(graph_route, "惠山古镇")

# print(dfs_path)


################################################
#  寻找最短路径
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
    # for i in path[:-1]:
    #     print(i, end='->')
    # print((path[-1]))
    # print(path)
    return path


# shortest_path = Dijkstra(network, '鼋头渚', '拈花湾', route)
# print(shortest_path)
################################################
#  最小代价生成树
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


def kruskal(vertices, edges):
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


# plan = kruskal(route, edges)

# print(plan)
################################################
# 图形界面
class spotpage():
    def __init__(self):

        self.window = tk.Tk()
        # window = tk.Tk()
        self.window.title('景区管理系统')
        self.window.geometry('1300x800')
        # self.canvas = tk.Canvas(self.window, height=800, width=1600)
        self.image_file = tk.PhotoImage(file='qiuqiu.png')
        self.spot_num = -1
        self.dfsenter = tk.Entry(self.window, show=None)
        self.shortestentry = tk.Entry(self.window, show=None)
        self.spotlist = []
        self.flag1 = 0
        self.flag2 = 0
        for i in route:
            self.add_spot(i)

#  获取景点坐标
    def get_coor(self):
        # print(self.spot_num)
        # global spot_num
        space = 50
        distance = 200
        self.spot_num += 1
        if self.spot_num == 0:
            return space, space
        elif self.spot_num == 1:
            return distance + space, space
        elif self.spot_num == 2:
            return 2 * distance + space, space
        elif self.spot_num == 3:
            return space, distance + space
        elif self.spot_num == 4:
            return distance + space, distance + space
        elif self.spot_num == 5:
            return 2 * distance + space, distance + space
        elif self.spot_num == 6:
            return space, 2 * distance + space
        elif self.spot_num == 7:
            return distance + space, 2 * distance + space
        elif self.spot_num == 8:
            return 2 * distance + space, 2 * distance + space

#  删除景点及其坐标
    def delete_spotlist(self, spot):
        # print(self.spotlist)
        for i in self.spotlist:

            for j in i:
                if j == spot:
                    count = self.spotlist.index(i)
                    # print(count)
                    self.spotlist.pop(count)
                    route.pop(count)
                    network.pop(count)
                    for num in network:
                        num.pop(count)

        # print(self.spotlist)

        self.spot_num = self.spot_num - 1
        self.spot()

#  添加景点及其坐标
    def insert_spotlist(self, spot, weight, near):
        # print(self.spotlist)
        self.spot_num = self.spot_num + 1
        count = route.index(near)
        route.append(spot)
        for i in range(len(network)):
            if i == count:
                network[i].append(int(weight))
            else:
                network[i].append(0)
        temp = []
        for i in range(10):
            temp.append(0)
        temp[count] = int(weight)
        network.append(temp)
        print(network)
        print(route)

        # self.spot()

    def add_spot(self, name):
        spot = {}
        spot[name] = self.get_coor()
        self.spotlist.append(spot)

        # print(self.spotlist)

        # print(network)
#  画出旅游景点图
    def spot(self):
        # self.spot_num += 1
        # print(self.spot_num)
        self.canvas = tk.Canvas(self.window, height=800, width=600)
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tomato',
                                                   width=10, tags='line')
        for spot in self.spotlist:
            for n in spot:
                # print(n)
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file, tags=n)
                # self.canvas.create_text(spot[n][0]+50, spot[n][1]+50, text = chr(route.index(n)+65),font = ('楷体',20))
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17), tags=n)
#  删除景点
    def delete(self):
        delete_spot = Delete_spot()
        self.window.wait_window(delete_spot)
        if delete_spot.valid == 0:
            return
        self.var = delete_spot.var_delete.get()
        self.delete_spotlist(self.var)
        self.canvas.destroy()
        self.spot_num -= 1
        self.spot()
        self.display()

        # print(delete_network)

#  添加景点
    def insert(self):
        insert_spot = Insert_spot()
        self.window.wait_window(insert_spot)
        print(insert_spot.valid)
        if insert_spot.valid == 0:
            return
        self.var = insert_spot.var_insert.get()
        result = re.search(re.compile('(.*?)/(\d+)/(.*)'), self.var)
        self.insert_spotlist(result[1], result[2], result[3])
        for i in self.spotlist:
            for j in i:
                if j == result[3]:
                    x = i[j][0]
                    y = i[j][1]
        line = self.canvas.create_line(x + 50 , y + 50, x + 50, y + 250, fill='Tomato', width=10)
        self.canvas.create_image(x, y , anchor='nw', image=self.image_file)
        self.canvas.create_text(x+50, y + 50, text=result[3], font=('楷体', 17))
        self.canvas.create_image(x, y + 200, anchor='nw', image=self.image_file)
        self.spotlist.append({result[1]:[x, y + 200]})
        self.canvas.create_text(x+50, y + 250, text=result[1], font=('楷体', 17))


        # self.spot_num += 1
        # self.spot()
        # self.display()

        # print(delete_network)

#  深度遍历路径
    def insert_dfs(self):
        messagebox = Messagebox()
        self.window.wait_window(messagebox)
        if messagebox.valid == 0:
            return
        self.var = messagebox.var_dfsenter.get()
        # if self.var not in route:
        #         tk.messagebox.showerror(title='error input', message='请输入正确的景点名字')
        #         # self.flag1 = 0
        # else:
        graph_route = graph_create(network, route)
        self.dfs_path = DFS(graph_route, self.var)
        self.show_dfsline()
        # self.flag1 = 1

    def insert_shortest(self):
        messagebox_shortest = Messagebox_shortest()
        self.window.wait_window(messagebox_shortest)
        if messagebox_shortest.valid == 0:
            return
        self.var = messagebox_shortest.var_shortestenter.get()

        result = re.search(re.compile('(.*?)/(.*)'), self.var)
        # if result == None or result[1] not in route or result[2] not in route:
        #     tk.messagebox.showerror(title='error input', message='请输入正确的景点名字')
        # self.flag2 = 0
        # else:
        #     # start = var
        #     self.dfs_path = DFS(graph_route, self.var)
        #     tk.messagebox.showinfo(title='correct input', message='成功输入')
        #
        # else:
        self.shortest_path = Dijkstra(network, result[1], result[2], route)
        self.show_shortestline()
        # tk.messagebox.showinfo(title='correct input', message='成功输入')
        # self.flag2 = 1
#  导游路线
    def guide_route(self):
        route_line = Route_line()
        route_line.display()
        self.window.wait_window(route_line)
        # route_line.mainloop()
        if route_line.valid == 0:
            return
#  最短路线
    def show_shortestline(self):
        # if self.flag2 == 0:
        #     tk.messagebox.showerror(title='blank', message='请输入起点/终点')
        # else:
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tomato',
                                                   width=10)

        path = []

        for i in self.shortest_path:
            path.append(route.index(i))
            # print(path)
        for i in range(len(path) - 1):
            # if network[i][j] != 0:
            i_coor = []
            for n in self.spotlist[path[i]]:
                i_coor.append(self.spotlist[path[i]][n][0])
                i_coor.append(self.spotlist[path[i]][n][1])
                # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
            j_coor = []
            for n in self.spotlist[path[i + 1]]:
                j_coor.append(self.spotlist[path[i + 1]][n][0])
                j_coor.append(self.spotlist[path[i + 1]][n][1])

                # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
            line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50, fill='Navy',
                                           width=10)

        for spot in self.spotlist:
            for n in spot:
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file)
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17))
#  道路建设建议路线
    def show_buildline(self):
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tomato',
                                                   width=10)

        path = []

        edges = edge_create(network, route)
        plan = kruskal(route, edges)
        for i in plan:
            path.append(route.index(i[1]))
            path.append(route.index(i[2]))
            # print(path)
        for i in range(0, len(path) - 1, 2):
            # if network[i][j] != 0:
            i_coor = []
            for n in self.spotlist[path[i]]:
                i_coor.append(self.spotlist[path[i]][n][0])
                i_coor.append(self.spotlist[path[i]][n][1])
                # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
            j_coor = []
            for n in self.spotlist[path[i + 1]]:
                j_coor.append(self.spotlist[path[i + 1]][n][0])
                j_coor.append(self.spotlist[path[i + 1]][n][1])

                # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
            line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                           fill='Indigo',
                                           width=10)

        for spot in self.spotlist:
            for n in spot:
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file)
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17))

    def show_dfsline(self):
        # if self.flag1 == 0:
        #     tk.messagebox.showerror(title='blank', message='请输入起点')
        # else:
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tomato',
                                                   width=10)

        path = []
        for i in self.dfs_path:
            # print(route)
            if i in route:
                path.append(route.index(i))
            # print(path)
        for i in range(0, len(path) - 1, 2):
            # if network[i][j] != 0:
            i_coor = []
            for n in self.spotlist[path[i]]:
                i_coor.append(self.spotlist[path[i]][n][0])
                i_coor.append(self.spotlist[path[i]][n][1])
                # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
            j_coor = []
            for n in self.spotlist[path[i + 1]]:
                j_coor.append(self.spotlist[path[i + 1]][n][0])
                j_coor.append(self.spotlist[path[i + 1]][n][1])

                # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
            line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                           fill='Maroon',
                                           width=10)

        for spot in self.spotlist:
            for n in spot:
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file)
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17))
#  界面展示
    def display(self):
        self.button_dfsline = tk.Button(self.window, text='导游线路策略', width=20, height=2, font=('楷体', 15),
                                        command=self.insert_dfs).place(x=650, y=230)
        self.button_buildline = tk.Button(self.window, text='道路建设建议路线', width=20, height=2, font=('楷体', 15),
                                          command=self.show_buildline).place(x=650, y=330)
        self.button_shortestline = tk.Button(self.window, text='最短路径', width=20, height=2, font=('楷体', 15),
                                             command=self.insert_shortest).place(x=950, y=230)
        # self.label_dfs = tk.Label(self.window, text = '请输入导游路线的起点:', font=('楷体', 15)).place(x=570,y=65)
        self.label_title = tk.Label(self.window, text='欢迎来到\n\n景区旅游信息系统', font=('楷体', 30)).place(x=750, y=50)
        self.get_coor()
        # self.add_spot()
        self.spot()
        self.canvas.place(x=0, y=0)
        # self.shortestentry.place(x=800,y=430,width = 145, height = 45)
        # self.dfsenter.place(x=800,y=55,width = 150, height = 45)
        self.button_route = tk.Button(self.window, text="导游线路图", width=20, height=2, font=('楷体', 15),
                                      command=self.guide_route).place(x=950, y=330)
        # self.button_insert = tk.Button(self.window,text="输入起点/终点",width=20,height=1,font=('楷体', 15),command=self.insert_shortest).place(x=980,y=435)
        self.button_route = tk.Button(self.window, text="删除景点", width=20, height=2, font=('楷体', 15),
                                      command=self.delete).place(x=950, y=430)
        self.button_route = tk.Button(self.window, text="增加景点", width=20, height=2, font=('楷体', 15),
                                      command=self.insert).place(x=650, y=430)


class Messagebox(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('输入起点')
        self.geometry('500x300')
        self.valid = 0

        self.var_dfsenter = tk.StringVar()

        self.dfsenter = tk.Entry(self, textvariable=self.var_dfsenter, show=None)

        self.label_dfs = tk.Label(self, text='请输入导游路线的起点:', font=('楷体', 15)).place(x=140, y=65)
        self.dfsenter.place(x=140, y=125, width=230, height=25)
        self.button_insert = tk.Button(self, text="确认", width=6, height=1, font=('楷体', 15),
                                       command=self.submit).place(x=100, y=230)
        self.button_insert = tk.Button(self, text="取消", width=6, height=1, font=('楷体', 15),
                                       command=self.destroy).place(x=300, y=230)

    def submit(self):
        if self.var_dfsenter.get() not in route:
            tk.messagebox.showerror(title='error input', message='请输入正确的景点名字')
            self.lift()
            # self.flag1 = 0
        else:
            self.valid = 1
            # self.dfs_path = DFS(graph_route, self.var)
            # self.show_dfsline()
            self.destroy()


class Messagebox_shortest(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('输入起点/终点')
        self.geometry('550x350')
        self.valid = 0

        self.var_shortestenter = tk.StringVar()

        self.shortestenter = tk.Entry(self, textvariable=self.var_shortestenter, show=None)

        self.label_shortest = tk.Label(self, text='请输入导游路线的起点/终点(起点和终点间用/分割):', font=('楷体', 15)).place(x=30, y=65)
        self.shortestenter.place(x=130, y=125, width=250, height=30)
        self.button_insert = tk.Button(self, text="确认", width=6, height=1, font=('楷体', 15),
                                       command=self.submit).place(x=130, y=270)
        self.button_insert = tk.Button(self, text="取消", width=6, height=1, font=('楷体', 15),
                                       command=self.destroy).place(x=330, y=270)

    def submit(self):
        self.var = self.var_shortestenter.get()
        result = re.search(re.compile('(.*?)/(.*)'), self.var)
        if result == None or result[1] not in route or result[2] not in route:
            tk.messagebox.showerror(title='error input', message='请输入正确的景点名字')
            self.lift()

            # self.flag1 = 0
        else:
            # self.dfs_path = DFS(graph_route, self.var)
            # self.show_dfsline()
            self.valid = 1
            self.destroy()


class Route_line(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.spot_num = -1
        self.title('导游路线')
        self.geometry('1000x500')
        self.valid = 0
        self.canvas = tk.Canvas(self, height=500, width=1000)
        self.image_file = tk.PhotoImage(file='qiuqiu2.png')
        self.spotlist = []
        for i in guide_route:
            self.add_spot(i)
        # self.var_shortestenter=tk.StringVar()
        # self.shortestenter = tk.Entry(self, textvariable=self.var_shortestenter,show=None)

        self.button_insert = tk.Button(self, text="返回", width=20, height=2, font=('楷体', 15),
                                       command=self.submit).place(x=700, y=250)
        self.button_insert = tk.Button(self, text="显示回路", width=20, height=2, font=('楷体', 15),
                                       command=self.showloop).place(x=700, y=100)

    def get_coor(self):
        # print(self.spot_num)
        # global spot_num
        space = 50
        distance = 200
        self.spot_num += 1
        if self.spot_num == 0:
            return space, space
        elif self.spot_num == 1:
            return distance + space, space
        elif self.spot_num == 2:
            return 2 * distance + space, space
        elif self.spot_num == 3:
            return space, distance + space
        elif self.spot_num == 4:
            return distance + space, distance + space
        elif self.spot_num == 5:
            return 2 * distance + space, distance + space

    def add_spot(self, name):
        spot = {}
        spot[name] = self.get_coor()
        self.spotlist.append(spot)
        self.canvas.place(x=0, y=0)

    def spot(self):
        # self.spot_num += 1
        # print(self.spot_num)
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if guide_network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tan',
                                                   width=10)
        for spot in self.spotlist:
            for n in spot:
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file)
                # self.canvas.create_text(spot[n][0]+50, spot[n][1]+50, text = chr(route.index(n)+65),font = ('楷体',20))
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17))

    def submit(self):
        self.valid = 1
        # self.dfs_path = DFS(graph_route, self.var)
        # self.show_dfsline()
        self.destroy()

    # def showloop(self):
    def display(self):
        self.get_coor()
        # self.add_spot()
        self.spot()

    def showloop(self):
        for i in range(self.spot_num):
            for j in range(self.spot_num):
                if guide_network[i][j] != 0:
                    i_coor = []
                    for n in self.spotlist[i]:
                        i_coor.append(self.spotlist[i][n][0])
                        i_coor.append(self.spotlist[i][n][1])
                        # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
                    j_coor = []
                    for n in self.spotlist[j]:
                        j_coor.append(self.spotlist[j][n][0])
                        j_coor.append(self.spotlist[j][n][1])

                        # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
                    line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                                   fill='Tan',
                                                   width=10)

        path = []
        for i in all_loop(guide_route):
            path.append(guide_route.index(i))
            # print(path)
        for i in range(len(path) - 1):
            # if network[i][j] != 0:
            i_coor = []
            for n in self.spotlist[path[i]]:
                i_coor.append(self.spotlist[path[i]][n][0])
                i_coor.append(self.spotlist[path[i]][n][1])
                # i_coor=[self.spotlist[i][n][0],self.spotlist[i][n][1]]
            j_coor = []
            for n in self.spotlist[path[i + 1]]:
                j_coor.append(self.spotlist[path[i + 1]][n][0])
                j_coor.append(self.spotlist[path[i + 1]][n][1])

                # j_coor=[self.spotlist[j][n][0],self.spotlist[j][n][1]]
            line = self.canvas.create_line(i_coor[0] + 50, i_coor[1] + 50, j_coor[0] + 50, j_coor[1] + 50,
                                           fill='DarkSlateGray',
                                           width=10)

        for spot in self.spotlist:
            for n in spot:
                self.canvas.create_image(spot[n][0], spot[n][1], anchor='nw', image=self.image_file)
                self.canvas.create_text(spot[n][0] + 50, spot[n][1] + 50, text=n, font=('楷体', 17))


class Delete_spot(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Delete')
        self.geometry('500x300')
        self.valid = 0

        self.var_delete = tk.StringVar()

        self.delete = tk.Entry(self, textvariable=self.var_delete, show=None)

        self.label_dfs = tk.Label(self, text='请输入要删除的景点:', font=('楷体', 15)).place(x=130, y=65)
        self.delete.place(x=130, y=105, width=230, height=25)
        self.button_insert = tk.Button(self, text="确认", width=6, height=1, font=('楷体', 15),
                                       command=self.submit).place(x=100, y=230)
        self.button_insert = tk.Button(self, text="取消", width=6, height=1, font=('楷体', 15),
                                       command=self.destroy).place(x=300, y=230)

    def submit(self):
        self.valid = 1
        if self.var_delete.get() not in route:
            tk.messagebox.showerror(title='error input', message='请输入正确的景点名字')
            self.lift()

            # self.flag1 = 0
        else:
            # self.dfs_path = DFS(graph_route, self.var)
            # self.show_dfsline()
            self.destroy()


class Insert_spot(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Insert')
        self.geometry('500x300')
        self.valid = 0

        self.var_insert = tk.StringVar()

        self.delete = tk.Entry(self, textvariable=self.var_insert, show=None)

        self.label_dfs = tk.Label(self, text='请输入要添加的景点/权值/相邻景点:', font=('楷体', 15)).place(x=80, y=65)
        self.delete.place(x=110, y=125, width=230, height=25)
        self.button_insert = tk.Button(self, text="确认", width=6, height=1, font=('楷体', 15),
                                       command=self.submit).place(x=100, y=230)
        self.button_insert = tk.Button(self, text="取消", width=6, height=1, font=('楷体', 15),
                                       command=self.destroy).place(x=300, y=230)

    def submit(self):
        self.var = self.var_insert.get()
        result = re.search(re.compile('(.*?)/(\d+)/(.*)'), self.var)
        # print(result)
        if result == None or result[3] not in route :
            tk.messagebox.showerror(title='error input', message='请按照正确格式输入')
            self.lift()

            # self.flag1 = 0
        else:
            self.valid = 1
            # self.dfs_path = DFS(graph_route, self.var)
            # self.show_dfsline()
            self.destroy()


def main():
    spotline = spotpage()
    spotline.display()
    spotline.window.mainloop()


main()
