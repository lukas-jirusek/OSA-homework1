from OddsGrid import OddsGrid
from datetime import datetime, timedelta
from numpy import matmul as matrix_multiply

class Simulation:
    #initialize data
    def __init__(self, 
                 grid : OddsGrid = None,
                 title : str = "",
                 start_time : datetime = datetime(2020, 2, 16, 7, 0, 0),
                 time_delta : timedelta = timedelta(seconds=20)                 
                 ):
        if grid == None:
            self.grid = OddsGrid()
        else:
            self.grid = grid
        self.title = title
        self.start_time = start_time
        self.delta = time_delta
        self.matrix = self.grid.get_matrix()
        self.reset()

    #resets simulation
    def reset(self):
        self.odds = self.grid.get_start()
        self.current_time = self.start_time
        self.steps = 0

    #moves simulation one step further
    def step(self):
        self.odds = matrix_multiply(self.odds, self.matrix)
        self.steps += 1
        self.current_time += self.delta
    
    #returns title + info about current step
    def get_title(self):
        return f"{self.title}\n{self.current_time.time()} {' ' * 8} Δ {self.current_time - self.start_time} {' ' * 8} {self.steps} krok(ů)"
    
    #returns grid labels
    def get_labels(self, odds = None):
        return self.grid.get_labels(odds)

    #prints simulation to terminal
    def print(self):
        print(self.get_title(), self.grid.to_string(self.odds), sep='\n')
    

if __name__ == '__main__':
    test = OddsGrid()
    sim = Simulation(test, "Test")
    sim.print()
    sim.step()

    sim.step()
    sim.print()