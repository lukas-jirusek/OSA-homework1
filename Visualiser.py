import os

class Visualiser():
    #base visualiser class
    def __init__(self, simulation):
        self.simulation = simulation

    @staticmethod
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
