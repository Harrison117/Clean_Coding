'''

Harold S. Umali
April 2, 2015
Description: A program that allows adding user-given Student Name and basic information, viewing of student's information
 and deleting a user-given name and its Information using dictionaries

'''

def menu_(): #Docstring for Menu display
    '''
    [1] Add a Student
    [2] View a Student
    [3] View all Students
    [4] Delete a Student
    [5] Delete all Students
    [6] Exit
    '''

def divider(): #Separator for easy reading of program
    for i in range(0,3):
        if i==1:
            for i in range(0,50):
                print("-",end="")
        print()
    return

def cont():
    if cont_==6:
        return False
    return True

def operations(operation,all_info): #all_info is the student record dictionary passed throughout the functions
    if cont_==1:
        addStudent(all_info)
    elif cont_==2:
        for a in student_record.keys(): #Displays key list for convenience
            print(a)
        find=input("Enter name: ")
        viewStudent(all_info,find)
    elif cont_==3:
        viewAllStudent(all_info)
    elif cont_==4:
        for a in student_record.keys(): #Same as viewing a student list (in key form)
            print(a)
        find=input("Enter name: ")
        deleteStudent(all_info,find)
    elif cont_==5:
        deleteAllStudent(all_info)

def addStudent(info): #Adds student name and info
    divider()
    name_=input("Enter Name: ")
    age_=input("Enter Age: ")
    deg_course=input("Enter Degree Course: ")
    gwa_=input("Enter GWA: ")
    student_record[name_]={"Age":age_,"Degree Course":deg_course,"GWA":gwa_} #This format will be the value of given name
    divider()
    for a,b in student_record.items(): #Updated dictionary
        print(a,b)

def viewStudent(info,student_name):
    if student_name in student_record: #Checks validity of name in dictionary(student record); prints if it exists
        divider()
        print(student_name)
        print("Age: ",student_record[student_name]['Age'])
        print("Degree Course: ",student_record[student_name]['Degree Course'])
        print("GWA: ",student_record[student_name]['GWA'])
        divider()
        input("Press enter to continue...")
    else:
        print(student_record.pop(student_name,"Name does not exist...")) #Always prints "Name does not exist" if name does not exist
        input("Press enter to continue...")

def viewAllStudent(info):
    divider()
    for a,b in student_record.items():
        print(a,b)
    divider()
    input("Press enter to continue...")

def deleteStudent(info,student_name):
    if student_name in student_record:
        divider()
        print("Are you sure you want to delete",student_name,"and its information?") #Notification
        n=int(input("[1] Yes [Any key] No :  "))
        if n==1:
            del student_record[student_name]
            divider()
            print("Entry cleared!")
            for a,b in student_record.items(): #Updated dictionary
                print(a,b)
            divider()
            input("Press enter to continue...")
    else:
        divider()
        print(student_record.pop(student_name,"Name does not exist...")) #Always prints "Name does not exist" if name does not exist
        input("Press enter to continue...")

def deleteAllStudent(info):
    divider()
    print("Are you sure you want to delete all the the names and their info?") #Notification
    n=int(input("[1] Yes [Any Key] No :  "))
    if n==1:
        student_record.clear() #Clears the rest of the records in the dictionary
        divider()
        print(info) #Updated empty dictionary
        print("Entries cleared!")
        divider()
        input("Press enter to continue...")

student_record={}
P=True
while P:
    divider()
    print(menu_.__doc__)
    divider()
    cont_=int(input("Operation: "))
    operations(cont_,student_record)
    c=cont()
    if c:
        continue
    else:
        divider()
        input("Goodbye, see you again!")
        break
