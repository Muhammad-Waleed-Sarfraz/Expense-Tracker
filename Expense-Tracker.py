Expense = []
Cost = 0
while True:
    print("1. Add your Item \n2. Remove an Item \n3. View Your Draft \n4. Quit")
    choice = input("What You Want to Do (1/2/3/4) = ")
    if choice in ["1","2","3","4"]:
        if (choice == "1"):
            item = input("Which item you want to add : ")
            price = float(input("What is the price of the item = "))
            Cost += price
            Expense.append(f"{item}: {price}")
            print("------Successfully Added------")
        elif(choice == "2"):
            item = input("Which item you want to remove : ")
            price = float(input("Price of the item you want to remove : "))
            Cost -= price
            Expense.remove(f"{item}: {price}")
            print("------Successfully Removed------")
        elif(choice == "3"):
            print("-----Your Receipt-----")
            for item in Expense:
                print(item)
            print(f"Total Spend : {Cost}")
        elif(choice == "4"):
            print("----Quit Successfully----")
            break
        else:
            print("----Invalid Choice----")
            


print("----Thank You----")