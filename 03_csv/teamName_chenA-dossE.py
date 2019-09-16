#Amber Chen
#SoftDev1 pd1
#K6 -- StI/O: Divine your Destiny!
#2019-09-15

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

print(occupations['Management'])
