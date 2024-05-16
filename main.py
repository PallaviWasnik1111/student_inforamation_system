#studen_information_system/main.py
from student import Student
from course import Course
from grade_calculator import calculate_gpa

#create object
student1=Student("001","piyush")
student2=Student("002","vrushabh")

#create course
ds_course=Course("DS01","data science 101")
da_course=Course("DA01","data science 102")
#enroll student course
student1.add_course(ds_course,90)
student1.add_course(ds_course,85)
student2.add_course(da_course,78)
student2.add_course(da_course,92)

#display student information
print(f"{student1.name}'s grades:{student1.get_grades}")
print(f"{student2.name}'s grades:{student2.get_grades}")

#calculate and display GPA
gpa_student1=calculate_gpa(student1.get_grades())
gpa_student2=calculate_gpa(student2.get_grades())
print(f"{student1.name}'s GPA:{gpa_student1:.2f}")
print(f"{student2.name}'s GPA:{gpa_student2:.2f}")


