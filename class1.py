def abc(func):
    print("1.Pizza")
    print("2.Burger")
    print("3.Sendwich")

    def menu():
        choice = int(input("Enter The Choice : "))

        if(choice==1):
            print("As Per Your Choice Pizza...!")
            print("4.Margerita")
            print("5.7Cheese")
            print("6.Chilly")
            p = int(input("Enter Number For Pizza : "))

            if(p==4):
                print("Your Order Is Margerita Pizza")
            elif(p==5):
                print("Your Order Is 7Cheese Pizza")
            elif(p==6):
                print("Your Order Is Chilly Pizza")
            else:
                print("Please Enter Valid Number...!")
                exit()

        elif(choice==2):
            print("As Per Your Choice Burger...!")
            print("7.Veg Burger")
            print("8.Cheese Burger")
            print("9.Chilly Burger")

            b = int(input("Enter Number For Burger :"))

            if(b==7):
                print("Your Order Is Veg Burger")
            elif(b==8):
                print("Your Order Is Cheese Burger")
            elif(b==9):
                print("Your Order Is Chilly Burger")
            else:
                print("Please Enter Valid Number...!")
                exit()
        
        elif(choice==3):
            print("As Per Your Choice Sendwich...!")
            print("10.Veg Sandwich")
            print("11.Cheese Sandwich")
            print("12.Grill Sandwich")

            s = int(input("Enter Number For Sandwich :"))

            if(s==10):
                print("Your Order Is Veg Sandwich")
            elif(s==11):
                print("Your Order Is Cheese Sandwich")
            elif(s==12):
                print("Your Order Is Grill Sandwich")
            else:
                print("Please Enter Valid Number...!")
                exit()

        else:
            print("Please Enter Valid Number...!")
            exit()
            
        func()             
    return menu

@abc
def xyz():
    print("Thank You...!")
xyz()    

