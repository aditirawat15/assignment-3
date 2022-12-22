a = {4:['D','Poor'], 5:('C','Below Average'), 6:('C+','Average'), 7:('B','Good'), 8:('B+','Very Good'), 9:('A','Excellent'), 10:('A+','Outstanding')}

grade = int(input('Grade : '))
if grade >= 4 and grade <= 10:
    print('Your Grade is',a[grade][0], 'and', a[grade][1], 'Performance.')
else: raise ValueError("Grade invalid")
