import json


with open("studebts.json",'r') as file:
    data=json.load(file)

students=data["students"]


def avg_marks(marks_list):
    avg=0
    for m in marks_list["marks"]:
        avg+=int(m)

    #marks_list["average"]= avg/len(marks_list["marks"])
    s["avg"]=(avg / len(marks_list["marks"]))

def grade(avg_list):
    avg=avg_list["avg"]

    if avg >= 80:
        avg_list["grade"] = "A"
    elif avg >= 60:
        avg_list["grade"] = "B"
    elif avg >= 40:
        avg_list["grade"] = "C"
    else:
        avg_list["grade"] = "F"

def gen_report(student):
    total_student=len(student)
    failed_students = 0
    topper = students[0]

    for student in students:
        if student["grade"] == "F":
            failed_students += 1

        if student["average"] > topper["average"]:
            topper = student

    print("----- REPORT -----")
    print("Total students:", total_student)
    print("Failed students:", failed_students)
    print("Topper:", topper["name"])
    print("Topper Average:", f"{topper['average']:.2f}")

for s in students:
    avg_marks(s)
    grade(s)


gen_report(students)