def calculate_gpa(grades):
    total_grade_points=sum(grades.values())
    total_course=len(grades)
    if total_course==0:
        return 0
    return total_grade_points/total_course