from algorithm.forwardChecking import forwardChecking

class backtrackingAlgorithm:
    def __init__(self, domain_assignment):
        self.domain_assignment = domain_assignment
        self.program_course = set((program_id, course_code) for program_id, course_code, _, _, _, _, _, _, _, _, in self.domain_assignment)
        
    def backtracking_search(self):
        result = []
        self.backtrack({}, self.domain_assignment, {}, result)
        print(result)
        return result
    
    def backtrack(self, schedule, domain, teacher_schedule, result):
        if len(result) == 2:
            return
        if len(schedule) == len(self.program_course):
            result.append(schedule.copy())
            return 
        
        var = self.select_unassigned_variable(schedule, domain)
        
        if var is None:
            return  # backtrack
        
        (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = var
        
        if course_type == 'Laboratory':
            time_requirements_1 = 3
            time_requirements_2 = 2
        else:
            time_requirements_1 = 2
            time_requirements_2 = 1
        
        schedule[(program_id, course_code)] = {
            'instructor': instructor,
            'schedule_1':{
                'room': room1,
                'day': day1,
                'time': (time1, time1 + time_requirements_1)
            },
            'schedule_2':{
                'room': room2,
                'day': day2,
                'time': (time2, time2 + time_requirements_2)
            }
        }
        
        # Perform forward checking
        update_domain = forwardChecking(var, domain)
        
        #recursion
        self.backtrack(schedule, update_domain, teacher_schedule, result)
        
        del schedule[(program_id, course_code)]
        
    def select_unassigned_variable(self, schedule, domain):
        for var in domain:
            (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = var
            if (program_id, course_code) not in schedule:
                    return var
                
        return None
    
    def instructor_schedule(self, teacher_schedule, instructor, day1, day2, time1, time2, course_type):
        if instructor not in teacher_schedule:
            teacher_schedule[instructor] = {day1: [], day2: []}
        
        if day1 not in teacher_schedule[instructor]:
            teacher_schedule[instructor][day1] = []
            
        if day2 not in teacher_schedule[instructor]:
            teacher_schedule[instructor][day2] = []
        
        if course_type == 'Laboratory':
            time_requirements_1 = 3
            time_requirements_2 = 2
        else:
            time_requirements_1 = 2
            time_requirements_2 = 1
            
        # Check if the instructor has more than 5 different days scheduled
        if len(teacher_schedule[instructor]) > 5:  # 4 because we are adding day1 and day2 below
            print('instructor exceed 5 days a week')
            print('instructor_id: ', instructor)
            return False
        
        # Check if the total time slots for a day exceed 6
        if len(teacher_schedule[instructor][day1]) + time_requirements_1 > 6:
            print('instructor exceed 6 hours a day')
            print('instructor_id: ', instructor, 'day: ', day1)
            return False

        if len(teacher_schedule[instructor][day2]) + time_requirements_2 > 6:
            print('instructor exceed 6 hours a day')
            print('instructor_id: ', instructor, 'day: ', day1)
            return False

        # Check for time slot conflicts
        for ts in range(time1, time1 + time_requirements_1 + 1):
            if ts in teacher_schedule[instructor][day1]:
                return False
        
        for ts in range(time2, time2 + time_requirements_2 + 1):
            if ts in teacher_schedule[instructor][day2]:
                return False
          
        teacher_schedule[instructor][day1].extend(range(time1, time1 + time_requirements_1))
        teacher_schedule[instructor][day2].extend(range(time2, time2 + time_requirements_2))
        return True