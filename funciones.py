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


def updateSuccessors(successors, parent, visited):
    successorsUpdated = []
    for s in successors:
        if s[0] not in visited:
            successorsUpdated.append(
                (s[0], parent[1] + [s[1]], parent[2] + s[2]))

    return successorsUpdated


def pushPQueue(successors, pqueue):
    for s in successors:
        pqueue.push(s, s[2])
    return pqueue
