import json


with open("students.json", 'r') as file:
    data=json.load(file)

students=data["students"]


def avg_marks(marks_list):
    total=0
    for m in marks_list:
        total+=int(m)
    return total / len(marks_list)

def grade_calc(avg):

    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

def gen_report(student_list):
    total_student=len(student)
    failed_students = 0
    topper = students[0]

    for s in student_list:
        if s["grade"] == "F":
            failed_students += 1

        if s["average"] > topper["average"]:
            topper = student

    print("----- REPORT -----")
    print("Total students:", total_student)
    print("Failed students:", failed_students)
    print("Topper:", topper["name"])
    print("Topper Average:", f"{topper['average']:.2f}")

# for s in students:
#     avg_marks(s)
#     grade(s)
#
#
# gen_report(students)
def save_to_json(students):
    data = {"students": students}
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

while True:
    print("choose:\n1. Add a student\n2. save and view report\n:3 exit")
    try:
        ch=int(input("Enter your choice: "))
    except ValueError:
        print("enter a number from the list")
        continue

    match ch:
        case 1:
            while True:
                name=input("write students name (""exit"")if you wanna stop")
                if name.lower()=="exit":
                    break
                marks=[]
                for i in range (3):
                    while True:
                        print(f"enter marks for the sub {i+1}")
                        try:
                            m=int(input())
                            if 0<=m<=100:
                                marks.append(m)
                                break
                            else:
                                print("enter between 0 to 100")
                        except ValueError:
                            print("enter a proper no")

                avg=avg_marks(marks)
                grade=grade_calc(avg)

                student = {
                "name": name,
                "marks": marks,
                "average": avg,
                "grade": grade
                }
                students.append(student)

        case 2:
            gen_report(students)
            save_to_json(students)

        case 3:
            print("exitt")
            break
        case _:
            print("invalid choice")