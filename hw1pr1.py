
pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]
#Problem 0 create the list [2, 7, 5, 9]
answer0 = e[:2] + pi[4:]
print(answer0)

# Problem 1: creating [7, 1]
answer1 =   e[1:3]          
print(answer1)

# Problem 2:create the list [9, 1, 1]
answer2 =   pi[5:0:-2]          
print(answer2)


# Problem 3: create the list [1, 4, 1, 5, 9]
answer3 =   pi[1:]          
print(answer3)


# Problem 4: create the list [1, 2, 3, 4, 5]
answer4 = e[-1::-2] + pi[::2]     
print(answer4)



h = 'harvey'
m = 'mudd'
c = 'college'

#Problem 5 hey
Q5 = h[0] + h[-2:]
print(Q5)

#Problem 6 collude
Q6 = c[:4] + m[1:3] + c[-1]
print(Q6)

#Problem 7 'arveyudd'
Q7 = h[1:] + m[1:]
print(Q7)

#Problem 8 hardeharharhar
Q8 = h[0:3] + m[3] + c[4] + h[0:3] + h[0:3]
print(Q8)

#Problem 9 legomyego 
Q9 = c[3:5] + c[5::-4] + m[0] + h[-1] + c[4:6] + c[1]
print(Q9)

#Problem 10 clearcall
Q10 = c[0:4:2] + h[4::-3] + h[2] + c[0] + h[1] + c[2:4]
print(Q10)