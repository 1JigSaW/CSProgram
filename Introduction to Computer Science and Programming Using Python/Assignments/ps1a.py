total_cost = float(input('Enter the cost of your dream home: '))
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04

current_savings = 0
month = 0
while current_savings <= portion_down_payment:
	current_savings += current_savings*(r/12)
	current_savings += annual_salary / 12*portion_saved
	month += 1
print(f'Number of months: {month}')