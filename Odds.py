from Directions import Directions

def rotate(odds, direction):
    if direction == Directions.RIGHT:
        # flipping to right - top row, right from elevator
        return {
            Directions.UP : odds[Directions.LEFT],
            Directions.LEFT : odds[Directions.DOWN],
            Directions.DOWN : odds[Directions.RIGHT],
            Directions.RIGHT : odds[Directions.UP],
            Directions.NONE : odds[Directions.NONE]
        }
    elif direction == Directions.LEFT:
        # flipping to left - top row, left from elevator
        return {
            Directions.UP : odds[Directions.RIGHT],
            Directions.LEFT : odds[Directions.UP],
            Directions.DOWN : odds[Directions.LEFT],
            Directions.RIGHT : odds[Directions.DOWN],
            Directions.NONE : odds[Directions.NONE]
        }
    else:
        return odds

def to_string(odds):
    #nicer formatting when printed
    a = odds[Directions.UP]
    b = odds[Directions.RIGHT]
    c = odds[Directions.DOWN]
    d = odds[Directions.LEFT]
    e = odds[Directions.NONE]
    res = \
f"""
         {a:.3f}
           ^
           |
{d:.3f} <- {e:.3f} -> {b:.3f}
           |
           V
         {c:.3f}
"""
    return res

NORMAL = {
    #default movement odds
    Directions.UP : .4,
    Directions.LEFT : .25,
    Directions.DOWN : .1,
    Directions.RIGHT : .25,
    Directions.NONE : 0
}

# test that default odds are equal to 1
assert(sum(NORMAL.values()) == 1.0)

# odds of movement on both sides from elevator are rotated by 90 degrees towards the elevator
TOP_LEFT = rotate(NORMAL, Directions.RIGHT)
TOP_RIGHT = rotate(NORMAL, Directions.LEFT)

if __name__ == '__main__':
    print("Normal odds:", to_string(NORMAL))
    print("Top row left odds:", to_string(TOP_LEFT))
    print("Top row right odds:", to_string(TOP_RIGHT))