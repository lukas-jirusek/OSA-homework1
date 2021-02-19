from Visualiser import Visualiser

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import seaborn as sb

class MatPlotLibVisualiser(Visualiser):
    #visualiser showing the simulation in matplotlib windows, one by one
    def __init__(self, simulation):
        super().__init__(simulation)
    
    def prepare_graph(self):
        labels = self.simulation.get_labels(self.simulation.odds)
        fig, ax = plt.subplots(
            figsize=(12, 7)
        )
        fig.canvas.set_window_title(self.simulation.title)
        ax.set_title(
            self.simulation.get_title(),
            loc = "left"
        )
        ax = sb.heatmap(
            self.simulation.odds.reshape(len(self.simulation.grid.grid), len(self.simulation.grid.grid[0])) * 100, 
            annot = labels, 
            fmt = '',
            linewidths = 1, 
            vmax = 70, 
            norm = LogNorm(vmin=0.4, vmax=70, clip=True),
            cmap = "viridis",
            xticklabels = ["A", "B", "C", "D", "E", "F", "G"],
            yticklabels = ["5", "4", "3", "2", "1"],
            cbar_kws = {
                'format': '%.0f%%',
                'ticks' : [0.4, 1, 3, 5, 10, 20, 40, 70],
            }
        )
        ax.tick_params(axis='y', rotation=0)

    def run(self):
        while True:
            Visualiser.cls()
            print(self.simulation.get_title())
            self.prepare_graph()
            plt.show()
            plt.close()
            self.simulation.step()
            if input("Press Enter to show next step or Q to exit: ").lower() in ["q", "quit", "exit"]:
                break
