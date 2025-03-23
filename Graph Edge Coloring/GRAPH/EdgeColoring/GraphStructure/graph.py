import networkx as nx
import matplotlib.pyplot as plt

def complete(n):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            graph[i].append(j)
            graph[j].append(i)
    return graph

def cycle(n):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        graph[i].append((i + 1) % n)
        graph[(i + 1) % n].append(i)
    return graph

def star(n):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        if i != 0:
            graph[0].append(i)
            graph[i].append(0)
    return graph

def fan(n):
    graph = {i: [] for i in range(n)}
    for i in range(1, n):
        graph[0].append(i)
        graph[i].append(0)
    for i in range(1, n - 1, 2):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    return graph

def sibling(n):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n:
            graph[i].append(left_child)
        if right_child < n:
            graph[i].append(right_child)
        if left_child < n and right_child < n:
            graph[left_child].append(right_child)
            graph[right_child].append(left_child)
    return graph

def binary(n):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n:
            graph[i].append(left_child)
            graph[left_child].append(i)
        if right_child < n:
            graph[i].append(right_child)
            graph[right_child].append(i)
    return graph

def path(n):
    graph = {i: [] for i in range(n)}
    for i in range(n - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    return graph

def plot_graph(graph, title="Graph"):
    G = nx.Graph(graph)
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_size=16, font_color='black')
    plt.title(title)
    plt.show()

def show(n, k):
    if k == 1:
        graph = complete(n)
    elif k == 2:
        graph = cycle(n)
    elif k == 3:
        graph = star(n)
    elif k == 4:
        graph = fan(n)
    elif k == 5:
        graph = sibling(n)
    elif k == 6:
        graph = binary(n)
    elif k == 7:
        graph = path(n)
    else:
        print("Invalid Inputs")
        return
    return graph