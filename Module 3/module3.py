# Part 1: Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts
# with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

# Function to calculate the total price
def calculate_total_bill(order):
    subtotal = 0
    for item_cost in order:
        subtotal += item_cost
    tax = subtotal * .07
    print("Tax: $", round(tax, 2))
    tip = subtotal * .18
    print("Tip: $", round(tip, 2))
    total = subtotal + tax + tip
    return round(total, 2)

# Initiate an empty array
order = []
more_items = True
item_number = 1

# Get the cost of each item ordered using a while loop
while more_items:
    order.append(float(input(f"Enter the cost of item {item_number}: ")))
    response = input("Do you have more items to enter? (Y or N): ").strip().upper()
    if response == "N":
        more_items = False
    elif response == "Y":
        more_items = True
    item_number += 1

# Perform calculation using calculate_total_bill function
order_total = calculate_total_bill(order)
print("Your total bill is $", order_total)

# Part 2: Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a
# Python program to solve the general version of the above problem. Ask the user for the time now
# (in hours) and then ask for the number of hours to wait for the alarm. Your program should output
# what the time will be on a 24-hour clock when the alarm goes off.

# Function to calculate the alarm time using an array
def calculate_alarm_time(current_time, wait_hours):
    hours_in_day = 24
    clock = list(range(hours_in_day))
    alarm_time = (current_time + wait_hours) % hours_in_day
    return clock[alarm_time]

# Get the current time from the user
current_time = int(input("Enter the current time (in hours, 0-23): "))

# Get the number of hours to wait for the alarm
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = calculate_alarm_time(current_time, wait_hours)

print(f"The alarm will go off at {alarm_time}:00.")
