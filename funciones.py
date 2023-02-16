def pushSuccessors(successors, structure, seen):
    for s in successors:
        structure.push(s)
    return structure


def isStateVisited(visited, state):
    return state in visited


def setSuccessorsPaths(directions, successors, parentPath):
    keys = directions.keys()
    for s in successors:
        if s[0] not in keys:
            directions[s[0]] = parentPath + [s[1]]
    return directions
