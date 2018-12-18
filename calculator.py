def addition(number_1, number_2):
    solution = number_1 + number_2
    print "Addition is", solution
    
def substraction(number_1, number_2):
    solution = number_1 - number_2
    print "Substraction is", solution

def multiplication(number_1, number_2):
    solution = number_1 * number_2
    print "Multiplication is", solution

def division(number_1, number2):
    solution =number_1 / number_2
    print "Division is", solution

def again():
    calc_again = raw_input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later BYE BYE...!!!')
    else:
        again()

def calculate():
    print "WELCOME TO CALCULATOR"
    print "Choose operation to perform \n 1. ADDITION \n 2. SUBSTRACTION \n 3. DIVISION \n 4. MULTIPLICATION"
    
    operation_choice = input("opeartion to perform = ") 
    
    if (operation_choice<1 or operation_choice>4 or Exception == NameError) :
        print "WRONG CHOICE, Please see the menu and try again...!!!"
    
    else :
        print "Enter both numbers"
        number_1 = input("Input first number : " )
        number_2 = input("Input second number : ")
            
        if operation_choice==1:
            addition(number_1, number_2)
            again()
        
        elif operation_choice==2:
            substraction(number_1, number_2)
            again()
        
        elif operation_choice==3:
            multiplication(number_1, number_2)
            again()
        
        elif operation_choice==4 :
            division(number_1, number_2)
            again()        
    
        else:
            print "wrong choice"

calculate()
