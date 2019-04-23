#Omar De La Torre

#4/23/2019

sday=int(input("What is the starting day? (0-6) "))

lstay=int(input("What is the length of the stay? "))

rday=(sday+lstay)%7

dayDict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


print(dayDict[rday])
