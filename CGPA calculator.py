print("✦ CGPA Calculator ✦")

# Grade dictionary (5-point scale)
grade_dict = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

# Number of courses
while True:
    try:
        course_num = int(input("How many courses are you taking: "))
        if course_num > 0:
            break
        print("Enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

# Course names (comma separated), strip stray spaces
while True:
    courses = input("What are they (list with commas): ")
    courses_list = [c.strip().upper() for c in courses.split(",") if c.strip()]
    if len(courses_list) == course_num:
        break
    print(f"You said {course_num} courses but listed {len(courses_list)}. Try again.")

# Course units (space separated)
while True:
    try:
        course_unit_list = [int(x) for x in input("What are their course units (list with spaces): ").replace(",", " ").split()]
        if len(course_unit_list) == course_num:
            break
        print(f"Enter exactly {course_num} units.")
    except ValueError:
        print("Units must be whole numbers.")

# Total course units
total_units = sum(course_unit_list)

# Grades (space separated, same order as the courses)
while True:
    grades_list = input("What are your grades for each (list with spaces, e.g. A B C): ").upper().replace(",", " ").split()
    if len(grades_list) != course_num:
        print(f"Enter exactly {course_num} grades.")
    elif any(g not in grade_dict for g in grades_list):
        print("Grade is non existent. Use only A, B, C, D, E or F.")
    else:
        break

# Calculate total quality points (unit x grade point for each course)
quality_points = sum(unit * grade_dict[g] for unit, g in zip(course_unit_list, grades_list))

# Calculate GPA
gpa = quality_points / total_units

# Results
print("\n--- Result Summary ---")
print(f"{'Course':<10}{'Unit':<6}{'Grade':<7}{'Points':<7}")
for course, unit, g in zip(courses_list, course_unit_list, grades_list):
    print(f"{course:<10}{unit:<6}{g:<7}{unit * grade_dict[g]:<7}")

print(f"\nTotal units: {total_units}")
print(f"Total quality points: {quality_points}")
print(f"GPA: {gpa:.2f}")