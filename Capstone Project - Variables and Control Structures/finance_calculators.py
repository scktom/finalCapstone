""""
I create the code in Visual Studio Community 2019
Version: 16.11.25
Python version: 3.9.13

I need to show only two decimal numbers in £
I found the round function on the Internet:
https://www.w3schools.com/python/ref_func_round.asp
"""
import math

#I write the message to the output, after I wait for the lowercase type command from the user
message = '''
investment \t - to calculate the amount of interest you'll earn on your investment \n
bond \t \t - to calculate the amount you'll have to pay on a home loan
'''
print(message)

command = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#I check the input is correct command or not
if command == "investment":
    #If the user choosed the investment command after I ask on the input:
    #deposit (decimal number)
    #interest_rate (integer number),
    #rate (decimal number) I convert integer number to decimal number (8% = 0.08)
    #year (integer number)
    #interest (string)
    deposit = float(input("Please enter the amount of money that you are depositing(£): "))
    interest_rate = int(input("Please enter the interest rate for one year(%): "))
    rate = interest_rate / 100
    year = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please choose from the following ones 'simple' or 'compound': ").lower()

    #I write the selected simple or compound interest value on the output
    if interest == "simple":
        simple_interest = round(deposit * (1+rate*year), 2)
        print(f"Simple interest for {year} year with {interest_rate}% rate = £{simple_interest}")
    elif interest == "compound":
        compound_interest = round(deposit * math.pow((1+rate), year), 2)
        print(f"Compound interest for {year} year with {interest_rate}% rate = £{compound_interest}")
    else:
        print("It's not valid word. Please write 'simple' or 'compound' word")


elif command == "bond":
    #If the user choosed the bond command after I ask on the input:
    #house_value (decimal number)
    #interest_rate (integer number)
    #monthly rate (decimal number) I convert integer number to decimal number (8% = 0.08) 
    #month_number (integer number)
    house_value = float(input("Please enter the present value of the house(£): "))
    interest_rate = int(input("Please enter the interest rate for one year(%): "))
    monthly_rate = (interest_rate / 100) / 12
    month_number = int(input("The number of months they plan to take to repay the bond: "))

    #I write the bond repayment value on the output
    repayment = round((monthly_rate*house_value)/(1-(1+monthly_rate)**(-month_number)), 2)
    print(f"You will pay £{repayment} monthly for {month_number} months")

else:
    print("It's not valid word. Please write 'investment' or 'bond' word")