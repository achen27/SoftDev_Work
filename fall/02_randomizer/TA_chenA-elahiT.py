#Amber Chen
#SoftDev1 pd1
#K02 -- NO-body expects the Spanish Inquisition!
#2019-09-11

import random

#list of students
KREWES = {'orpheus':['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
    'rex':['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'],
    'endymion':['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren', 'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry', 'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']}

#randomizer with team as paramerter
def randStudent(team):
    students = KREWES[team] #retreiving list based on parameter passed
    name = students[random.randint(0,len(students)-1)] #choses random index and assigns value to name
    return(name) #returns random name


#testing
#x = []
#y = []
#z = []
#i = 0

#while (i < 10):
#    x.append(randStudent('orpheus'));
#    y.append(randStudent('rex'));
#    z.append(randStudent('endymion'));
#    i+=1

#print(x)
#print(y)
#print(z)
