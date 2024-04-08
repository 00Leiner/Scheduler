class programConstraints:
    def __init__(self, program_course_assign_once, program_schedule_noOverlap) -> None:
        self.program_course_assign_once = program_course_assign_once
        self.program_schedule_noOverlap = program_schedule_noOverlap
        
    def program_constraints(self, program_id, course_code, course_type, day1, day2, time1, time2):
        if not any(self.assign_once(program_id, course_code), self.schedule(program_id, course_type, day1, day2, time1, time2)):
            return False
        return True
        
    def assign_once(self, program_id, course_code):
        if (program_id, course_code) in self.program_course_assign_once:
            return False
        
        self.program_course_assign_once.add((program_id, course_code))
        return True
    
    def schedule(self, program_id, course_type, day1, day2, time1, time2):
        if course_type == 'Laboratory':
            plus1 = 3
            plus2 = 2
        else:
            plus1 = 2
            plus2 = 1
            
        if program_id not in self.program_schedule_noOverlap:
            self.addAll(program_id, course_type, day1, day2, time1, time2, plus1, plus2)
            return True
        
        if not all(day1 in self.program_schedule_noOverlap[program_id], day2 in self.program_schedule_noOverlap[program_id]):
            self.addAll(program_id, course_type, day1, day2, time1, time2, plus1, plus2)
            return True
            
        if day1 in self.program_schedule_noOverlap[program_id]:
            for time in range(time1, (time1 + plus1)):
                if time in self.program_schedule_noOverlap[program_id][day1]:
                    return False
        
        if day2 in self.program_schedule_noOverlap[program_id]:
            for time in range(time2, (time2 + plus2)):
                if time in self.program_schedule_noOverlap[program_id][day2]:
                    return False
            
        self.addAll(program_id, course_type, day1, day2, time1, time2, plus1, plus2)
        return True
        
    def addAll(self,program_id, course_type, day1, day2, time1, time2, plus1, plus2):
        self.program_schedule_noOverlap[program_id][day1].append((range(time1, (time1 + plus1))))
        self.program_schedule_noOverlap[program_id][day2].append((range(time2, (time2 + plus2))))
   