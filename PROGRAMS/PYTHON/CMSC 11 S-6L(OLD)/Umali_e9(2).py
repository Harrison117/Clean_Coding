'''

Harold S. Umali
April 9, 2015
Description: A program that allows adding user-given Student Name and basic information, viewing of student's information
 deleting a user-given name and its information using dictionaries, and saves/loads dictionary data using file handling and
 some other functions.

'''

def menu_(): ## Docstring for Menu display
    '''
What would you like to do?
    
    [1] Add a Student/Edit a Student Record
    [2] View a Student
    [3] View all Students
    [4] Delete a Student
    [5] Delete all Students
    [6] Save Record
    [7] Load current Record
    [8] Exit
    '''

    
def divider(): ## Separator function for easy reading of program
    for i in range(0,3):
        if i==1:
            for i in range(0,50):
                print("-",end="")
        print()
    return

    
def cont(): 
    if cont_=="8":
        return False
    return True    

    
def operations(operation,all_info): ## all_info is the student record dictionary passed throughout the functions
    if cont_=="1":
        addStudent(all_info)
    elif cont_=="2":
        for a in student_record.keys(): ## Displays key list for convenience
            print(a)
        find_stud=input("Find student: ")
        viewStudent(all_info,find_stud)
    elif cont_=="3":
        viewAllStudent(all_info)
    elif cont_=="4":
        for a in student_record.keys(): ## Same as viewing a student list (in key form)
            print(a)
        find_stud=input("Find student: ")
        deleteStudent(all_info,find_stud)
    elif cont_=="5":
        deleteAllStudent(all_info)
    elif cont_=="6":
        saveData(all_info)
    elif cont_=="7":
        loadData(all_info)

        
def addStudent(info):
    divider()
    name_=input("Enter Student Name: ")
    age_=input("Enter Student's Age: ")
    deg_course=input("Enter Student's Degree Course: ")
    gwa_=input("Enter Student's current GWA: ")
    student_record[name_]={"Age":age_,"Degree Course":deg_course,"GWA":gwa_} #This format will be the value of given name
    divider()
    for a,b in student_record.items(): ## Updated dictionary
        print(a,b)
    divider()
    print("Student info has been updated!")
    divider()
    input("Press enter to continue...")

        
def viewStudent(info,student_name):
    if student_name in student_record: ## Checks validity of name in dictionary(student record); prints if it exists
        divider()
        print(student_name)
        print("Age: ",student_record[student_name]['Age'])
        print("Degree Course: ",student_record[student_name]['Degree Course'])
        print("GWA: ",student_record[student_name]['GWA'])
        divider()
        input("Press enter to continue...")
    else: ## If student name doesn't exist...
        print(student_record.pop(student_name,"Student does not exist...")) 
        divider()
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
        print("Are you sure you want to delete",student_name+"'s record?")
        n=input("[1] Yes [Any key] No :  ")
        if n=="1":
            del student_record[student_name]
            divider()
            print("Record cleared!")
            for a,b in student_record.items(): ## Updated dictionary
                print(a,b)
            divider()
            input("Press enter to continue...")
    else:
        divider()
        print(student_record.pop(student_name,"Student does not exist...")) 
        ## Always prints "Name does not exist" if name does not exist
        divider()
        input("Press enter to continue...")
        

def deleteAllStudent(info):
    divider()
    print("Are you sure you want to delete all the students' names and their records?")
    n=input("[1] Yes [Any Key] No :  ")
    if n=="1":
        student_record.clear() ## Clears the rest of the records in the dictionary
        divider()
        print(info) ## Updated empty dictionary
        print("Entries cleared!")
        divider()
        input("Press enter to continue...")


def saveData(info): ## Turns dictionary into a text file...
    divider()
    print("WARNING! This will be overwriting the current save file...")
    n=input("Are you sure you want to save? [1] Overwrite [Any key] No: ")
    if n=="1":
        new_file=open("studrec.txt","w")
        new_file.write(str(info)) ## dictionary can't be stored in the text file, so it has to be converted into a string
        new_file.close()
        divider()
        input("Saved! Press enter to continue...")

    
def loadData(info):
    try: 
        ## This statement tests if the saved file studrec.txt exists; executes when it exist
        new_file=open("studrec.txt","r")
        for line in new_file:
            info.update(eval(line))
            ## eval(line) reads the line, which is a string, as a dictionary
            ## It "converts" the string into a dictionary
            ## The evaluated dictionary will be updated into the current dictionary data of the program
        new_file.close()
    except FileNotFoundError: 
        ## The type of error when the asked file doesn't exist.
        ## When the test(try) fail, it will 'catch' this error.
        ## So this block will execute when the error should happen.
        divider()
        print("The save file does not exist...")
        divider()
        input("Press enter to continue...")
        return
    divider()
    input("Loaded! Press enter to continue...")
    
    
student_record={}
print()
print("Welcome!")
while True:
    divider()
    print(menu_.__doc__)
    divider()
    cont_=input("Operation: ")
    operations(cont_,student_record)
    c=cont()
    if c:
        continue
    else:
        divider()
        print("Goodbye, see you again!")
        divider()
        input("Exiting program. Press enter to exit...")
        break