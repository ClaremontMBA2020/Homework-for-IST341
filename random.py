#import random 
#random.choice([41,42,43])

#x = 0

#for i in range(4):
#    x += 10
#print(x)

# L = ['golf', 'fore!', 'club', 'tee']
# for i in range(len(L)):
#     if i%2 == 1:
#         print(L[i])

S ='time to think this over!'
result = ''
for i in range(len(S)):
    if S[i-1] == ' ':
        result += S[i]
print(result)