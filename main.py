#VANESSA CLARK
#CIS 298
#PROJECT 4
#CREATE A REGISTRATION DATA BASE USING THE LIBRARY SQLITE

# from https://www.py4e.com/html3/15-database

import sqlite3

connection = sqlite3.connect('registration.sqlite') #open nb
cursor = connection.cursor() #grab pen



#cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cursor.fetchall())

choice = ""

while choice != "QUIT":
    print("\nMain Menu") #mainmenu
    print("1 - Manage Faculty")
    print("2 - Manage Students")
    print("3 - Show Transcript")
    print("4 - Show Sections")
    print("5 - Show Courses")
    print("6 - Show Enrollments")
    print("QUIT - Exit")

    choice = input("Enter a choice: ").strip().upper()

    #1 DECISION: "choice" which section  of the program to go to ? 1. Faculty 2. Students 3. Transcript
    #2 DECISION: "action" where inside that section you want to go? 1. List 2. Add 3. change/modify

    if choice == "1":
        action = input("Enter 1 for List Faculty, 2 for Add Faculty, 3 for Update Faculty")

        if action == "1":
            cursor.execute('SELECT * FROM Faculty')
            print("id, name, email")
            for row in cursor: # read results
                print(row)  #read results
        elif action == "2":
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('INSERT INTO faculty (name, email) VALUES (?, ?)',(name, email))
            connection.commit()
        elif action == "3":
            id = int(input("Enter the ID to update"))
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('update faculty set name = ?, email = ? WHERE id = ?', (name, email, id) )
            connection.commit()
    elif choice == "2":
        action = input("Enter 1 for List Student, 2 for Add Student, 3 for Update Student: ")

        if action == "1":
            cursor.execute('SELECT * FROM Student')
            print("id, name, email")
            for row in cursor:
                print(row)

        elif action == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            cursor.execute(
                'INSERT INTO Student (name, email) VALUES (?, ?)',
                (name, email)
            )
            connection.commit()

        elif action == "3":
            student_id = int(input("Enter the ID to update: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            cursor.execute(
                'UPDATE Student SET name = ?, email = ? WHERE id = ?',
                (name, email, student_id)
            )
            connection.commit()

    elif choice == "3":
        student_id = int(input("Enter student ID: "))

        cursor.execute('''
            SELECT Course.Department, Course.Number, Course.Credits, Enrollment.Grade
            FROM Enrollment
            INNER JOIN Student ON Student.id = Enrollment.Student_ID
            INNER JOIN Section ON Section.ID = Enrollment.Section_ID
            INNER JOIN Course ON Course.id = Section.Course_ID
            WHERE Student_ID = ?
        ''', (student_id,))

        print("Department, Number, Credits, Grade")
        for row in cursor:
            print(row)


# to get a transcript for a given student
# select course.Department, Course.Number, course.Credits, Enrollment.Grade from Enrollment
# inner join student on Student.id = Enrollment.Student_ID
# inner join section on Section.ID = Enrollment.Section_ID
# inner join course on Course.id = Section.Course_ID
# where Student_ID = 1
    elif choice == "4":
        action = input("Enter 1 for List Section, 2 for Add Section, 3 for Update Section: ")

        if action == "1":
            cursor.execute('SELECT * FROM Section')
            for row in cursor:
                print(row)

        elif action == "2":
            course_id = input("Enter Course_ID: ")
            cursor.execute(
                'INSERT INTO Section (Course_ID) VALUES (?)',
                (course_id,)
            )
            connection.commit()

        elif action == "3":
            section_id = int(input("Enter section: "))
            course_id = input("Enter Course ID: ")
            cursor.execute(
                'UPDATE Section SET Course_ID = ? WHERE id = ?',
                (course_id, section_id)
            )
            connection.commit()
    elif choice == "5":
        action = input("Enter 1 for List Course, 2 for Add Course, 3 for Update Course: ")
        if action == "1":
            cursor.execute('SELECT * FROM Course')
            for row in cursor:
                print(row)
        elif action == "2":
            department = input("Enter Department: ")
            number = input("Enter Number: ")
            credits = input("Enter Credits: ")
            cursor.execute(
                'INSERT INTO Course (Department, Number, Credits) VALUES (?, ?, ?)',
            (department, number, credits)
            )
            connection.commit()

        elif action == "3":
            course_id = int(input("Enter ID: "))
            department = input("Enter Department: ")
            number = input("Enter Number: ")
            credits = input("Enter Credits: ")
            cursor.execute(
            'UPDATE Course SET Department = ?, Number = ?, Credits = ? WHERE id = ?',
      (department, number, credits, course_id)
        )
            connection.commit()

    elif choice == "6":
        action = input("Enter 1 for List Enrollment, 2 for Add Enrollment, 3 for Update Enrollment: 4 for Delete Enrollment:")

        if action == "1":
            cursor.execute('SELECT * FROM Enrollment')
            for row in cursor:
                print(row)

        elif action == "2":
            student_id = input("Enter the STUDENT ID: ")
            section_id = input("Enter the section: ")
            grade = input("Enter Grade: ")
            cursor.execute(
                'INSERT INTO Enrollment (Student_ID, Section_ID, Grade) VALUES (?, ?, ?)',
                (student_id, section_id, grade)
            )
            connection.commit()

        elif action == "3":
            enrollment_id = int(input("Enter enrollment id "))
            student_id = input("Enter Student ID: ")
            section_id = input("Enter Section : ")
            grade = input("Enter Grade: ")
            cursor.execute(
                'UPDATE Enrollment SET Student_ID = ?, Section_ID = ?, Grade = ? WHERE id = ?',
                (student_id, section_id, grade, enrollment_id)
            )
        elif action == "4":
            enrollment_id = int(input("Enter ID to delete: "))
            cursor.execute('DELETE FROM Enrollment WHERE id = ?', (enrollment_id,))
            connection.commit()
connection.close() #close notebook
