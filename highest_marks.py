num_students = int(input("Enter the number of students:"))
name = []
marks = []
for i in range(num_students):
    student_name = input("Enter the name of the student: ")
    mark = float(input("Enter the mark for student: "))
    name.append(student_name)
    marks.append(mark)
highest_marks = max(marks)
print("The highest marks is: ", highest_marks)