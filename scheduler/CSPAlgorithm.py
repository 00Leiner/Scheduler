from domain.assignmnet_domain import assignmnetDomain
from algorithm.backtracking import backtrackingAlgorithm
from utils.data_format import formatting_data

class CSPAlgorithm:
    def __init__(self, programs, courses, instructors, rooms) -> None:
        self.define_domain_variable(programs, courses, instructors, rooms)
        self.define_algorithm()
        self.define_result(programs, courses, instructors, rooms)
    
    def define_domain_variable(self, programs, courses, instructors, rooms):
        assignmnet = assignmnetDomain(programs, courses, instructors, rooms)
        self.domain_assignment = assignmnet.assignment()
        #print(self.domain_assignment)
        
    def define_algorithm(self):
        algo = backtrackingAlgorithm(self.domain_assignment)
        self.result = algo.backtracking_search()
        #print(result)
    
    def define_result(self, programs, courses, instructors, rooms):
        student_details = {student['_id']: student for student in programs}
        course_details = {course['code']: course for course in courses}
        teacher_details = {teacher['_id']: teacher for teacher in instructors}
        room_details = {room['_id']: room for room in rooms}
        schedule = formatting_data(self.result, student_details, course_details, teacher_details, room_details)
        print(schedule)
        return schedule
    