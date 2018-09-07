#Q.1- Write a python script to create a databse of students named Students.
import sqlite3
try:
    con=sqlite3.connect('Student.db')
    cursor=con.cursor()
    query="create table student( name varchar(10) , marks int(50))"
    cursor.execute(query)
    print("table created successfully")
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Done ")

#Que2- Take students name and marks(between 0-100) as input from user 10 times using loops.
record = []
for i in range(10):
    record.append((input("name "), int(input("marks "))))

#Que3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
try:
    con=sqlite3.connect('Student.db')
    cursor=con.cursor()
    query="insert into Student(name,marks) values(?,?)"
    cursor.executemany(query,record)
    con.commit()
    print("querry commited")
    quer="select * from Student"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("name :{}  marks :{}" .format(row[0],row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Done ")

#Que4- Print the names of all the students who scored more than 80 marks.
try:
    con=sqlite3.connect('Student.db')
    cursor=con.cursor()
    query="select * from Student where marks > 80"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("name :{}  marks :{}" .format(row[0],row[1]))
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Done ")
