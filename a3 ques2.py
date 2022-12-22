day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

#dictionary with months to days in them
dates = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

#if year not in range(1800,2025) or month not in range(0,13) or day>dates[month]: raise ValueError("Please enter a valid date")
#using if elif for conditions
if year not in range(1800,2025): raise ValueError("Please enter a valid date")
elif month not in range(0,13): raise ValueError("Please enter a valid date")
elif day>dates[month]: raise ValueError("Please enter a valid date")

if year % 4 == 0 and (year % 100 != 0 or year%400 == 0): dates[2] = 29
#print(dates[2])

if day == dates[month]:
    day = 1
    if month == 12: 
        month = 1 
        year += 1
    else : month += 1
else:
    day += 1

if day < 10 : day = '0' + str(day)
if month < 10 : month = '0' + str(month)
print('Next Date is ' + str(day) + '/' + str(month) + '/' + str(year))
