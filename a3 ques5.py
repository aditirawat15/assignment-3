from math import ceil
str1 = "ABCDEFGHIJK" #any odd numbered string can work here
for i in range(ceil(len(str1)/2)): print(' '*i + str1[0:(len(str1)-i*2)])
