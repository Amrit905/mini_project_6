'''STUDENT RECORD PERSISTENCE & EXPORT SYSTEM'''
import csv
import json
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "students.json")
CSV_FILE = os.path.join(BASE_DIR, "students.csv")
LOG_FILE = os.path.join(BASE_DIR, "activity_log.txt")
 
#SUBJECTS NAME
SUBJECTS = ("Python", "Maths", "DBMS")


#LOAD EXISTING DATA
def load_Students():
    
    if not os.path.exists(JSON_FILE):
        print("No students.json Found.Starting with empty data.")
        return {}, True
    
    #READING JSON FILE
    with open(JSON_FILE,'r',encoding='utf-8') as file:
        data = json.load(file)
    
    print("\nStudent records loaded successfully")    
    return data, True
 
#SAVE STUDENTS RECORD TO JSON FILE
def save_student(students):
    with open(JSON_FILE,"w", encoding='utf-8') as file:
        json.dump(students,file,indent=3)   
        
        print("\n Records Saved Sucessfully to students.json.")  
        
        return True
    
        
#ADD STUDENT RECORDS
def add_students(student_records):
    
    # student_records={}
    
    while True:
        
        student_id= input("Enter Student ID: ")
        
        if student_id in student_records:
            print("Student Id already exists.")
            continue
        
        student_name = input("Enter Student Name: ")
        
        if student_name=="":
            print("Student's Name can't be empty.")
            continue
        
        department = input("Enter Department of the student: ")
        
        marks={}
        
        for subject in SUBJECTS:
            
            subject_mark = float(input(f"Enter {subject} marks: "))
            
            if 0<=subject_mark<=100:
                
                if subject_mark.is_integer():
                    
                    marks[subject]=subject_mark
                    
                
            else:
                print("marks must be in between 0 and 100")
                
        student={"Name":student_name,"Department":department,"Marks":marks}
    
        student_records[student_id]=student   
        
        if save_student(student_records):
            
            write_log(f"Added student record: {student_id}")
            
            print('\nStudent record added successfully!')
        else:
            del student_records[student_id]
            
            
#DISPLAYING A STUDENT RECORD BY USING STUDENT ID
def display_student(student_id, student):
    
    print("\n" + "=" * 55)
    print("                STUDENT DETAILS")
    print("=" * 55)
    
    print("\nStudent ID: ",student_id)
    print("\nStudent Name: ", student["Name"])
    print("\nDepartment: ",student["Department"])
    
    print("\nSubject Marks:")
    for subject in SUBJECTS:
       print(f"{subject:<15}: {student['Marks'][subject]}")

       print("-" * 55)
       
       
'''ACTIVITY LOG''' 
      
def initialize_log():

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", encoding="utf-8") as file:

            file.writelines([
                "STUDENT RECORDS SYSTEM ACTIVITY LOG\n",
                "=" * 50 + "\n"
            ])


def write_log(message):

    current_time = datetime.datetime.now()

    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] {message}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(log_message)


  
#DISPLAY ALL STUDENTS
def display_all(student_record):
    
    if not student_record:
        print("\nNo student records are found!")
        
        return
    
    
    print("\n" + "=" * 55)
    print("                 ALL STUDENT RECORDS")
    print("=" * 55)
    
    for student_id,student in student_record.items():
        display_student(student_id,student)
        

#Search Student
def search_student(student_record):
    
    print("\n" + "=" * 55)
    print("                  SEARCH STUDENT")
    print("=" * 55)
    
    student_id = input("Enter Student ID to search: ")
    
    if student_id in student_record:
        display_student(student_id, student_record[student_id])
    
    else:
        print("\nStudent record not found.")
        
#UPDATING STUDENT RECORD
def update(student_record):
    

    print("\n" + "=" * 55)
    print("                 UPDATE STUDENT RECORD")
    print("=" * 55)

    student_id = input("Enter Student ID to update: ")
    
    if student_id not in student_record:
        print("\n student record not found!")
        return
    
    student=student_record[student_id]
    
    print("\nCurrent student details:")
    display_student(student_id,student)
    
    print("\nUpdate student details:")
    
    student["Name"]=input("Enter New name: ")
    student["Department"]=input("Enter new department:")
    
    for subject in SUBJECTS:
        student["Marks"][subject]=float(input(f"Enter {subject} marks:"))
        
    if save_student(student_record):
        
        write_log(f"Updated student record: {student_id}")
        
        print("\nStudent record updated successfully!")
        
        
