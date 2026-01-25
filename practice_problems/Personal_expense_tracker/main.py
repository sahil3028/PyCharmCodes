import json

with open("personalData.json",'r') as file:
    data=json.load(file)

perD=data.get("personalData",[])

def report(perdata):
    total=0
    for a in perdata:
        total+=a["amount"]
    print("The total money spent: ",total)

    print("Category wise expenditure")
    cat_exp = {}

    for c in perdata:
        if c["category"] in cat_exp:
            cat_exp[c["category"]] += c["amount"]
        else:
            cat_exp[c["category"]] = c["amount"]

    for key,val in cat_exp.items():
        print(key," = ",val)

    high=0;highTitle=""
    for h in perdata:
        if high<h["amount"]:
            high=h["amount"]
            highTitle=h["title"]
    print("the hight expenditure is: ",highTitle," of ",high)

    print("The avg expenditure is: ", total/len(perdata))
    return
def save_file(allData):
    data= {"personalData": allData}
    with open("personalData.json",'w') as file:
        json.dump(data,file,indent=4)
while True:
    ch=int(input("CHOICES:\n1 Add Expense\n2. View all Expenses\n3. View Report\n 4. exit and save"))

    match ch:
        case 1:
            title=input("enter the title")
            while True:
                try:
                    date=input("enter date").split("-")
                    if int(date[0])<1000:
                        raise ValueError("year must be 4 digits")
                    elif 12<=int(date[1])<0:
                        raise ValueError("Month must be between 1-12")
                    elif 31<=int(date[2])<0:
                        raise ValueError("there are only 30 or 31 days!")
                    else :
                        break
                except ValueError as e:
                    print("invalid date:",e)
                    continue
            while True:
                try:
                    amt=int(input("Enter the Amount "))
                    if amt<0:
                        raise ValueError("amount cant be negative")
                    else:
                        break

                except ValueError:
                    print("amount error: ",ValueError)
                    continue
            while True:
                try:
                    cat=input("enter the Category")
                    if len(cat)==0:
                        raise ValueError("Can't be Empty")
                    else:
                        break
                except ValueError:
                    print("Category Error: ",ValueError)
                    continue

            personaldata={
                    "title": title,
                    "amount": amt,
                    "category": cat,
                    "date": date[0]+"-"+date[1]+"-"+date[2]
                }
            perD.append(personaldata)
        case 2:
            print("Your all expenses are: \n")
            for exp in perD:
                print(f"-->{exp["title"]} of {exp["amount"]}\n")

        case 3:
            print("REPORT--")
            report(perD)
        case 4:
            save_file(perD)
            break