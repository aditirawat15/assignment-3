from statistics import mean

def seq(terms):
    if terms <= 0: raise ValueError("Please enter a postive no. of terms")
    elif terms == 1 : return [0]
    elif terms == 2 : return [0,1]
    else: 
        seq = [0,1]
        numb = 2 #number of terms calculated
        while(numb < terms) : 
            seq.append(seq[numb - 1] + seq[numb - 2])
            #print(seq)
            numb += 1
        return seq

fib = seq(int(input("Enter number of terms in sequence : ")))
print(fib)
print(round(mean(fib),2))
