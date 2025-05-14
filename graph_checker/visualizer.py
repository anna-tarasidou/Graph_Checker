import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(edges):
    g = nx.Graph()
    g.add_edges_from(edges)
    nx.draw(g, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    plt.title("Constructed Graph")

    plt.show()
