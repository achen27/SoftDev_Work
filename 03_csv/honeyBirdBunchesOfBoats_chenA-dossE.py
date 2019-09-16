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
    occupations[float(a[1])] = a[0]

#print(occupations['Management'])

#random funtion
def randomOcc():
    r = random.randint(1, 998) / 10.0
    #print("random num: " + str(r))
    for o in fNewList[1:-2]:
        if (r >= 0):
            #print(o[1])
            r -= float(o[1])
            #print("new num: " + str(r))
        else:
            return o[0]

#testing function
test = 0

fTest = []
for s in fList:
    fTest.append(s.rsplit(',',1))
print(fTest)
for s in fList[1:-2]:
    s[1] = 0
print(fTest)

#while (test < 1000):
