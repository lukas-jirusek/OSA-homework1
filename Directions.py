from enum import Enum, auto

class Directions(Enum):
    #directions used when moving
    NONE = auto()
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

if __name__ == '__main__':
    print(Directions.NONE)
    print(Directions.UP.name)
    print(Directions.UP.value)