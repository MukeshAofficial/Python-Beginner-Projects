def add(a,b):
    return a+b 

def sub(a,b):
    return a-b 

def multi(a,b):
    return a*b 

def divide(a,b):
    if b!=0:
        return a/b 
    else: 
        return "Error Division by zero"

def main():
    while True:
        print('\n simple calculator')
        print('1.Add')
        print('2.Subtraction')
        print('3.Multiply')
        print('4.Division')
        print('5.Exit')


        choice=input('Enter Your choice:')
        if choice in ['1','2','3','4']:
            num1=float(input('Enter First number:'))
            num2=float(input('Enter second numebr:'))


            if choice=='1':
                print(f'results {add(num1,num2)} ')
            elif choice=='2':
                print(f'results {sub(num1,num2)}')
            elif choice=='3':
                print(f'results  {multi(num1,num2)}')
            elif choice=='4':
                print(f'results {divide(num1,num2)}')
            else:
                print("Goodbye!")
                break
        else:
            print("Invalid choice, please try again.")

main()