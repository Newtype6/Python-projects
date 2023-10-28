# Project 2

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? £"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))


tip_amount = tip_percent / 100 * total_bill
new_total_bill = total_bill + tip_amount
per_person = round(new_total_bill / people, 2)
per_person = "{:.2f}".format(per_person)

print(f"Each person should pay: £{per_person}")
