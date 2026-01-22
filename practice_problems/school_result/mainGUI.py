import json
import FreeSimpleGUI as sg

# ---------------- DATA LOAD ----------------

try:
    with open("students.json", "r") as file:
        data = json.load(file)
        students = data.get("students", [])
except FileNotFoundError:
    students = []

# ---------------- LOGIC FUNCTIONS ----------------

def avg_marks(marks_list):
    return sum(marks_list) / len(marks_list)


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
    if not student_list:
        return "No students available."

    total_students = len(student_list)
    failed_students = sum(1 for s in student_list if s["grade"] == "F")
    topper = max(student_list, key=lambda s: s["average"])

    report = (
        "----- REPORT -----\n"
        f"Total students: {total_students}\n"
        f"Failed students: {failed_students}\n"
        f"Topper: {topper['name']}\n"
        f"Topper Average: {topper['average']:.2f}"
    )
    return report


def save_to_json(students):
    with open("students.json", "w") as file:
        json.dump({"students": students}, file, indent=4)

# ---------------- GUI LAYOUT ----------------

layout = [
    [sg.Text("Student Performance Tracker", font=("Arial", 16))],

    [sg.Text("Student Name"), sg.Input(key="-NAME-")],

    [sg.Text("Marks (3 subjects)")],
    [
        sg.Input(key="-M1-", size=(5, 1)),
        sg.Input(key="-M2-", size=(5, 1)),
        sg.Input(key="-M3-", size=(5, 1))
    ],

    [sg.Button("Add Student"), sg.Button("Save & View Report"), sg.Button("Exit")],

    [sg.Multiline(size=(45, 10), key="-OUTPUT-", disabled=True)]
]

window = sg.Window("Student Tracker", layout)

# ---------------- EVENT LOOP ----------------

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    if event == "Add Student":
        name = values["-NAME-"].strip()

        if not name:
            sg.popup("Name cannot be empty")
            continue

        try:
            marks = [
                int(values["-M1-"]),
                int(values["-M2-"]),
                int(values["-M3-"])
            ]
        except ValueError:
            sg.popup("Marks must be numbers")
            continue

        if not all(0 <= m <= 100 for m in marks):
            sg.popup("Marks must be between 0 and 100")
            continue

        avg = avg_marks(marks)
        grade = grade_calc(avg)

        students.append({
            "name": name,
            "marks": marks,
            "average": avg,
            "grade": grade
        })

        window["-OUTPUT-"].update(f"Student '{name}' added successfully.\n", append=True)

        window["-NAME-"].update("")
        window["-M1-"].update("")
        window["-M2-"].update("")
        window["-M3-"].update("")

    if event == "Save & View Report":
        save_to_json(students)
        report = gen_report(students)
        window["-OUTPUT-"].update(report + "\n")

window.close()