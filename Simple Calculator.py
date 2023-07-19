num1= float(input('enter 1st number ='))
num2= float(input('enter 2nd number ='))

print("press 1 for addition, 2 for substruction, 3 for multiply, 4 for division")

choice=int(input('press between 1-4 = '))

if choice==1:
    print('sum= ',num1+num2)

elif choice==2:
    print('sub= ', num1 - num2)

elif choice==3:
    print('multi= ', num1 * num2)

elif choice==4:
    print('div= ', num1/num2)

else:print("Something went wrong")