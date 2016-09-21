# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import *
from game import Directions
from game import Agent
from game import Actions
from pacman import *

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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
    start = problem.getStartState()
    discovered=[]
    actions=[]
    stack = util.Stack()
    stack.push([start,Directions.STOP])	
    while not stack.isEmpty():
        vertice, path = stack.pop()    
        discovered.append(vertice)
        if not problem.isGoalState(vertice):
            for vizinho in problem.getSuccessors(vertice):
                    if vizinho[0] not in discovered:
                        stack.push([vizinho[0],path+(","+vizinho[1])])
        else:
            break
    return path.split(",")

	

def breadthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    
    start = problem.getStartState()
    discovered=[]
    actions=[]
    queue = util.PriorityQueue()
    queue.push([start,Directions.STOP],0)
    while not queue.isEmpty():
        vertice, path = queue.pop()
        discovered.append(vertice)
        if not problem.isGoalState(vertice):
            for vizinho in problem.getSuccessors(vertice):
                    if vizinho[0] not in discovered:
                        queue.push([vizinho[0],path+(","+vizinho[1])],vizinho[2])
        else:
            break
    return path.split(",")
    
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    start = problem.getStartState()
    discovered=[]
    actions=[]
    queue = util.PriorityQueue()
    queue.push([start,Directions.STOP],0)
    while not queue.isEmpty():
        vertice, path = queue.pop()
        discovered.append(vertice)
        if not problem.isGoalState(vertice):
            for vizinho in problem.getSuccessors(vertice):
                    if vizinho[0] not in discovered:
                        queue.update([vizinho[0],path+(","+vizinho[1])], heuristic(vizinho[0],problem))
        else:
            #print  path.split(",") , "tamanho" ,len(path.split(","))
            break
    return path.split(",")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
