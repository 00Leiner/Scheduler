def check_room_availability(var, domain):
    (program_id, course_code, course_type, instructor, room1, room2, day1, day2, time1, time2) = var
    if course_type == 'Laboratory':
        time_requirements_1 = 3
        time_requirements_2 = 2
    else:
        time_requirements_1 = 2
        time_requirements_2 = 1
    
    # Check room availability for room1
    for ts in range(time1, time1 + time_requirements_1):
        if not any((program_id, course_code, course_type, instructor, room1, _, day1, _, ts, _) == (_program_id, _course_code, _course_type, _instructor, _room1, _, _day1, _, _time1, _) for _program_id, _course_code, _course_type, _instructor, _room1, _, _day1, _, _time1, _ in domain):
            return False
    
    # Check room availability for room2
    for ts in range(time2, time2 + time_requirements_2):
        if not any((program_id, course_code, course_type, instructor, _, room2, _, day2, _, ts) == (_program_id, _course_code, _course_type, _instructor, _, _room2, _, _day2, _, _time2) for _program_id, _course_code, _course_type, _instructor, _, _room2, _, _day2, _, _time2 in domain):
            return False
    
    return True
