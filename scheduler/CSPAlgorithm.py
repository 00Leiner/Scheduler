from domain.assignmnet_domain import assignmnetDomain
from algorithm.backtracking import backtrackingAlgorithm

class CSPAlgorithm:
    def __init__(self, programs, courses, instructors, rooms) -> None:
        self.define_domain_variable(programs, courses, instructors, rooms)
        self.define_algorithm()
    
    def define_domain_variable(self, programs, courses, instructors, rooms):
        assignmnet = assignmnetDomain(programs, courses, instructors, rooms)
        
        self.domain_assignment = assignmnet.assignment()
        #print(self.domain_assignment)
        
    def define_algorithm(self):
        algo = backtrackingAlgorithm(self.domain_assignment)
        result = algo.backtracking_search()