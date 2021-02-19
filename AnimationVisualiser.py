from MatPlotLibVisualiser import MatPlotLibVisualiser

import matplotlib.pyplot as plt
import os
import webbrowser
import random
import imageio
import shutil

class AnimationVisualiser(MatPlotLibVisualiser):
    #visualiser creating a gif image of the simulation
    def __init__(self, simulation, frames = 100, result_path = "./result.gif"):
        super().__init__(simulation)
        self.path = "./tmp" + str(random.randint(1000000, 20000000000)) + "folder"
        self.frames = frames
        self.result_path = result_path
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def run(self):
        print (f"Generating {self.frames} frames to temporary folder")
        printed = set()
        filenames = []
        for frame in range(self.frames):
            percentage = (frame / self.frames) * 100
            #print(percentage)
            done = int(percentage / 10.0) * 10
            #print(done)
            if done % 10 == 0 and done not in printed:
                print(f"{done} % done...")
                printed.add(done)
            self.prepare_graph()
            path = f"{self.path}/fig{frame:03d}.png"
            plt.savefig(path, dpi=300)
            plt.close()
            filenames.append(path)
            self.simulation.step()
        print(f"Done.")


        print ("\nGenerating animation...")
        images = [imageio.imread(path) for path in filenames]
        imageio.mimsave(self.result_path, images, duration=0.5)
        shutil.rmtree(self.path, ignore_errors=True)
        print ("Done, stored in: " + self.result_path + " opening... ")
        webbrowser.open(os.path.abspath(self.result_path))

