def getWhereCanGo(line, col):
    """prend en entrée la position relative de la fourmie sur le plateau
    renvoi une liste de tuples correspondant
    aux mouvements possibles de la fourmie"""
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
    """prend en entrée la position relative de la fourmie sur le plateau
    renvoi les coordonnées tk y correspondant"""
    coords_out = (
        100 + (200 * coords_in[0]),
        100 + (200 * coords_in[1])
    )
    return coords_out


def set():
    """ne prend rien en entree
    renvoie une liste de listes de dictionnaires correspondant au plateau
    chaques sous-listes correspondant a une ligne,
    chaques dictionnaires correspondant a une case"""
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
