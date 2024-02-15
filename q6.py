def triangle_of_symbols(height,symbol):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        triangle_line = spaces + symbol * (2 * i - 1)
        print(triangle_line)

def main():
    #print the program name
    print("Shape of traingle with symbols")
    
    #input of the users
    height = int(input("Enter the height: "))
    symbol = input("Enter symbol: ")
    #calling function
    triangle_of_symbols(height,symbol)
    

if __name__ == "__main__":
    main()