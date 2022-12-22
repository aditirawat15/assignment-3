#predefined sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
#part a)
#A = Set1.union(Set2) - Set1.intersection(Set2)
A = Set1^Set2
print(A)

#part b)
#print((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
#print(Set1|Set2|Set3)
B = (Set1|Set2|Set3) - ((Set1&Set2) | (Set2&Set3) | (Set3&Set1))
print(B)

#part c)
C = (Set1&Set2) | (Set2&Set3) | (Set3&Set1)
print(C)

#part d)
D = set()
for i in range (1,11) : 
    if i not in Set1:  D.add(i) 
print(D)

#part e)
E = set()
for i in range (1,11) : 
    if i not in Set1|Set2|Set3:  
        #print(i)
        E.add(i) 
print(E)
