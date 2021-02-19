from Visualiser import Visualiser

class TerminalVisualiser(Visualiser):
    #visualiser showing the simulation in a terminal
    def __init__(self, simulation):
        super().__init__(simulation)
    
    def run(self):
        while True:
            Visualiser.cls()
            self.simulation.print()
            self.simulation.step()
            if input("Press Enter to continue or Q to exit: ").lower() in ["q", "quit", "exit"]:
                break