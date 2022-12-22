str_input = input("Enter numbers (using ',' or ' 'as separators):")
if (' ' in str_input) : numbers = str_input.split(' ')
elif(',' in str_input) :numbers = str_input.split(',')
#print(numbers)
#numbers2 = []
#for i in numbers: numbers2.append(int(i))

list_final = []
for i in numbers:
    list_final.append((int(i),int(i)**2))

print(list_final)
