print("Welcome to Tip Calculator v1.0!\nLet me help you calculate how much you will pay\n.")

total_bill = float(input('What was the total bill? '))
tip_percent = float(input('What percentage tip would you like to give? 10, 12, or 15? '))/100
num_people = float(input('How many people to split the bill? '))

raw_bill_per_person = total_bill / num_people
tip = round(raw_bill_per_person + (raw_bill_per_person * tip_percent), 2)

print(f"Each person should pay: ${tip}")
