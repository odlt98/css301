#Omar De La Torre
#4/9/2019

xlist=[1,2,3,4,5,6,7,8,9 ,-1, -2]

negSum = 0
posSum = 0

for x in xlist:
    if x<0 and x%2!=0:
        negSum+=x
    elif x>0 and x%2==0:
        posSum+=x
        
print(posSum+negSum)
