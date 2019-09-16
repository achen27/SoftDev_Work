#Amber Chen
#SoftDev1 pd1
#K6 -- StI/O: Divine your Destiny!
#2019-09-15

import random

#opening file
f = open("occupations.csv","r")

#storing file into large string
fString = f.read()

#spliting string into array with name and percentage as an element
fList = fString.split('\n')

#creating new array with each element as an array with name and percentage
fNewList = []
for s in fList:
    fNewList.append(s.rsplit(',',1))

#added key value pairs to dictionary
occupations = {}
for a in fNewList[1:-2]:
    occupations[a[0]] = float(a[1])

#print(occupations['Management'])

#random funtion
def randomOcc():
    r = random.randint(1, 998) / 10.0
    #print("random num: " + str(r))
    for o in fNewList[1:-2]:
        r -= float(o[1])
        if (r <= 0):
            return o[0]

#TESTING
test = 0

#creating new array to count occurances
fTest = []
for s in fList:
    fTest.append(s.rsplit(',',1))
#print(fTest)
for s in fTest[1:-2]:
    s[1] = str(0)
#print(fTest)

#testing many runs of function
while (test < 1000000):
    str = randomOcc()
    for s in fTest:
        if str == s[0]:
            s[1] = int(s[1]) + 1
    test += 1

#calculating percentages of each
for s in fTest[1:-2]:
    s[1] = int(s[1]) / 10000.0

#finding difference from actual percentages
x = 1
for s in fTest[1:-2]:
    s[1] = round((float(s[1]) - float(fNewList[x][1])),2)
    x += 1

#printing results
for s in fTest[1:-2]:
    print(s)
