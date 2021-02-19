from Directions import Directions
from string import ascii_uppercase
from OddsGridCell import OddsGridCell
import Odds
import numpy as np

WIDTH = 7
HEIGHT = 5

ROWS = HEIGHT
COLUMNS = WIDTH

#define absorbing points
absorbing = {
    (2, 0) : OddsGridCell("Kumbál", True),
    (0, 3) : OddsGridCell("Výtah", True),
    (2, 6) : OddsGridCell("Restaurace", True)
}


#define starting point
start = (4, 3), OddsGridCell("Start", False)


#check points defined above
for row, col in absorbing:
    assert 0 <= row < ROWS and 0 <= col < COLUMNS

row, col = start[0]
assert 0 <= row < ROWS and 0 <= col < COLUMNS
    
class OddsGrid:
    # grid constructor
    def __init__(self):

        # grid is 2D representation of the space
        self.grid = [[None] * COLUMNS for _ in range(ROWS)]

        
        #create cells
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row, col) in absorbing:
                    self.grid[row][col] = absorbing[row, col]
                elif (row, col) == start[0]:
                    self.grid[row][col] = start[1]
                else:
                    self.grid[row][col] = OddsGridCell()
        
        #calculate internal movement matrix (considering 5*7 cells = 35 * 35 movement matrix)
        self.set_all_odds()

    # set neigbhor movement odds for each cell
    def set_neighbor_odds(self):        
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                self.set_neighbor_odds_cell(cell, row_index, col_index)

    #fixes odds for cells near edges of grid
    @staticmethod
    def fix_odds(odds, row, col):
        
        if col == 0:
            # we cannot move to left
            odds[Directions.NONE] += odds[Directions.LEFT]
            odds[Directions.LEFT] = 0
        if col == COLUMNS - 1:
            # we cannot move to right
            odds[Directions.NONE] += odds[Directions.RIGHT]
            odds[Directions.RIGHT] = 0
        if row == 0:
            # we cannot move up
            odds[Directions.NONE] += odds[Directions.UP]
            odds[Directions.UP] = 0
        if row == ROWS - 1:
            # we cannot move down
            odds[Directions.NONE] += odds[Directions.DOWN]
            odds[Directions.DOWN] = 0
        
    #sets movement dictionary to neighbors for one cell
    @staticmethod
    def set_neighbor_odds_cell(cell, row, col):
        if (row, col) in absorbing:
            #absorbing celldoesnt allow further movement, only "movement" is to stay
            cell.set_neighbor_odds(
            {
                Directions.UP : 0,
                Directions.LEFT : 0,
                Directions.DOWN : 0,
                Directions.RIGHT : 0,
                Directions.NONE : 1
            }
            )
            return

        elif row == 0:
            #extra case for top row    
            if col < 3:
                #extra case for top tow, left from elevator
                odds = Odds.TOP_LEFT.copy()
            
            else:
                #extra case for top tow, right from elevator
                odds = Odds.TOP_RIGHT.copy()
        else:
            #normal case for every other cell
            odds = Odds.NORMAL.copy()

        #fix movement odds near edges of grid
        OddsGrid.fix_odds(odds, row, col)

        #store the movement odds in cell 
        cell.set_neighbor_odds(odds)
    
    #creates odds of movement to ALL cells (unlike just neighbors above)
    def set_all_odds(self):
        self.set_neighbor_odds()

        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                self.set_all_odds_cell(cell, row_index, col_index)


    #creates odds of movement to ALL cells (function for one cell)
    def set_all_odds_cell(self, cell, cell_row, cell_col):
        oddsarray = []
        #for all other cells
        odds = cell.get_neighbor_odds()
        for row_index, row in enumerate(self.grid):
            oddsarray_row = []
            for col_index in range(len(row)):
                #check if the other cell is neighbor, if it is, use odds stored inside cell to get a chance to get there
                if cell_row == row_index and cell_col == col_index:
                    oddsarray_row.append(odds[Directions.NONE])

                elif cell_row - 1 == row_index and cell_col == col_index:
                    oddsarray_row.append(odds[Directions.UP])

                elif cell_row + 1 == row_index and cell_col == col_index:
                    oddsarray_row.append(odds[Directions.DOWN])

                elif cell_row == row_index and cell_col - 1 == col_index:
                    oddsarray_row.append(odds[Directions.LEFT])

                elif cell_row == row_index and cell_col + 1 == col_index:
                    oddsarray_row.append(odds[Directions.RIGHT])
                else:
                    #if cell is not a neighbor, we cant move there
                    oddsarray_row.append(0)
            oddsarray.append(oddsarray_row)
        #store odds of all movements inside cell
        cell.all_odds = oddsarray


    #allows user to input cell to check odds to visit each neighbor
    def debug_odds(self):
        while 1:
            res = input("Enter cell: ")
            if res in ["q", "quit", ""]:
                break
            elif len(res) == 2:
                col = ascii_uppercase.find(res[0].upper())
                row = ROWS - int(res[1])
                assert 0 <= row < ROWS and 0 <= col < COLUMNS
                self.to_string(self.grid[row][col].all_odds)

    #returns movement matrix from all cells - again, big 35 * 35 matrix (for 7*5 cells)
    def get_matrix(self) -> np.array(np.array(float)):                # get 35 * 35 matrix with movement odds
        return np.array([cell.get_flattened_odds() for row in self.grid for cell in row])

    #returns start vector - start position is marked with 1, other cells with 0
    @staticmethod
    def get_start() -> np.array(float):          # row with start
        arr = [0] * (ROWS * COLUMNS)
        row, col = start[0] 
        arr[COLUMNS * row + col] = 1
        return np.array(arr)

    #returns labels of grid, includes odds of provided
    def get_labels(self, odds = None):
        labels = []
        for row_index, row in enumerate(self.grid):
            labels_row = []
            for col_index, cell in enumerate(row):

                label = f"{ascii_uppercase[col_index]}{ROWS - row_index}\n"

                if cell.name:
                    label += cell.name

                label += "\n"

                if odds is not None and (cell_odds := odds[row_index * COLUMNS + col_index]):
                    label += f"{cell_odds * 100:.3f} %"

                labels_row.append(label)
            labels.append(labels_row)
        return labels

    #returns string representation of grid using labels, with odds, if provided
    def to_string(self, odds = None):        
        width = COLUMNS * 15 + 1
        string = "-" * width + "\n"
        labels = self.get_labels(odds)
        for row in labels:

            string += "|"
            for label in row:
                position, _, _ = label.split("\n")
                string += f"{position : ^14}|"

            string += "\n|"
            for label in row:
                _, name, _ = label.split("\n")
                string += f"{name : ^14}|"

            if odds is not None:
                string += "\n|"
                for label in row:
                    _, _, cell_odds = label.split("\n")
                    string += f"{cell_odds : ^14}|"

            string += "\n" + "-" * width + "\n"
        return string

    #prints grid, without any odds
    def __str__(self):
        return self.to_string()

#testing        
if __name__ == '__main__':
    print(OddsGrid.get_start())
    test = OddsGrid()
    
    print(a := test.grid[4][0].all_odds)
    print(lab := test.get_labels(a))
    print(lab := test.to_string(a))

    '''
    print(test)
    test.debug_odds()

    print(test.grid[4][0].odds)
    print(test.grid[4][0].all_odds)
    #print(test)
    #print(test.grid[3][4].odds)
    '''