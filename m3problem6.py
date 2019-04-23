#Omar De La Torre

#4/23/2019

#program reads file and gives count for each time a word comes up


textD = {}

f = open("testText.txt", "r")

def buildTextD(words):
    for x in words:
        if x not in textD:
            textD[x] = 1
        else:
            textD[x] = textD[x] + 1

for line in f:
    w = line.split()
    buildTextD(w)

print(textD)

f.close()

