# Tarasidou Anna

from .visualizer import draw_graph


def add_node(graph, node_name, node_degree):
    graph[node_name] = node_degree


def construct_graph(sequence):
    graph_nodes = {}
    edges = []

    sequence.sort(reverse=True)
    for i, d in enumerate(sequence):
        add_node(graph_nodes, f"X{i}", d)

    print("Sequence: ", sequence)
    print("Nodes: ", graph_nodes)

    keys_list = list(graph_nodes.keys())

    for i in range(len(keys_list)):
        key = keys_list[i]
        for j in range(i + 1, len(keys_list)):
            next_node = keys_list[j]
            if graph_nodes[key] > 0 and graph_nodes[next_node] > 0:
                edges.append((key, next_node))
                graph_nodes[key] -= 1
                graph_nodes[next_node] -= 1
            if graph_nodes[key] == 0 or graph_nodes[next_node] == 0:
                continue

    print("Edges: ", edges)
    draw_graph(edges)
