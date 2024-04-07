from algorithm.constraintPropagation import ConstraintPropagation
from algorithm.forwardSearch import ForwardSearch
from domain.assignmnet_domain import assignmnetDomain
from algorithm.backtracking import backtrackingAlgorithm

class CSPAlgorithm:
    def __init__(self, programs, courses, instructors, rooms) -> None:
        self.define_domain_variable(programs, courses, instructors, rooms)
    
    def define_domain_variable(self, programs, courses, instructors, rooms):
        assignmnet = assignmnetDomain(programs, courses, instructors, rooms)
        
        self.domain_assignment = assignmnet.assignment()
        #print(self.domain_assignment)
        
    def define_algorithm(self):
        numSolution = 2
        constraintpropagation = ConstraintPropagation()
        forwardsearch = ForwardSearch()
        algo = backtrackingAlgorithm(self.domain_assignment, forwardsearch, constraintpropagation)
        algo.backtracking_search(numSolution)