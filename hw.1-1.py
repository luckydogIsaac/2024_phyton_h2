# Import the 'calendar' module
import calendar

# Prompt the user to input the year and month
y = int(input("Input the year : "))
m = int(input("Input the month : "))

# Print the calendar for the specified year and month
print(calendar.month(y, m))
