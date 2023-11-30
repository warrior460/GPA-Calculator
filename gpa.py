# GPA Calculator
number_of_subjects = 4

subject_names = ['Bangla', 'English', 'Math', 'Science']

# Taking the marks of each subject from the user
subject_marks = []
for i in range(number_of_subjects):
  while True:
    marks = int(input("Enter the marks for " + subject_names[i] +  ": "))
    if marks > 100:
      print("Invalid marks. Marks cannot be greater than 100. Please enter again.")
    else:
      subject_marks.append(marks)
      break

# Calculating the total marks
total_marks = sum(subject_marks)

# Calculating the average marks
average_marks = total_marks / number_of_subjects

# Calculating the GPA
if average_marks >= 91:
    gpa = "A+"
elif average_marks >= 81:
    gpa = "A"
elif average_marks >= 71:
    gpa = "B"
elif average_marks >= 61:
    gpa = "C"
elif average_marks >= 41:
    gpa = "D"
else:
    gpa = "F"

# Displaying the GPA
print("Your GPA is:", gpa)
