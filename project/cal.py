# basic calculator project
bool=True
while(bool==True):
    print("Enter your number's")
    num1=int(input("Enter your first number "))
    num2=int(input("Enter your second number "))
    print("Enter your options \n 1. Add \n 2. Substrate \n 3. Multiple \n 4. Divide ")
    option=input("Enter your options " )
    if option == "1":
        print(num1+num2)
    elif option=="2":
        print(num1-num2)
    elif option=="3":
        print(num1*num2)
    elif option=="4":
        print(num1/num2)
    else:
        print("wrong option")
        bool=False
            

