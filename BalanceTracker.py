transactionAmounts=[]
transactionTypes=[]
a='Addition'
s='Substraction'
h='History'
i='iInformation'
q='Quit'
def showInfo(valueList,typeList,desiredType):
    print("Transaction Information: ")
    additionCount=0
    substractionCount=0
    for i in range(len(transactionTypes)):
        if transactionTypes[i] == a:
            additionCount+=1

        elif transactionTypes[i] == s:
            substractionCount+=1
        print("Addition count: ", additionCount)
        print("Substraction count: ", substractionCount)

        totalAddition=sum(transactionAmounts[i] for i in range(len(transactionAmounts)) if transactionTypes[i] == a)
        totalSubstraction=sum(transactionAmounts[i] for i in range(len(transactionAmounts)) if transactionTypes[i] == s)
        print("Total addition: ", totalAddition)
        print("Total substraction: ", totalSubstraction)

def balanceTracker():
    print("Welcome to Balance Tracker")
    print("Enter starting balance: ")
    startingBalance = float(input())
    balance=startingBalance
    print("Current balance is : ", balance)
    # transactionAmounts.append(startingBalance)
    
    a='Addition'
    s='Substraction'
    h='History'
    i='iInformation'
    q='Quit'

    while True:
        print("[A]ddition")
        print("[S]ubstraction")
        print("[H]istory")
        print("[I]nformation")
        print("[Q]uit")
        
        choice = input().lower()
        print("> ", choice)

        if choice == 'a':
            addAmount = float(input())
            print("Add to balance: ", addAmount)
            transactionAmounts.append(addAmount)
            balance+=addAmount
            transactionTypes.append(a)
            print("Current balance is: ", balance)
        elif choice == 's':
            subAmount = float(input())
            print("substract from balance:", subAmount)
            transactionAmounts.append(subAmount)
            balance-=subAmount
            transactionTypes.append(s)
            print("Current balance is: ", balance)
        elif choice == 'h':
            print("Transaction History: ")
            print("Starting balance was ", startingBalance)
            for i in range(len(transactionAmounts)):
                print(f"Transaction {i+1} -", transactionTypes[i], f"of", transactionAmounts[i])
        elif choice == 'i':
            showInfo()

            

            

        elif choice == 'q':
            print("Good bye!")
            break

    

balanceTracker()

