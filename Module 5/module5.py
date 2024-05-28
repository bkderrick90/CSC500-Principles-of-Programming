# Part 1: Write a program that uses nested loops to collect data and calculate the average rainfall over a period of
# years. The program should first ask for the number of years. The outer loop will iterate once for each year. The
# inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the
# inches of rainfall for that month. After all iterations, the program should display the number of months, the total
# inches of rainfall, and the average rainfall per month for the entire period.

print("Part 1: Average Rainfall\n")

numYears = 0

while numYears <= 0:
    numYears = int(input("Enter number of years (greater than zero): "))

totalRain = 0

for count in range(numYears):
    for month in range(1, 13):
        if month == 1:
            rainfall = int(input(f"Enter rainfall for January of year {count+1}: "))
            totalRain += rainfall
        elif month == 2:
            rainfall = int(input(f"Enter rainfall for February of year {count+1}: "))
            totalRain += rainfall
        elif month == 3:
            rainfall = int(input(f"Enter rainfall for March of year {count+1}: "))
            totalRain += rainfall
        elif month == 4:
            rainfall = int(input(f"Enter rainfall for April of year {count+1}: "))
            totalRain += rainfall
        elif month == 5:
            rainfall = int(input(f"Enter rainfall for May of year {count+1}: "))
            totalRain += rainfall
        elif month == 6:
            rainfall = int(input(f"Enter rainfall for June of year {count+1}: "))
            totalRain += rainfall
        elif month == 7:
            rainfall = int(input(f"Enter rainfall for July of year {count+1}: "))
            totalRain += rainfall
        elif month == 8:
            rainfall = int(input(f"Enter rainfall for August of year {count+1}: "))
            totalRain += rainfall
        elif month == 9:
            rainfall = int(input(f"Enter rainfall for September of year {count+1}: "))
            totalRain += rainfall
        elif month == 10:
            rainfall = int(input(f"Enter rainfall for October of year {count+1}: "))
            totalRain += rainfall
        elif month == 11:
            rainfall = int(input(f"Enter rainfall for November of year {count+1}: "))
            totalRain += rainfall
        elif month == 12:
            rainfall = int(input(f"Enter rainfall for December of year {count+1}: "))
            totalRain += rainfall

numMonths = numYears * 12
averageRain = totalRain / numMonths

print(f"\nThe total rainfall across {numMonths} months was: {totalRain} inches")
print(f"The average rainfall across {numMonths} months was: {averageRain} inches\n")

# Part 2: The CSU Global Bookstore has a book club that awards points to its students based on the number of books
# purchased each month. The points are awarded as follows:
#
#     If a customer purchases 0 books, they earn 0 points.
#     If a customer purchases 2 books, they earn 5 points.
#     If a customer purchases 4 books, they earn 15 points.
#     If a customer purchases 6 books, they earn 30 points.
#     If a customer purchases 8 or more books, they earn 60 points.
#
# Write a program that asks the user to enter the number of books that they have purchased this month and then display
# the number of points awarded.

print("Part 2: CSU Global Book Club Points\n")

numBooks = int(input("How many books have you purchased this month: "))

if numBooks <= 0:
    print("You have earned 0 points this month.")
elif numBooks <= 2:
    print("You have earned 5 points this month.")
elif numBooks <= 4:
    print("You have earned 15 points this month.")
elif numBooks <= 6:
    print("You have earned 30 points this month.")
elif numBooks >= 7:
    print("You have earned 60 points this month.")
