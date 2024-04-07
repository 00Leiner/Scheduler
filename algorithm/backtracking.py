
class backtrackingAlgorithm:
    def __init__(self, domain_assignment, forwardsearch, constraintpropagation) -> None:
        self.domain_assignment = domain_assignment
        self.constraintpropagation = constraintpropagation
        self.forwardsearch = forwardsearch
        self.instructor_schedule = {}
        
    def backtracking_search(self, numSolution):
        solutions = []
        self.backtrack({}, solutions, numSolution)
    
    def backtrack(self, schedule, solutions, numSolutions):
        if len(solutions) == numSolutions:
            return# Stop the search if the desired number of solutions is reached
        
        list_domain_assignment = self.domain_assignment
        program_course = set() #used as basis for complete scheduling
        
        if len(schedule) == len(program_course):
            # Solution found, append it to the list of solutions
            solutions.append(schedule.copy())  # Use copy to avoid modifying the original assignment
            return
        
        program_id, course_code, instructor, room1, room2, day1, day2, time1, time2 = list_domain_assignment #set of domain data 
        
        program_course.add((program_id, course_code)) #get all unique combination of program course data
        
        # Apply forward checking and constraint propagation
        if self.forwardsearch.forwardChecking(schedule, program_id, course_code, instructor, room1, room2, day1, day2, time1, time2) \
           and self.constraintpropagation.constraint_propagation(schedule, program_id, course_code, instructor, room1, room2, day1, day2, time1, time2):
            
            schedule[(program_id, course_code)] = {
                'instructor': instructor,
                'schedule_1' :{
                    'room': room1,
                    'day': day1,
                    'time': time1
                },
                'schedule_2' :{
                    'room': room2,
                    'day': day2,
                    'time': time2
                }
            }
            
            # Recursive call to continue the search
            self.backtrack(schedule, solutions, numSolutions)
                        
            # Backtrack: remove the current assignment to explore other possibilities
            del schedule[(program_id, course_code)]
        
        
        return None
    