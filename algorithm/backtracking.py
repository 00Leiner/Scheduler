from algorithm.otherAlgorithm import ConstraintPropagation

class backtrackingAlgorithm:
    def __init__(self, domain_assignment) -> None:
        self.domain_assignment = domain_assignment
        self.program_course = set((program_id, course_code) for program_id, course_code, _, _, _, _, _, _, _, _, in self.domain_assignment) #used as basis for complete scheduling
        
        #print(self.domain_assignment)
        
    def define_variable_for_constraints(self):
        program_course_assign_once = set()
        program_schedule_noOverlap = {}
        instructor_scheduler = {}
        room_schedule = {}
        self.ConstraintPropagation = ConstraintPropagation(program_course_assign_once, program_schedule_noOverlap, instructor_scheduler, room_schedule)
        
        
    def backtracking_search(self, numSolution):
        solutions = []
        self.backtrack({}, solutions, numSolution)
    
    def backtrack(self, schedule, solutions, numSolutions):
        if len(solutions) == numSolutions:
            return# Stop the search if the desired number of solutions is reached
        
        
        if len(schedule) == len(self.program_course):
            # Solution found, append it to the list of solutions
            solutions.append(schedule.copy())  # Use copy to avoid modifying the original assignment
            return
        
        (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = self.domain_assignment #set of domain data 

        update_domain = self.constraints_propagation(program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2)
            
        """
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
                del schedule[(program_id, course_code)]"""
   
        return None
    