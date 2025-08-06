#Built a simple calculator using functions

def add (a,b):
    return a + b

def subtract (a,b):
    return a - b 

def  multiply (a,b):
    return a * b 

def  divide (a,b):
    if b == 0:
        return "Sorry cannot complete computation please input a correct number "
    return a / b
def calculator() :
    print("What calculation would you like to do :")
    print("1.For addition \n2.For substraction \n3.For multiplication \n4.For division")

    choice = input("Please choose an option: 1 ,2 ,3 ,4 : ")
    if choice in ('1','2','3','4'):
        try:
            num1    = float(input("Input the first number : "))
            num2 = float(input("Input the second number : "))
            

        except ValueError:
          print ("Please input a valid number")

        if choice == '1' :
            print('Results is :', add(num1, num2))

        elif choice == '2' :
            print ('Results is :', subtract(num1, num2))    

        elif choice == '3' :
            print ('Result is :', multiply(num1,num2))

        elif choice == '4' :
            print ('Result is :', divide(num1,num2))

    else :
        print ('Invalid choice, Please choose a correct number')
         
        
calculator()
        

    


    