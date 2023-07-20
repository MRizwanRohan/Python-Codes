print('******* MINI CALCULATOR *******')
print('')
num1=float(input("enter 1st number = "))
num2=float(input("enter 2nd number = "))
print('')
print("##########################\nFor addition press '+' \nfor subtraction press '-' \nfor multiplication press '*' \nfor division press '/' \n##########################\n")

choice = input("enter what you want to do = ")
print("")

if choice == "+":
    print("ans is ",num1+num2)
elif choice == "-":
    print("ans is ",num1 - num2)
elif choice == "*":
    print("ans is ",num1*num2)
elif choice == "/":
    print("ans is ",num1/num2)
else: print('ERROR')