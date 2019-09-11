import random

KREWES = {'x':['a','b','c','d'],
    'y':['e','f','g','h'],
    'z':['i','j','k','l']}

def randStudent(team):
    students = KREWES[team]
    name = students[random.randint(0,len(students)-1)]
    return(name)

x = []
y = []
z = []
i = 0

while (i < 10):
    x.append(randStudent('x'));
    y.append(randStudent('y'));
    z.append(randStudent('z'));
    i+=1

print(x)
print(y)
print(z)
