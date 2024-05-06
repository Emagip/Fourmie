def getWhereCanGo(line, col):
    can_go_to = []

    if col == 0:
        can_go_to.append((0, 1))

    elif col == 4:
        can_go_to.append((0, -1))

    else:
        can_go_to.append((0, 1))
        can_go_to.append((0, -1))

    if line == 4:
        can_go_to.append((-1, 0))
    elif line == 0:
        can_go_to.append((1, 0))
    else:
        can_go_to.append((1, 0))
        can_go_to.append((-1, 0))
    return can_go_to


def GetCoords(coords_in):
    coords_out = (
        50 + (100 * coords_in[0]),
        50 + (100 * coords_in[1])
    )
    return coords_out

def set():
    plateau = []
    HasCandy = False
    for i in range(5):
        plateau.append([])
        if i == 4:
            HasCandy = True
        for j in range(5):
            plateau[i].append({
                "can_go": getWhereCanGo(i, j),
                "HasCandy": HasCandy
            })
    return plateau
