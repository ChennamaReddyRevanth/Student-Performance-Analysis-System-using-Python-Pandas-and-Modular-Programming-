
from student_system import data_handler, operations, analysis

def main():
    
    
    df = data_handler.load_data()
    while True:
        print("\n==== STUDENT PERFORMANCE MENU ====")
        print("1. Add New Student Record")
        print("2. Update Student Marks")
        print("3. View All Student Records")
        print("4. View Class-wise Average Marks")
        print("5. View Subject Topper")
        print("6. Export Data to CSV")
        print("7. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            name = input("Enter Name: ")
            cls = input("Enter Class: ")
            math = int(input("Math Marks: "))
            sci = int(input("Science Marks: "))
            eng = int(input("English Marks: "))
            df = operations.add_student(df, name, cls, math, sci, eng)
            print("Student added successfully.")
        elif choice == "2":
            sid = input("Enter Student ID: ")
            math = int(input("Math Marks: "))
            sci = int(input("Science Marks: "))
            eng = int(input("English Marks: "))
            df = operations.update_marks(df, sid, math, sci, eng)
            print("Marks updated.")
        elif choice == "3":
            print(df)
        elif choice == "4":
            print(analysis.class_wise_average(df))
        elif choice == "5":
            sub = input("Enter Subject (Math/Science/English): ")
            print(analysis.subject_topper(df, sub))
        elif choice == "6":
            data_handler.save_data(df)
            print("Data exported to student_data.csv")
        elif choice == "7":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
