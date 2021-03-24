import json

import numpy as np
import pandas as pd

import plotly.offline as py
import plotly.graph_objects as go
import networkx as nx

import sys

class NetworkMap:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def map(self):
        netmap = nx.Graph()


def main(args):
    print("Hello World!")
    filename = args[1]

    mapfile = open(filename, 'r')
    map_data = json.load(mapfile)
    mapfile.close()

    nodes = map_data["network"]["nodes"]
    connections = map_data["network"]["connections"]

    netmap = NetworkMap(nodes, connections)


    print(connections)



if __name__ == '__main__':
    main(sys.argv)