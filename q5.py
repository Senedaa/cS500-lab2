def rectangle_of_symbols(height,width,symbol):
     while height > 0:
        for j in range(1, width + 1):
            print(symbol, end='')
        print()
        height -= 1

def main():
    #print the program name
    print("Shape of Rectangle with symbols")
    
    #input of the users
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))
    symbol = input("Enter symbol: ")
    #calling the function

    rectangle_of_symbols(height,width,symbol)

if __name__ == "__main__":
    main()