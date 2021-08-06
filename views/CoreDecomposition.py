import pandas as pd
import networkx as nx
from typing import Dict
from .View import View
from views.components import TableComponent, AirportsMapComponent
import matplotlib.pyplot as plt
import nx_altair as nxa


class CoreDecomposition(View):
    def render(self, graphs):
        pass
        # TODO K-core
        # TODO K-shell
        # TODO innermost core
