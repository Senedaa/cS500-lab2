def main():
    #print program name
    print("CD Calculator")

    # input of the user values
    initial_amt = int(input("Enter the initial investment amount: "))
    apy = float(input("Enter annual percentage yield (APY %): "))
    num_months = int(input("Enter number of months for the CD term: "))
    comp_frequency = input("Enter compounding frequency (monthly, quarterly, annually): ").lower()

    # intializing variables
    cd_values = []
    total_interest = 0

    for month in range(1, num_months + 1):
        # Calculating the monthly interest rates
        if comp_frequency == "monthly":
            monthly_rate = apy / 100 / 12
            periods = month
        elif comp_frequency == "quarterly":
            monthly_rate = apy / 100 / 4
            periods = month // 3
        elif comp_frequency == "annually":
            monthly_rate = apy / 100
            periods = month // 12
        else:
            print("Error, Invalid Compounding Frequency")
            return

        # Calculating CD Value using compound interest
        cd_value = initial_amt * (1 + monthly_rate) ** periods
        cd_values.append(cd_value)

    # showing table
    print("\n{:<6}{:<15}".format("Month", "CD Value"))
    print("{:<6}{:<15}".format("-" * 5, "-" * 12))

    for month in range(1, num_months + 1):
        cd_value = cd_values[month - 1]
        print("{:<6}${:,.2f}".format(month, cd_value))

    # Calculating total interest earned
    total_interest = cd_values[-1] - initial_amt
    print(f"\nTotal interest earned: ${total_interest:,.2f}")

if __name__ == "__main__":
    main()
