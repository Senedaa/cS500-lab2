def circle_of_symbols(radius, symbol):
    #drawing circle using Bresenham’s circle drawing algorithm
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()

def main():
    #print the program name
    print("Shape of Circle with symbols")
    print()
    #user inputs
    radius = int(input("Enter the radius of the circle: "))
    symbol = input("Enter the symbol character: ")
    
    #calling the function
    circle_of_symbols(radius, symbol)

if __name__ == "__main__":
    main()