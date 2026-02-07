import json

with open ("accounts.json",'r')as file:
    data=json.load(file)

accounts=data.get("accounts",[])

def create_account():
    accNos=[int(no["account_no"]) for no in accounts]
    name=input("whats your name: ")

    while True:
        accNo=int(input("enter your account number"))
        if accNo in accNos:
            print("The acc no already exists")
            continue
        else:
            break

    while True:
        acctype=input("whats your account type ('savings'/'current')?")
        if acctype =="savings" or acctype=="current":
            break
        else:
            print("enter properly: ")
            continue

    initialBalance=int(input("enter the initial balance: "))

    account={
  "account_no": accNo,
  "name": name,
  "balance": initialBalance,
  "account_type": acctype,
  "transactions": [
    {"type": "deposit", "amount": initialBalance}
  ]
}
    accounts.append(account)

def view_accounts(account=accounts):
    for acc in account:
        print("acc no\t\tacc name\n",acc["account_no"],"\t\t",acc["name"],"\n")

def deposit():
    accNo=int(input("Enter your account number: "))
    for acc in accounts:
        if accNo==acc["account_no"]:
            amt=int(input("Enter the amount you wanna deposit: "))
            depo= {"type": "deposit", "amount": amt}
            acc["balance"]+=amt
            acc["transactions"].append(depo)
            return
    print("No account Exist with that Account Number.")

def withdraw():
    accNo = int(input("Enter your account number: "))
    for acc in accounts:
        if accNo == acc["account_no"]:
            amt = int(input("Enter the amount you wanna withdraw: "))
            if amt>acc["balance"]:
                print("Insufficient Balance 'gareeb'  ",acc["balance"]," only left")
                return
            depo = {"type": "withdraw", "amount": amt}
            acc["balance"]-=amt
            acc["transactions"].append(depo)
            return
    print("No account Exist with that Account Number.")

def account_statement():
    accNo = int(input("Enter your account number: "))
    for acc in accounts:
        if accNo == acc["account_no"]:
            print("acc no\tacc name\taccount type\n", acc["account_no"], "\t", acc["name"],"\t",acc["account_type"], "\n")
            print("\n\t\tTransactions: \n\ttype\tamount\n\t")
            for t in acc["transactions"]:
                print(t["type"],"\t",t["amount"],"\n\t")
            return
    print("No account Exist with that Account Number.")

def bank_report():
    totalAcc=0;totalMoney=0;highestBalance=[{'balance':0}];zeroAcc=[]
    for acc in accounts:
        totalAcc+=1
        totalMoney+=acc["balance"]
        if highestBalance[0]["balance"] <acc["balance"]:
            highestBalance[0]=acc
        if acc["balance"]==0:
            zeroAcc.append(acc)
    print("\tTotal no of accounts: ",totalAcc,"\n Total money in bank: ",totalMoney)
    print("\nAccount with highest balance : ")
    view_accounts(account=highestBalance)
    print("\n Accounts with zero balance :\n")
    view_accounts(account=zeroAcc)

def save_file():
    data={"accounts":accounts}
    with open("accounts.json",'w')as file:
        json.dump(data,file,indent=4)

while True:
    ch=int(input("\t\tMENU\n1. Create account\n2. View all accounts\n3. Deposit money\n4. Withdraw money\n5. View account statement\n6. Generate bank report\n7. Save & Exit"))
    match ch:
        case 1:
            print("\n\n")
            create_account()
        case 2:
            print("\n\n")
            view_accounts()
        case 3:
            print("\n\n")
            deposit()
        case 4:
            print("\n\n")
            withdraw()
        case 5:
            print("\n\n")
            account_statement()
        case 6:
            bank_report();            print("\n\n")

        case 7:
            save_file()
            print("EXITING...")
            break