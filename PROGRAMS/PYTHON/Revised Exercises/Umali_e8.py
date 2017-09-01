'''

@author Harold S. Umali
Originally created in: April 2 2015
Revised in: August 30 2017
Description: A program that allows adding user-given Student Name and basic information, viewing of student's
    information and deleting a user-given name and its Information using dictionaries

    UPDATE(08/30):
        

'''

CONST_OK = 'y'
CONST_NULL = ''
CONST_ENTER_LOGIN = 'PROMPT_LOGIN'
CONST_DELETE_INFO = 'PROMPT_DELETE'

def divider(): #Separator for easy reading of program
    for i in range(0,3):
        if i==1:
            for i in range(0,50):
                print("-",end="")
        print()
    return

def userAuthentication(typeOfPrompt, passwordGiven):

    if typeOfPrompt == CONST_ENTER_LOGIN:
        username = input("Enter Username: ")
        password = input("Enter password: ")
        return username, password

    elif typeOfPrompt == CONST_DELETE_INFO:
        password = input("Enter password to delete: ")
        if password == passwordGiven:
            return CONST_OK
        else:
            return CONST_NULL

def addStudentInformation(informationRecord):
    studentName = input("Enter Student Name: ")
    studentNickname = input("Enter Student Nickname: ")
    studentNumber = input("Enter Student Number: ")
    studentClassification = input("Enter Student Classification: ")
    studentCourse = input("Enter Degree Course: ")
    studentCollege = input("Enter Attending College: ")
    studentAge = int(input("Enter Student Age: "))
    studentGrade = int(input("Enter Recent Grade: "))

    informationRecord[studentName] = {
        'Nickname':studentNickname,
        'Student Number':studentNumber,
        'Classification':studentClassification,
        'Course':studentCourse,
        'College':studentCollege,
        'Age':studentAge,
        'GWA':studentGrade
    }

    return informationRecord

def viewStudentInformation(informationRecord):

    nameSearch = input("Search name: ")
    if nameSearch in informationRecord:
        print("Student Name: {}".format(studentName))

        for attribute, value in studentName.items():
            print("{}: {}".format(attribute, value))

    else:
        print("Record of {} not found...".format(nameSearch))

    return

def viewAllStudentInformation(informationRecord):
    for studentName, studentDescription in informationRecord.items():
        divider()
        print("Student Name: {}".format(studentName))

        for attribute, value in studentDescription.items():
            print("{}: {}".format(attribute, value))

    return

def deleteStudentInformation(informationRecord):
    nameSearch = input("Enter name: ")

    if nameSearch in informationRecord:
        print("Are you sure you want to delete the records of {}?".format(nameSearch))
        permission = userAuthentication('PROMPT_DELETE')

        if permission == CONST_OK:
            del informationRecord[nameSearch]
        else:
            print("Authentication failed...")

    return

def clearStudentRecords(informationRecord):
    print("Are you sure you want to delete all the records?")
    permission = userAuthentication('PROMPT_DELETE')

    if permission == CONST_OK:
        informationRecord.clear()
        print("DELETE SUCCESSFUL...")

    return

studentInformationRecord={}

stateOfProgram = True
