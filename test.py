import numpy as np
class Spot:
    def __init__(self, name, weight, serial):
        self._name = ''
        self._weight = 0
        self._serial = 0

    def getname(self):
        return self._name

    def getweight(self):
        return self._weight

    def getserial(self):
        return self._serial


def print_spot(spot):
    print(spot.getname(), spot.getweight(), spot.getserial(), end=" ")


def find_spot(spotlist, name):
    for spot in spotlist:
        if spot.getname() == name:
            print_spot(spot)


def delete_spot(spotlist, name):
    for spot in spotlist:
        if spot.getname() == name:
            spotlist.remove(spot)


# def readfile(self):
#     try:
#         with open(r'C:\Users\蒋明峰\Desktop\text.txt', 'r') as f:
#             content = f.readline()
#             if content != '':
#                 s = content.rstrip('\n').split(',')
#                 self._name, self._weight, self._serial = s[0], int(s[1]), int(s[2])
#     except:
#         print('invalid file')
#         exit(0)


def sign_in():
    print('*********欢迎来到景区旅游信息系统*********')
    print('1.创建景区景点分布图')
    print('2.输出景区景点分布图')
    print('3.输出导游路线')
    print('4.输出最佳导游路线')
    print('5.输出最佳路径')
    print('6.输出道路修建规划图')
    print('7.退出系统')


def input_num():
    choose_num = input()
    if choose_num.isdigit():
        if int(choose_num) < 1 or int(choose_num) > 7:
            print('invalid input')
        else:
            print('welcome')
    else:
        print('please input a num')


def readfile_spots():
    try:
        with open(r'C:\Users\蒋明峰\Desktop\spots.txt', 'r') as f:
            spotlist = []

            content = f.readlines()
            for line in content:
                s = line.rstrip('\n').split(',')
                name, serial = s[0], s[1]
                spotlist.append(s)
            return spotlist
            # print(spotlist)
    except:
        print('invalid file')
        exit(0)


def readfile_weight():
    try:
        with open(r'C:\Users\蒋明峰\Desktop\weight.txt', 'r') as f:
            line = f.readlines()
            l = []
            for w in line:
                str =w.rstrip('\n').split(',')
                l.append(str)
            return l
            # print(l)
    except:
        print('invalid file')
        exit(0)


spot = []
weight = []
spot = readfile_spots()
weight = readfile_weight()
# print(spot)
# print(weight)
# readfile_spots()


# def get_degree(weight):
#     degree = []
#     for i in weight:
#         num = 0
#         for j in i:
#             if int(j) != 0:
#                 num += 1
#         degree.append(num)
#     print(degree)
#
#
# get_degree(weight)
tour_route = ['周立1', '周立2', '周立3', '周立4', '周立5']
tour_mat =[[0, 1, 0, 0, 0],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 1, 0],
           [0, 1, 1, 0, 1],
           [0, 0, 0, 1, 0]]
# c = np.matmul(tour_mat, tour_mat)
# print(np.matmul(c, tour_mat))
# def jdg_loop(tour_mat):

def graph_create(mat, route):
    graph = {}

    for i in range(len(route)):
            val = []
            for num in range(len(mat[i])):
                if   mat[i][num] != 0 :
                    val.append(chr(num + 65))
            graph[route[i]] = val
    print(graph)

def edge_create(mat, route):
    edge = []
    for i in range(len(route)):
            for num in range(i+1):
                if  mat[i][num] != 0 :
                    ele = []
                    ele.append(mat[i][num])
                    ele.append(route[num])
                    ele.append(route[i])
                    edge.append(ele)
    print(edge)

edge_create(tour_mat,tour_route)

