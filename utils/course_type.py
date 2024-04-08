def course_type(courses):
    _type = {}
    for course in courses:
        _type[course['code']] = course['type']
        
    return _type