#EXPORT TO CSV
def csv_export(student_record):
    
    if not student_record:
        print("\nNo student record found!")
        
        return
    
    headers=["Student ID","Name","Department","Python","Maths","DBMS"] 
    
    with open(CSV_FILE,'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
        
        for student_id, student in student_record.items():
            
            row ={"Student ID":student_id,"Name":student["Name"],"Department":student["Department"],"Python":student["Marks"]["Python"],"Maths":student["Marks"]['Maths'],"DBMS":student["Marks"]["DBMS"]}  
            
            writer.writerow(row)
            
        print("\nCSV export completed successfully!")   
                 
        print("File location:", CSV_FILE)

        write_log(f"Exported {len(student_record)} student records to students.csv")
        

'''READING METHODS READ(), READLINE(), READLINES()'''
def read_log():
    print("\nUsing read() method:")
    
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        content=file.read()

    print(content)

def readline_log():
    print("\nUsing readline() method:")
    
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        line = file.readline()

        print(line)
        

def readlines_log():
    print("\nUsing readlines() method:")
    
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
        print(lines)

def view_activity_log():

    while True:

        print("\n" + "=" * 55)

        print("                  VIEW ACTIVITY LOG")

        print("=" * 55)

        print("1. Read entire file using read()")

        print("2. Read one line using readline()")

        print("3. Read all lines using readlines()")

        print("4. Return to main menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            read_log()

        elif choice == "2":

            readline_log()

        elif choice == "3":

            readlines_log()

        elif choice == "4":

            break

        else:

            print("\nInvalid choice. Please try again.")


'''JSON STRING OPERATIONS'''
def json_string(student_record):
    
    if not student_record:
        print("\nStudent record not available!")
        
        return
    
    student_id = input("Enetr Student ID for json demonstration: ")
    
    if student_id not in student_record:
        print("\nStudent record not found!")
        return
    
    student=student_record[student_id]
    
    #CONVERTING PYTHON_OBJECT TO JSON STRNG USING JSON.DUMPS()
    
    json_strings=json.dumps(student, indent=4)
    
    print("\n",json_strings)
    
    #CONVERTING JSON STTRING TO PYTHON_OBJECT USING JSON.LOADS()
    py_obj = json.loads(json_strings)
    
    print("\n",py_obj)
    
    print("\nJSON string conversion demonstrated successfully!")
    


            
#MAIN FUNCTION           
def main():
    
    initialize_log()
    
    Student_Records, storage_ready = load_Students()
    
    while True:
          
        print("\n" + "=" * 65)
        print("          STUDENT RECORDS MANAGEMENT SYSTEM")
        print("=" * 65)

        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Search Student by ID")
        print("4. Update Student Record")
        print("5. Export Records to CSV")
        print("6. View Activity Log")
        print("7. Demonstrate JSON String Operations")
        print("8. Exit")

        print("=" * 65)
        
        choice = int(input("Enter Your Choice(1-8): "))
        
        if choice==1:
            
            if storage_ready:
                add_students(Student_Records)
                
                
            else:
                print("\nCan't add records because json loading failed.")
                
        elif choice==2:
            
            if storage_ready:
                display_all(Student_Records)
            else:
                print("\nStudent records not available.")
                
        elif choice ==3:
            
            if storage_ready:
                search_student(Student_Records)
            else:
                print("\nStudent details not found")    
            
        elif choice==4:   
            
            if storage_ready:
                update(Student_Records)
            else:
                print("\nJson loading failed.Can't update at the moment.")
                    
        elif choice==5:
            
            if storage_ready:
                csv_export(Student_Records)
            else:
                print("\nJson loading failed.Can't export now!")
                       
        elif choice==6: 
            view_activity_log()
                      
        elif choice==7:  
            
            if storage_ready:
                json_string(Student_Records)
            else:
                print("\nStudent records not found!") 
                    
        elif choice==8: 
            
            print("Exiting....")      
            break
        
        else:
            print("\nInvalid Choice.")
    
if __name__=="__main__":
    main()