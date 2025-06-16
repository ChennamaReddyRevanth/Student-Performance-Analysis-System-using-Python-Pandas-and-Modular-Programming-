### Student-Performance-Analysis-System-using-Python-Pandas-and-Modular-Programming-
## Objective:
Build a modular console-based system to manage and analyze student performance 
records using Python. This system should allow the user to add, update, analyze, and 
export student marks using pandas, and should be structured using functions, 
modules, and packages.


# Student Performance Analysis System

A modular, console-based Python application to manage and analyze student performance using **pandas**, with support for adding, updating, analyzing, and exporting records.


## Features

- Add, update, and view student records
- Auto-generate student IDs
- Calculate average marks and assign grades (A–F)
- View class-wise average marks using pandas `groupby()`
- Find subject toppers
- Export data to CSV (`student_data.csv`)
- Modular code structure with packages and functions
- CLI-based user interface

## Project Structure

student_performance/

├── main.py # Entry point    
└── student_system/ # Python package   
├── init.py    
├── data_handler.py # CSV loading/saving  
├── operations.py # Add/update/grade functions  
└── analysis.py # Reports and statistics

## Grade Criteria

| Average Marks | Grade |
|---------------|-------|
| ≥ 90          | A     |
| ≥ 75          | B     |
| ≥ 60          | C     |
| ≥ 40          | D     |
| < 40          | F     |


##  How to Run

1. **Install dependencies**:
   ```bash
   pip install pandas
Run the program:

Edit
====== STUDENT PERFORMANCE MENU ======
1. Add New Student Record
2. Update Student Marks
3. View All Student Records
4. View Class-wise Average Marks
5. View Subject Topper
6. Export Data to CSV
7. Exit
# Sample Output
==== STUDENT PERFORMANCE MENU ====
1. Add New Student Record
2. Update Student Marks
3. View All Student Records
4. View Class-wise Average Marks
5. View Subject Topper
6. Export Data to CSV
7. Exit
Choose option: 3

  Student ID     Name Class  Math  Science  English  Average Grade  
0       S001  Revanth   12A   100      100       99    99.67     A  
1       S002     sree   12A    99       95       66    86.67     B  
2       S003    fahim   12B    54       55       87    65.33     C  
3       S004    revss   12B   100      100      100   100.00     A  

==== STUDENT PERFORMANCE MENU ====
1. Add New Student Record
2. Update Student Marks
3. View All Student Records
4. View Class-wise Average Marks
5. View Subject Topper
6. Export Data to CSV
7. Exit
Choose option: 1

Enter Name: Dinesh

Enter Class: 11A

Math Marks: 99

Science Marks: 87

English Marks: 66

Student added successfully.

# Notes
Data is saved in student_data.csv upon choosing "Export".
Ensure the file is closed in Excel before saving to avoid permission errors.
Requires Python 3.8+ and pandas 2.x.
