# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import funciones
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """

    stack = util.Stack()
    visited = []
    path = []

    state = problem.getStartState()
    visited.append(state)
    isGoal = problem.isGoalState(state)

    if isGoal:
        return []

    successors = problem.getSuccessors(state)

    stack = funciones.pushSuccessors(successors, stack, visited)

    while True:

        if stack.isEmpty():
            break

        state = stack.pop()
        stack.push(state)
        isGoal = problem.isGoalState(state[0])

        if isGoal:
            path.append(state[1])
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:
            visited.append(state[0])
            path.append(state[1])
            successors = problem.getSuccessors(state[0])
            successors = [s for s in successors if s[0] not in visited]
            stack = funciones.pushSuccessors(successors, stack, visited)
        else:
            stack.pop()
            path.pop()
    return path


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    queue = util.Queue()
    visited = []
    directions = {}

    start = [problem.getStartState()]
    queue.push(start)
    directions[start[0]] = []
    path = []

    while True:
        if queue.isEmpty():
            break
        state = queue.pop()
        isGoal = problem.isGoalState(state[0])
        if isGoal:
            print("Goal is: ", state[0])
            path = directions[state[0]]
            break

        if state[0] not in visited:

            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            successors = [s for s in successors if s[0] not in visited]
            queue = funciones.pushSuccessors(successors, queue, visited)
            parentPath = directions[state[0]]
            directions = funciones.setSuccessorsPaths(
                directions, successors, parentPath)

        else:
            if not queue.isEmpty():
                queue.pop
    return path


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pqueue = util.PriorityQueue()
    visited = []
    path = []

    start = problem.getStartState()
    isGoal = problem.isGoalState(start)
    start = [start, [], 0]

    if isGoal:
        return []
    pqueue.push(start, start[2])

    while True:
        if pqueue.isEmpty():
            break

        state = pqueue.pop()
        isGoal = problem.isGoalState(state[0])

        if isGoal:
            path = state[1]
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:
            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            successors = funciones.updateSuccessors(successors, state, visited)
            pqueue = funciones.pushPQueue(successors, pqueue)

    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
