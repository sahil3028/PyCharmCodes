import json

with open("shows.json", 'r') as file:
    data = json.load(file)

shows = data.get("shows", [])
report = data.get("report",[])


def tryagain():
    c = input("Go Back press(B) or Try again press(T): ")
    if c == "B" or c == "b":
        return False
    elif c == "T" or c == "t":
        return True
    else:
        print("Invalid choice, going back")
        return False


def view_shows():
    for s in shows:
        print(
            s["show_id"], "-->", s["movie"],
            "| Screen:", s["screen"],
            "| Time:", s["time"],
            "| Available:", s["available_seats"]
        )


def book():
    while True:
        try:
            id = int(input("Enter movie id: "))
            break
        except ValueError:
            print("Enter valid id")
            if not tryagain():
                return

    for s in shows:
        if id == s["show_id"]:
            try:
                num = int(input("Enter number of seats: "))
            except ValueError:
                print("Invalid seat count")
                return

            if num <= s["available_seats"]:
                s["available_seats"] -= num
                s["booked"] += num
                print("Your total is", num * s["price"], "THANKS!!")
            else:
                print("We don't have enough seats!!")
            return

    print("WE ARE NOT SCREENING THAT SHOW")


def cancel():
    while True:
        try:
            id = int(input("Enter movie id: "))
            break
        except ValueError:
            print("Enter valid id")
            if not tryagain():
                return

    for s in shows:
        if id == s["show_id"]:
            try:
                num = int(input("Enter number of seats to cancel: "))
            except ValueError:
                print("Invalid seat count")
                return

            if num <= s["booked"]:
                s["available_seats"] += num
                s["booked"] -= num
                print("Your total refund is", num * s["price"], "THANKS!!")
            else:
                print("We NEVER booked that many seats!!")
            return

    print("WE ARE NOT SCREENING THAT SHOW")


def search():
    try:
        choice = int(input(
            "\nSearch options\n"
            "1. By Name\n"
            "2. By Time\n"
            "3. By Screen\n"
            "Choose: "
        ))
    except ValueError:
        print("Invalid choice")
        return

    match choice:
        case 1:
            n = input("Enter movie name: ")
            for s in shows:
                if s["movie"].lower() == n.lower():
                    print(s["show_id"], "-->", s["movie"], "Screen:", s["screen"], "Time:", s["time"])

        case 2:
            n = input("Enter time (HH:MM): ")
            for s in shows:
                if s["time"] == n:
                    print(s["show_id"], "-->", s["movie"], "Screen:", s["screen"], "Time:", s["time"])

        case 3:
            try:
                n = int(input("Enter screen number: "))
            except ValueError:
                print("Invalid screen number")
                return

            for s in shows:
                if s["screen"] == n:
                    print(s["show_id"], "-->", s["movie"], "Screen:", s["screen"], "Time:", s["time"])

        case _:
            print("Invalid choice")


def movie_report():
    report["total_shows"] = len(shows)
    report["tickets_sold"] = 0
    report["total_revenue"] = 0
    report["fully_booked"] = []
    mostBook = 0
    report["most_booked"] = "none"

    for s in shows:
        report["tickets_sold"] += s["booked"]
        report["total_revenue"] += s["booked"] * s["price"]

        if s["booked"] > mostBook:
            mostBook = s["booked"]
            report["most_booked"] = s["movie"]

        if s["available_seats"] == 0:
            report["fully_booked"].append(s["movie"])

    print(report)


def save():
    data = {"shows": shows, "report": report}
    with open("shows.json", 'w') as file:
        json.dump(data, file, indent=4)


while True:
    try:
        choice = int(input("\nBook Your Show\n""1. View all shows\n""2. Book tickets\n""3. Cancel tickets\n""4. Search show\n""5. Generate report\n""6. Save and Exit\n""Choose: "))
    except ValueError:
        print("Invalid input")
        continue

    match choice:
        case 1:
            view_shows()
        case 2:
            book()
        case 3:
            cancel()
        case 4:
            search()
        case 5:
            movie_report()
        case 6:
            save()
            print("Closing...")
            break
        case _:
            print("Invalid choice")