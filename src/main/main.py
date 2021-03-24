import json

import numpy as np
import pandas as pd

import plotly.offline as py
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx

import sys

class NetworkMap:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = []
        for edge in edges:
            self.edges.append( (edge[0], edge[1]) )

    def map(self):
        netmap = nx.Graph()
        netmap.add_edges_from(self.edges)

        plt.subplot(121)
        nx.draw(netmap, with_labels=True, font_weight='bold')
        plt.savefig("C:\\Users\\BATLab-035\\network-overlay-py\\network_graph.png", format="png")
        plt.show()


def main(args):
    filename = args[1]

    mapfile = open(filename, 'r')
    map_data = json.load(mapfile)
    mapfile.close()

    nodes = map_data["network"]["nodes"]
    connections = map_data["network"]["connections"]

    netmap = NetworkMap(nodes, connections)




if __name__ == '__main__':
    main(sys.argv)