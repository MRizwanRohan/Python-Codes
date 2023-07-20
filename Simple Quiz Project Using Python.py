print('****** WELCOME TO QUIZ ******')
print('')
ans= input('Do you want to play quick QUIZ? YES or NO?\n')

if ans.lower()=="no":
    print("OK BYE")
if ans.lower()=="yes":
    print("OK, let's start :)")

    print("")
    print("###########################")

    print("QUS no 1")
    num1= input("What is CPU?\n")
    if num1.lower()=="central processing unit":
        print("Correct :)")
    else:print("Incorrect")

    print('')
    print("QUS no 2")
    num2= input("What is HTML?\n")
    if num2.lower()=="hyper text transfer protocol":
        print("Correct :)")
    else:print("Incorrect")

    print('')
    print("QUS no 3")
    num3= input("Is HTML a programming?\n")
    if num3.lower()=="no":
        print("Correct :)")
    else:print("Incorrect")

    print('')
    print("QUS no 4")
    num4= input("What is 4+2?\n")
    if num4== "6":
        print("Correct :)")
    else:print("Incorrect")