#Omar De La Torre

#4/23/2019

f = open("testText.txt", "r")

newF = open("newtestText.txt", "w")

counter = 1

for line in f:
    if counter % 2 !=0:
        newF.write(line)
    counter+=1

f.close()
newF.close()


