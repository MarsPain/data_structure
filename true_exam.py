def maze(maze_size, link_input):
    """
    # 晨哥thoughtworks-2018秋招笔试题
    :param maze_size:迷宫大小
    :param link_input:节点连接列表
    :return:
    """
    row = maze_size[0]  # 迷宫行数
    col = maze_size[-1]  # 迷宫列数
    # 初始化连接字典
    link_dict = {}
    for i in range(row):
        for j in range(col):
            link_dict[tuple((i, j))] = []
    # 得到连接字典，键值对为“节点：该节点所连接的节点列表”
    for link_list in link_input:
        link_dict[tuple(link_list[0])].append(tuple(link_list[-1]))
        link_dict[tuple(link_list[-1])].append(tuple(link_list[0]))
    # 字典中的字典列表value去重
    for key in link_dict.keys():
        link_dict[key] = set(link_dict[key])
    print(link_dict)
    link_node_set = set()    # 用于记录深度搜索过程中出现过的节点

    def dfs(node):
        if node in link_node_set:
            return
        else:
            link_node_set.add(node)
            for link_node in link_dict[node]:
                dfs(link_node)
    dfs(tuple((0, 0)))
    print(link_node_set)
    if len(link_node_set) == row*col:   # 如果一次深度搜索能搜索到所有节点，则该迷宫能够连通
        print("Yes!!!!!!")
        return link_dict
    else:
        print("Error!!!!!!!!")
# 案例测试
maze_size = [3, 3]
link_input = [[(0, 1), (0, 2)], [(0, 0), (1, 0)], [(0, 1), (1, 1)], [(0, 2), (1, 2)], [(1, 0), (1, 1)],
              [(1, 1), (1, 2)], [(1, 1), (2, 1)], [(1, 2), (2, 2)], [(2, 0), (2, 1)]]
link_dict = maze(maze_size, link_input)