print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))   

bill_total = bill + (bill * tip / 100)
individual_amount = bill_total / people
roundup_amount = round(individual_amount, 2)

print(f"Each person should pay: ${roundup_amount}")