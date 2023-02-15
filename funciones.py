def pushSuccessors(successors, stack, seen):
    for s in successors:
        if s[0] not in seen:
            stack.push(s)
    return stack


def isStateVisited(visited, state):
    return state in visited
