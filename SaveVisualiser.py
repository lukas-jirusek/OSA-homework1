from MatPlotLibVisualiser import MatPlotLibVisualiser

import matplotlib.pyplot as plt
import os
import webbrowser

class SaveVisualiser(MatPlotLibVisualiser):
    #visualiser saving photos of the simulation to a folder of choosing
    def __init__(self, simulation, path = "./tmp", frames = 100):
        super().__init__(simulation)
        self.path = path
        self.frames = frames
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
    def run(self):
        print (f"Generating {self.frames} frames")
        printed = set()
        for frame in range(self.frames):
            percentage = (frame / self.frames) * 100
            #print(percentage)
            done = int(percentage / 10.0) * 10
            #print(done)
            if done % 10 == 0 and done not in printed:
                print(f"{done} % done...")
                printed.add(done)
            self.prepare_graph()
            plt.savefig(f"{self.path}/fig{frame:03d}.png", dpi=300)
            plt.close()
            self.simulation.step()
        print(f"Done.")
        print(f"Files saved to {self.path}, opening")
        webbrowser.open(os.path.abspath(self.path))