class OddsGridCell:
    #class for storing info about one cell
    def __init__(self, name = "", absorbing = False):

        #name, if any, for example "Elevator"
        self.name = name

        #true, if it is absorbing
        self.absorbs = absorbing

        #movement odds for 5 directions (4 neighbors, no movement)
        self.neighbor_odds = None

        #movement odds to all cells in a grid
        self.all_odds = None
    
    def set_neighbor_odds(self, odds):
        self.neighbor_odds = odds

    def get_neighbor_odds(self):
        return self.neighbor_odds
    
    def get_flattened_odds(self):
        #[j for sub in ini_list for j in sub] 
        return [val for row in self.all_odds for val in row]
    
    

        