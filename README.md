# Student Registration Database

A command-line program for managing a university registration system,
built with Python and SQLite. Created for CIS 298 (Project 4).

## What it does
Lets a user manage the core records of a registration system from a menu:
- **Faculty and Students:** list, add, and update records (name, email)
- **Courses:** list, add, and update courses (department, number, credits)
- **Sections:** list, add, and update sections of a course
- **Enrollments:** list, add, update, and delete a student's enrollment in a section, including their grade
- **Transcripts:** enter a student ID to see every course they took, with credits and grade

## How it's built
Data is stored in a SQLite database with five related tables:
Faculty, Student, Course, Section, and Enrollment. Enrollment links
students to sections, and sections link to courses. The transcript
feature uses SQL joins across those tables to pull everything together.

## How to run
1. Make sure Python 3 is installed (SQLite comes with it).
2. [Create the database tables using schema.sql, or describe how your tables were set up].
3. Run `python registration.py` and follow the menu.

## What I learned
- Designing related tables and connecting them with keys
- Writing SQL queries (SELECT, INSERT, UPDATE, DELETE, INNER JOIN)
- Using parameterized queries (`?`) to pass user input safely
- Building a menu-driven interface in Python
