#Colorful Cats
#SoftDev pd1
#K18 -- Average
#2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

#getting a list of courses by specific id
command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
allCourses = c.execute(command).fetchall()
#print(allCourses)

# print(type(allCourses[0][0]))
# print(type(allCourses[0][1]))
# print(type(allCourses[0][2]))


id = allCourses[0][1] #keeps track of ids
name = allCourses[0][0] #keeps track of names
#print(allCourses.fetchall())
#new table with student’s name, id, and average
command = "CREATE TABLE IF NOT EXISTS stu_avg (name TEXT, id INTEGER primary key, average REAL, numCourses INTEGER)"
c.execute(command)

count = 1; #keeps track of number of courses
sum = allCourses[0][2]; #keeps track of sum
for row in allCourses[1:]:
    #print("0")
    if row[1] == id:
        #print("1")
        sum += row[2] #adds to sum if id is the same
        count += 1
    else:
        #print("2")
        #inserts new row into table
        #print(name)
        #print(id)
        #print((sum/count))

        #print(type(name))
        #print(type(id))
        #print(type(sum/count))

        #print('INSERT INTO stu_avg VALUES (\"'+ name + '\", ' + str(id) + ', ' + str(sum/count) + ');')
        command = 'INSERT INTO stu_avg VALUES (\"'+ name + '\", ' + str(id) + ', ' + str(sum/count) + ', ' + str(count) + ');'
        c.execute(command)
        name = row[0]
        id = row[1]
        count = 1
        sum = row[2]

#insert last student after loop ends
command = 'INSERT INTO stu_avg VALUES (\"'+ name + '\", ' + str(id) + ', ' + str(sum/count) + ', ' + str(count) + ');'
c.execute(command)

#command = "SELECT * FROM stu_avg;"
#c.execute(command)
#print(c.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database
