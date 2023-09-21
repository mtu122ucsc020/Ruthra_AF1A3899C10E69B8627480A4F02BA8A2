class Student:

  def __init__(self , name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_Students(Student_list):
  # sort the list of Students in descending order of CGPA
  sorted_Students = sorted(Student_list,
                    key=lambda Student: Student.cgpa,
                    reverse=True)
#syntax - Lambda arg:exp
  return sorted_Students


#Example usage:
Students = [
  Student("Swetha", "A123", 7.8),
  Student("Sona", "A124", 8.9),
  Student("Ruthra", "A125", 9.1),
  Student("Surya", "A126", 9.9),
] 

sorted_Student = sort_Students(Students)

#Print the sorted list of Students
for Student in sorted_Student:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(Student.name,Student.roll_number,Student.cgpa))