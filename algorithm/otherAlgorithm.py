class ConstraintPropagation:
    def __init__(self, program_course_assign_once, program_schedule_noOverlap, instructor_scheduler, room_schedule) -> None:
        self.program_course_assign_once = program_course_assign_once
        self.program_schedule_noOverlap = program_schedule_noOverlap
        self.instructor_scheduler = instructor_scheduler
        self.room_schedule = room_schedule
        
    def constraintPropagation(self):
        pass