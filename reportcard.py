

name = input("Enter Student Name: ")

num_subjects = int(input("Enter number of subjects: "))

subjects = []
marks_list = []

total = 0

def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
for i in range(num_subjects):
    print(f"\nSubject {i + 1}")
    subject = input("Enter Subject Name: ")
    marks = float(input("Enter Marks (out of 100): "))

    subjects.append(subject)
    marks_list.append(marks)
    total += marks


percentage = total / num_subjects
cgpa = percentage / 9.5

overall_grade = get_grade(percentage)


print("\n")
print("=" * 45)
print("              REPORT CARD")
print("=" * 45)

print(f"Student Name : {name}\n")

print("{:<20} {:<10} {:<10}".format("Subject", "Marks", "Grade"))
print("-" * 45)

for i in range(num_subjects):
    grade = get_grade(marks_list[i])
    print("{:<20} {:<10} {:<10}".format(subjects[i], marks_list[i], grade))

print("-" * 45)
print(f"Total Score : {total:.2f} / {num_subjects * 100}")
print(f"Percentage : {percentage:.2f}%")
print(f"CGPA       : {cgpa:.2f} / 10")
print(f"Overall Grade : {overall_grade}")
print("=" * 45)