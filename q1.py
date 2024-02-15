def main():
    #print the program name
    print("Simple Calculator")
    #input the numbers
    while True:

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        opr = input("Enter operation sign: ")
        error_message = None

        if opr == '+':
            result = num1 + num2
        elif opr == '-':
            result = num1 - num2
        elif opr == '*':
            result = num1 * num2
        elif opr == '/':
            if num2 == 0:
                error_message= "Error, divide by zero!"
            else:
                result = num1 /num2 
        else:
            error_message = "Error,Invalid Operator"

        if error_message is None:
            print("The result is", result)
        else:
            print(error_message)
        
        confirm = input("Do you want to start again (y/n)?")
        if confirm.lower() != 'y':
            break

if __name__ == "__main__":
    main()