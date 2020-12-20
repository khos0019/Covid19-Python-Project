'''
Created on Oct. 7, 2020
Updated on Nov. 29, 2020

References: 
        
'Python MySQL Select From Table [Complete Guide],' PYnative, 09-Jun-2020. [Online]. 
Available: https://pynative.com/python-mysql-select-query-to-fetch-data/. [Accessed: 29-Nov-2020].

'Python MySQL - Where Clause,' Tutorialspoint. [Online]. 
Available: https://www.tutorialspoint.com/python_data_access/python_mysql_where_clause.htm#:~:text=If you want to fetch,the table for the operation. 
[Accessed: 29-Nov-2020].

@author: Khosla
'''

from covid19.View.CovidView import CovidView
from covid19.Model.CovidModel import CovidModel
import re
import csv
from os import path
import mysql.connector 

'''
For your information: You must have a MySQL workbench created with localhost, default port and root username.
Also, No need to manually create your own database in MySQL, when you save the records for the first time a database 
and a table is created for you.
'''
class CovidController():
    '''
    Uses the user's input to create, edit and delete records. Also, uses the user's input to load and save records.
    '''
    
    ##Choice is initialized to be equal to -1.
    choice = -1
    
    ##maxNumberofRecords is initialized to be equal to 200. Also, this variable determines the number of records that can be created.
    maxNumberofRecords = 200
    
    def __init__(self):
        '''
        Initializes itself. Similar to a default constructor in Java.
        '''
        
        ##Stores all the records.
        self.covidModels = []
        
        ##Creates a new instance of CovidView().
        self.covidView = CovidView()
    
    def launch(self):
        '''
        Based of user input, one of the following selections will call a method associated with it.
        '''
        
        print("Created By Navraj Khosla.")
        
        ##Prompts the user if they want to load the records from the database.
        isDatabase = self.covidView.userPrompt("\nWould you like to load the records from the database (YES/NO)? ")
        
        ##If the user enters YES, loadFromDatabase() method is called. 
        if isDatabase.lower()[0] == "y":
            self.loadFromDatabase("pythonassignment")
                
        ##If the user enters NO, a new prompt is displayed.
        elif isDatabase.lower()[0] == "n":
            ##Prompts the user if they want to load the records from a CSV file.
            isCSV = self.covidView.userPrompt("\nWould you like to load the records from a CSV file (YES/NO)? ")
            
            ##If the user enters YES, loadFromFile() method is called. If the user enters NO, records are not loaded to the simple data structure.
            if isCSV.lower()[0] == "y":
                self.loadFromFile()

        ##Continue to display the menu until a valid selection is made by the user.
        while(True):
                        
            ##Stores the users input from the displayed menu.
            choice = self.covidView.displayMenu()
    
            ##If the user entered 1, a prompt is shown to the user.
            if choice == 1:
                ##Prompts the user if they want to display records from the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to display records from the database (YES/NO)? ")
                
                ##If the user enters YES, displayFromDatabase() method is called. 
                if isDatabase.lower()[0] == "y":
                    self.displayFromDatabase("pythonassignment")
                
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to display the records from the simple data structure.
                    isCSV = self.covidView.userPrompt("\nWould you like to display records from the in-memory data (YES/NO)? ")
                    
                    ##If the user enters YES, displayRecordMenu() method is called. If the user enters NO, records are not displayed.
                    if isCSV.lower()[0] == "y":
                        self.displayRecordMenu()
            
            ##If the user entered 2, the findRecordsFromDatabase() method is called.            
            elif choice == 2:
                self.findRecordsFromDatabase("pythonassignment")
            
            ##If the user entered 3, a prompt is shown to the user.
            elif choice == 3:
                ##Prompts the user if they want to create a record in the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to create a record for the database (YES/NO)? ")
                
                ##If the user enters YES, databaseCreateRecord() method is called. 
                if isDatabase.lower()[0] == "y":
                    self.databaseCreateRecord("pythonassignment")
                
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to create a record in the simple data structure.
                    isCSV = self.covidView.userPrompt("\nWould you like to create a record for the in-memory data (YES/NO)? ")
                    
                    ##If the user enters YES, createRecord() method is called. If the user enters NO, a record is not created.
                    if isCSV.lower()[0] == "y":
                        self.createRecord()
                    
            ##If the user entered 4, a prompt is shown to the user.
            elif choice == 4:
                ##Prompts the user if they want to edit a record in the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to edit a record in the database (YES/NO)? ")
                
                ##If the user enters YES, databaseUpdatedRecord() method is called. 
                if isDatabase.lower()[0] == "y":
                    self.databaseUpdateRecord("pythonassignment")
                
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to edit a record in the simple data structure.
                    isCSV = self.covidView.userPrompt("\nWould you like to edit a record in the in-memory data (YES/NO)? ")

                    ##If the user enters YES, editRecord() method is called. If the user enters NO, a record is not edited.
                    if isCSV.lower()[0] == "y":
                        self.editRecord()
            
            ##If the user entered 5, a prompt is shown to the user.
            elif choice == 5:
                ##Prompts the user if they want to delete a record in the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to delete a record in the database (YES/NO)? ")
                
                ##If the user enters YES, databaseDeleteRecord() method is called. 
                if isDatabase.lower()[0] == "y":
                    self.databaseDeleteRecord("pythonassignment")
                
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to delete a record in the simple data structure.
                    isCSV = self.covidView.userPrompt("\nWould you like to delete a record in the in-memory data (YES/NO)? ")

                    ##If the user enters YES, deleteRecord() method is called. If the user enters NO, a record is not deleted.
                    if isCSV.lower()[0] == "y":
                        self.deleteRecord()
            
            ##If the user entered 6, a prompt is shown to the user.
            elif choice == 6:
                ##Prompts the user if they want to load the records from the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to load the records from the database (YES/NO)? ")
                
                ##If the user enters YES, loadFromDatabase() method is called. 
                if isDatabase.lower()[0] == "y":
                    self.loadFromDatabase("pythonassignment")
                        
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to load the records from a CSV file.
                    isCSV = self.covidView.userPrompt("\nWould you like to load the records from a CSV file (YES/NO)? ")
                    
                    ##If the user enters YES, loadFromFile() method is called. If the user enters NO, records are not loaded to the simple data structure.
                    if isCSV.lower()[0] == "y":
                        self.loadFromFile()
            
            ##If the user entered 7, a prompt is shown to the user.
            elif choice == 7:    
                ##Prompts the user if they want to save the records into the database.
                isDatabase = self.covidView.userPrompt("\nWould you like to save the records to the database (YES/NO)? ")
                
                ##If the user enters YES, saveToDatabase() method is called.
                if isDatabase.lower()[0] == "y":
                    self.saveToDatabase("pythonassignment")
                
                ##If the user enters NO, a new prompt is displayed.
                elif isDatabase.lower()[0] == "n":
                    ##Prompts the user if they want to save the records into a CSV file.
                    isCSV = self.covidView.userPrompt("\nWould you like to save the records to a CSV file (YES/NO)? ")

                    ##If the user enters YES, saveToFile() method is called. If the user enters NO, records are not saved.
                    if isCSV.lower()[0] == "y":
                        self.saveToFile()

            ##If the user entered 8, it will call exit() method.
            elif choice == 8:    
                self.exit()
                break
                
            else:
                ##Displays the error message.
                self.covidView.printError("\nInvalid Selection.")    
        
    def displayRecordMenu(self):
        '''
        Displays the record menu to determine how many records the user would like to see. Starting from the first record.
        '''
        
        ##Stores the number of records the user wants to see.
        numRecords = self.covidView.userNumericPrompt("\nHow many records would you like to view? ")
        
        ##Checks if numRecords is an integer.
        if isinstance(numRecords, int):
            
            ##Determines if the number of records the user wants to see is more than what is stored in the in-memory data.
            if numRecords > len(self.covidModels):
                
                ##Displays an error message.
                self.covidView.printError("\nInsufficient records.")
                return
            
            ##Displays the number of records that the user wants to see.
            for i in range(numRecords):
                
                ##Prints out the records from the in-memory data.
                self.covidView.printRecord(self.covidModels[i])
        
    
    def createRecord(self):
        '''
        Creates a record based of user input.
        '''
        
        ##Determines if the in-memory data is equal to the max number of records that can be stored.
        if len(self.covidModels) == self.maxNumberofRecords:
            
            ##Displays the error message.
            self.covidView.printError("Max Number of Records. Cannot create a new record.")
            return
        
        print("\nPlease enter the following information about the record you would like to create.")
    
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")
        
        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
        
        ##Store and pass all the user input to the __init__() method in CovidModels.
        covidModel = CovidModel(countryID, date, cases, deaths, nameFR, nameEN)
        
        ##Append the information to the list.
        self.covidModels.append(covidModel) 
        
        ##Display the completion message.
        self.covidView.printCompletion("\nRecord created.")
        return   
    
    def editRecord(self):
        '''
        Edits a record that the user knows it exists, based of user input to find a match from the list.
        '''
        
        print("\nPlease enter the following information about the record you would like to edit.")
        
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")

        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
        
        ##Go through each record that exists inside the list.
        for i in range(len(self.covidModels)) :
            
            ##Store all the records in CovidRecord.
            CovidRecord = self.covidModels[i]
            
            ##Check and find a match between the user input and records from CovidRecord.
            if CovidRecord.getID() == countryID and CovidRecord.getDate() == date and CovidRecord.getCases() == cases and CovidRecord.getDeaths() == deaths and CovidRecord.getNameFr() == nameFR and CovidRecord.getNameEn() == nameEN:
                
                ##If match found, display the edit record menu.
                editFieldsString = self.covidView.editRecordMenu()
                
                ##Split the user input.
                editFields = editFieldsString.split(',')
                
                ##Store the strings in field.
                for field in editFields:
                    
                    ##If user entered id, store and prompt for a new Country ID, and set that record's ID to the new Country ID.
                    if field.strip() == 'id':
                        newID = self.covidView.userPrompt("\nEnter New Country ID: ")
                        self.covidModels[i].setID(newID)
                    
                    ##If user entered date, store and prompt for a new Date, and set that record's Date to the new Date.
                    if field.strip() == 'date':
                        newDate = self.covidView.userPrompt("Enter New Date (YYYY-MM-DD): ")
                        self.covidModels[i].setDate(newDate)
                        
                    ##If user entered cases, store and prompt for a new Number of Cases, and set that record's Number of Cases 
                    ##to the new Number of Cases.
                    if field.strip() == 'cases':
                        newCase = self.covidView.userPrompt("Enter New Number of Cases: ")
                        self.covidModels[i].setCases(newCase)
                        
                    ##If user entered deaths, store and prompt for a new Number of Deaths, and set that record's Number of Deaths 
                    ##to the new Number of Deaths.    
                    if field.strip() == 'deaths':
                        newDeath = self.covidView.userPrompt("Enter New Number of Deaths: ")
                        self.covidModels[i].setDeaths(newDeath)
                        
                    ##If user entered name_fr, store and prompt for a new Country Name in French, and set that record's Country Name in 
                    ##French to the new Country Name in French.    
                    if field.strip() == 'name_fr':
                        newNameFR = self.covidView.userPrompt("Enter New Country Name in French: ")
                        self.covidModels[i].setNameFr(newNameFR)   
                    
                    ##If user entered name_en, store and prompt for a new Country Name in English, and set that record's Country Name in 
                    ##English to the new Country Name in English.     
                    if field.strip() == 'name_en':
                        newNameEN = self.covidView.userPrompt("Enter New Country Name in English: ")
                        self.covidModels[i].setNameEn(newNameEN)    
                     
                ##Display the completion message.
                self.covidView.printCompletion("\nRecord has been edited.")
                        
                break
             
            
    def deleteRecord(self):
        '''
        Deletes a record that the user knows it exists, based of user input to find a match from the list.
        '''
        
        ##Initializes recordDeleted to be false.
        recordDeleted = False
        
        print("\nPlease enter the following information about the record you would like to delete.")
        
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")

        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
         
        ##Stores the records that we will delete.
        recordsToDelete = []    
        
        ##Confirms that the user wants to delete the record.
        confirm = self.covidView.userPrompt("\nAre you sure you want to delete the record (Y/N)? ")   
        
        ##Checks if the user selects Y.
        if confirm.lower()[0] == 'y':    
            
            ##Go through each record that exists inside the list.
            for i in range(len(self.covidModels)) :
            
                ##Store all the records in CovidRecord.
                CovidRecord = self.covidModels[i]
                
                ##Check and find a match between the user input and records from CovidRecord.
                if CovidRecord.getID() == countryID and CovidRecord.getDate() == date and CovidRecord.getCases() == cases and CovidRecord.getDeaths() == deaths and CovidRecord.getNameFr() == nameFR and CovidRecord.getNameEn() == nameEN:
                    
                    ##Appends the record that matches the user input to recordsToDelete list.
                    recordsToDelete.append(CovidRecord)
            
            ##Goes through the list.        
            for j in range(len(recordsToDelete)):
                
                ##Removes the record from the in-memory data.
                self.covidModels.remove(recordsToDelete[j])
                
                ##Changes recordDeleted to equal True since a record has been deleted.
                recordDeleted = True
                
                ##Display the completion message.
                self.covidView.printCompletion("\nRecord has been deleted.")
                
        return recordDeleted
        
        
    def loadFromFile(self):
        '''
        Loads records from a file to the in-memory data.
        '''
        
        ##Clears the in-memory data.
        self.covidModels.clear()
        
        ##Stores the file name that the user wants to use to load the records from.
        fileName = self.covidView.userPrompt("\nEnter file name to load from (default file is InternationalCovid19Cases.csv): " )
        
        ##If the user does not put any input in, the records will be loaded from InternationalCovid19Cases by default.
        if fileName == "":
            fileName = "InternationalCovid19Cases"
        
        ##If the user inputs a file name without the file name extension, we will add the csv file extension for them.
        if fileName.find('.') < 0:
            fileName = fileName + ".csv"
        
        try :
    
            ##File exists, attempting to open the file and read the contents of the file
            with open(fileName, newline='', encoding='utf-8') as csvFile:
                count = 0
                reader = csv.reader(csvFile, delimiter=',')
                
                ##Add the first 100 records from the file to the data structure.     
                for row in reader:
                    if count > 0 and count <= 100 :
                                                
                        rowID = row[0]
                        rowDate = row[1]
                        rowCases = row[2]
                        rowDeaths = row[3]
                        rowNameFR = row[4]
                        rowNameEN = row[5]
                        
                        covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)
                        
                        ##Appends each record loaded to the list.
                        self.covidModels.append(covidModel)
         
                    count = count + 1
                
                ##Displays the completion message.
                self.covidView.printCompletion("\nData set loaded from file.")    
    
        ##Handles any errors when reading the file.
        except IOError as e :
            print(e)
            
    def saveToFile(self):       
        '''
        Saves the in-memory data records to a file.
        '''
        
        ##Stores the file name that the user wants to use to save the records to.
        fileName = self.covidView.userPrompt("\nEnter file name to save to (default file is InternationalCovid19Cases.csv): " )
        
        ##If the user does not put any input in, the records will be loaded from InternationalCovid19Cases by default.
        if fileName == "":
            fileName = "InternationalCovid19Cases"
        
        ##If the user inputs a file name without the file name extension, we will add the csv file extension for them.
        if fileName.find(".") < 0:
            fileName = fileName + ".csv"
        
        ##Checks if the file exists.
        fileExists = path.exists(fileName)
        
        ##If file exists, append the records instead of writing over the records that already exist in the file.    
        if fileExists:
            csvFile = open(fileName, 'a+', newline='', encoding='utf-8')
        
        ##If file does not exist, create a new file using the file name provided by the user and store the records into this file.
        else: 
            csvFile = open(fileName, 'w', newline='', encoding='utf-8')
       
        try:
            with csvFile:
                
                ##Allows us to write to the file.
                writer = csv.writer(csvFile, delimiter=',')
                
                ##If file does not exist, use the first row as the header names for each column.
                if fileExists == False:
                    header = ['id', 'date', 'cases', 'deaths', 'name_fr', 'name_en']
                        
                    writer.writerow(header)
                
                ##For the number of records that exist,
                for i in range(len(self.covidModels)) :
                    ##Store each record to CovidRecord.
                    CovidRecord = self.covidModels[i]
                    
                    ##Format and store all the records into the records list.
                    records = [CovidRecord.getID(), CovidRecord.getDate(), CovidRecord.getCases(), CovidRecord.getDeaths(), 
                                CovidRecord.getNameFr(), CovidRecord.getNameEn()]
                    
                    ##Writes the formatted records into the file. One record for each row.
                    writer.writerow(records)
                  
                ##Displays the completion message.      
                self.covidView.printCompletion("\nDate set saved to file.")
         
        ##Handles any errors when reading the file.        
        except IOError as e :
            print(e)
                
    def exit(self):
        '''
        Exit out of the program.
        '''
        
        ##Displays completion message.
        self.covidView.printCompletion("\nExited Program.")
        
        ##Terminates the running program.
        exit
                
    def displayFromDatabase(self, DBname):
        '''
        Displays the record menu to determine how many records the user would like to see. Starting from the first record. 
        Records displayed are from the database.
        '''
        
        ##Stores the number of records the user wants to see.
        numRecords = self.covidView.userNumericPrompt("\nHow many records would you like to view? ")
        
        ##Checks if numRecords is an integer.
        if isinstance(numRecords, int):
            
            try:
                ##Connects to the database.
                connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
                
                ##Allows us to manipulate the database.
                cursor = connection.cursor();
                
                ##Database query that selects all information from the table. In this case,
                ##it will be used to determine the number of rows in the database.
                numOfRecordsQuery = "SELECT * FROM covidcases"
                
                ##Executes the Query.
                cursor.execute(numOfRecordsQuery)
                
                ##Gathers all the records in the database.
                numOfRecordsInDatabase = cursor.fetchall()
                
                ##Determines if the number of records the user wants to see is more than what is stored in the database.
                if numRecords > len(numOfRecordsInDatabase):
                    
                    ##Displays an error message.
                    self.covidView.printError("\nInsufficient records.")
                    return
                
                ##Database query that selects all information from the table.
                selectQuery = "SELECT * FROM covidcases"
                
                ##Executes the Query
                cursor.execute(selectQuery)
                
                ##Gathers a certain number of records in the database that the user wants to see.
                records = cursor.fetchmany(numRecords)
                
                ##Formats and displays the records.
                for row in records:
                                                
                    rowID = row[0]
                    rowDate = row[1]
                    rowCases = row[2]
                    rowDeaths = row[3]
                    rowNameFR = row[4]
                    rowNameEN = row[5]
                        
                    covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)
                    
                    ##Prints out the records.
                    self.covidView.printRecord(covidModel)
                 
                ##Closes connection.    
                connection.close()
            
            ##Handles any errors.       
            except mysql.connector.Error as error:
                
                ##Displays error message.
                self.covidView.printError("\nFailed to display records from the database table: {}".format(error))

    def databaseCreateRecord(self, DBname):
        '''
        Creates a record in the database based of user input.
        '''
        
        print("\nPlease enter the following information about the record you would like to create.")
    
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")
        
        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
        
        ##Store and pass all the user input to the __init__() method in CovidModels.
        covidModel = CovidModel(countryID, date, cases, deaths, nameFR, nameEN)

        try:
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.    
            cursor = connection.cursor();
            
            ##Database insert query that will insert a record of information into the database.    
            insertQuery = "INSERT INTO covidcases (id, date, cases, deaths, name_fr, name_en) VALUES (%s, %s, %s, %s, %s, %s)"
            
            ##Format and store all the records into the records list.
            records = [covidModel.getID(), covidModel.getDate(), covidModel.getCases(), covidModel.getDeaths(), 
                        covidModel.getNameFr(), covidModel.getNameEn()]
            
            ##Executes the Query
            cursor.execute(insertQuery, records)
            
            ##Commits the transactions.
            connection.commit()
            
            ##Closes the connection.
            connection.close()
            
            ##Displays a completion message.
            self.covidView.printCompletion("\nRecord created in database.")
            return
           
        ##Handles any errors.            
        except mysql.connector.Error as error:
            
            ##Displays error message.
            self.covidView.printError("\nFailed to create the record in the database table: {}".format(error))
                
    def databaseUpdateRecord(self, DBname):
        '''
        Based of user input, we find a match in the database and edit that specific record.
        '''
        
        print("\nPlease enter the following information about the record you would like to edit.")
        
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")

        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
        
        covidModel = CovidModel(countryID, date, cases, deaths, nameFR, nameEN)
                                
        try:
            ##Boolean variable initialized to be false.
            recordFound = False
            
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.        
            cursor = connection.cursor();
            
            ##Database select query that will locate the specific record in the database using the user input.    
            selectQuery = "SELECT * FROM covidcases WHERE id = %s and date = %s and cases = %s and deaths = %s and name_fr = %s and name_en = %s"
            
            ##Format and store all the records into the records list.
            records = [covidModel.getID(), covidModel.getDate(), covidModel.getCases(), covidModel.getDeaths(), 
                        covidModel.getNameFr(), covidModel.getNameEn()]
            
            ##Executes the query.
            cursor.execute(selectQuery, records)
            
            ##Gathers all the records in the database that match the user's input.
            records = cursor.fetchall()
            
            ##Formats and displays the records.    
            for row in records:
                                                
                rowID = row[0]
                rowDate = row[1]
                rowCases = row[2]
                rowDeaths = row[3]
                rowNameFR = row[4]
                rowNameEN = row[5]
                        
                covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)

                ##Prints out the records.
                self.covidView.printRecord(covidModel)  
                
                ##Changes the variable to true since records were found. 
                recordFound = True
            
            ##If no records in the database match the user's input, the boolean variable stays false.    
            if recordFound == False:
                
                ##Displays error message.
                self.covidView.printError("\nNo record found in the database.")
            
            ##If records in the database match the user's input, we display a prompt to the user.    
            elif recordFound == True:
                
                ##If match found, display the edit record menu.
                editFieldsString = self.covidView.editRecordMenu()
                
                ##Split the user input.
                editFields = editFieldsString.split(',')
                
                ##Variables that will eventually hold user input.
                newID = ""
                newDate = ""
                newCases = ""
                newDeaths = ""
                newNameFR = ""
                newNameEN = ""
                
                ##Starts the beginning of the database update query.
                updateQuery = "UPDATE covidcases SET"
                
                ##Store the strings in field.
                for field in editFields:
                    
                    ##If user entered id, prompt for a new Country ID. Also, add the new Country ID to the update query. 
                    if field.strip() == 'id':
                        newID = self.covidView.userPrompt("\nEnter New Country ID: ")
                        updateQuery = updateQuery + " id = %(newID)s,"

                    ##If user entered date, prompt for a new Date. Also, add the new date to the update query.
                    if field.strip() == 'date':
                        newDate = self.covidView.userPrompt("Enter New Date (YYYY-MM-DD): ")
                        updateQuery = updateQuery + " date = %(newDate)s,"
                        
                    ##If user entered cases, prompt for a new Number of Cases. Also, add the new Number of Cases to the update query.
                    if field.strip() == 'cases':
                        newCases = self.covidView.userPrompt("Enter New Number of Cases: ")
                        updateQuery = updateQuery + " cases = %(newCases)s,"
                        
                    ##If user entered deaths, prompt for a new Number of Deaths. Also, add the new Number of Deaths to the update query.
                    if field.strip() == 'deaths':
                        newDeaths = self.covidView.userPrompt("Enter New Number of Deaths: ")
                        updateQuery = updateQuery + " deaths = %(newDeaths)s,"
                        
                    ##If user entered name_fr, prompt for a new Country Name in French. Also, add the new Country Name in French to the update query.
                    if field.strip() == 'name_fr':
                        newNameFR = self.covidView.userPrompt("Enter New Country Name in French: ")
                        updateQuery = updateQuery + " name_fr = %(newNameFR)s,"
                    
                    ##If user entered name_en, prompt for a new Country Name in English. Also, add the new Country Name in English to the update query.
                    if field.strip() == 'name_en':
                        newNameEN = self.covidView.userPrompt("Enter New Country Name in English: ")
                        updateQuery = updateQuery + " name_en = %(newNameEN)s,"
                
                ##Removes the last comma in the update query.        
                updateQuery = updateQuery[0:len(updateQuery)-1]
                
                ##Variables that hold the user's input that will be used in the update query.       
                originalId = covidModel.getID()
                origDate = covidModel.getDate()
                origCases = covidModel.getCases()
                origDeaths = covidModel.getDeaths()
                origNameFR = covidModel.getNameFr()
                origNameEN = covidModel.getNameEn()
                
                ##Database update query that will be used to edit an existing record in the database.
                updateQuery = updateQuery + "WHERE id = %(origID)s and date = %(origDate)s and cases = %(origCases)s and deaths = %(origDeaths)s and name_fr = %(origNameFR)s and name_en = %(origNameEN)s"
                
                ##A dictionary that will be used to place the values in the correct spots in the update query.
                covidModelDict = {'newID': newID, 'newDate': newDate, 'newCases': newCases, 'newDeaths': newDeaths, 'newNameFR': newNameFR,
                                   'newNameEN': newNameEN, 'origID': originalId, 'origDate': origDate, 'origCases': origCases, 'origDeaths': origDeaths,
                                   'origNameFR': origNameFR, 'origNameEN': origNameEN}
                
                ##Executes the query.
                cursor.execute(updateQuery, covidModelDict)  
                
                ##Commits the transactions.
                connection.commit()
                
                ##Closes the connection.
                connection.close()   

                ##Displays completion message.
                self.covidView.printCompletion("\nRecord in database has been edited.")
                     
        ##Handles any errors.               
        except mysql.connector.Error as error:
            
            ##Displays error message.
            self.covidView.printError("\nFailed to update the record in the database table: {}".format(error))                 
                
    def databaseDeleteRecord(self, DBname):
        '''
        Based of user input, we will find a match in the database and delete the record.
        '''
        
        print("\nPlease enter the following information about the record you would like to delete.")
        
        ##Stores the Country ID.
        countryID = self.covidView.userPrompt("\nEnter Country ID: ")
        
        ##Stores the Date.
        date = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")

        ##Checks that the format of the date is correct.
        regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])?$'
        matchDate = re.compile(regex).match(date)
        
        ##If the date is the wrong format or date is not valid, display an error message.
        if matchDate is None:
            self.covidView.printError("Wrong format or date is not valid.")
            return
        
        ##Stores the Number of Cases.
        cases = self.covidView.userPrompt("Enter Number of Cases: ")
        
        ##Stores the Number of Deaths.
        deaths = self.covidView.userPrompt("Enter Number of Deaths: ")
        
        ##Stores the Country Name in French.
        nameFR = self.covidView.userPrompt("Enter Country Name in French: ")
        
        ##Stores the Country Name in English.
        nameEN = self.covidView.userPrompt("Enter Country Name in English: ")
        
        covidModel = CovidModel(countryID, date, cases, deaths, nameFR, nameEN)
                                
        try:
            ##Boolean variable initialized to be false.
            recordFound = False
            
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.        
            cursor = connection.cursor();
            
            ##Database select query that will locate the specific record in the database using the user input.    
            selectQuery = "SELECT * FROM covidcases WHERE id = %s and date = %s and cases = %s and deaths = %s and name_fr = %s and name_en = %s"
            
            ##Format and store all the records into the records list.
            records = [covidModel.getID(), covidModel.getDate(), covidModel.getCases(), covidModel.getDeaths(), 
                        covidModel.getNameFr(), covidModel.getNameEn()]
            
            ##Executes the query.
            cursor.execute(selectQuery, records)
            
            ##Gathers all the records in the database that match the user's input.
            records = cursor.fetchall()
            
            ##Formats and displays the records.    
            for row in records:
                                                
                rowID = row[0]
                rowDate = row[1]
                rowCases = row[2]
                rowDeaths = row[3]
                rowNameFR = row[4]
                rowNameEN = row[5]
                        
                covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)

                ##Prints out the records.
                self.covidView.printRecord(covidModel)  
                
                ##Changes the variable to true since records were found. 
                recordFound = True
            
            ##If no records in the database match the user's input, the boolean variable stays false.    
            if recordFound == False:
                
                ##Displays error message.
                self.covidView.printError("\nNo record found in the database.")
            
            ##If records in the database match the user's input, we display a prompt to the user.    
            elif recordFound == True:
               
                ##Confirms that the user wants to delete the record.
                confirm = self.covidView.userPrompt("\nAre you sure you want to delete the record (Y/N)? ")   
                
                ##Checks if the user selects 'Y'.
                if confirm.lower()[0] == 'y':  
                    
                    ##Database delete query that will use the user's input to delete the record in the database.
                    deleteQuery = "DELETE FROM covidcases WHERE id = %s and date = %s and cases = %s and deaths = %s and name_fr = %s and name_en = %s"
                    
                    ##Variables that hold the user's input that will be used in the delete query.   
                    deleteId = covidModel.getID()
                    deleteDate = covidModel.getDate()
                    deleteCases = covidModel.getCases()
                    deleteDeaths = covidModel.getDeaths()
                    deleteNameFR = covidModel.getNameFr()
                    deleteNameEN = covidModel.getNameEn()
                    
                    ##Execute the query
                    cursor.execute(deleteQuery, (deleteId, deleteDate, deleteCases, deleteDeaths, deleteNameFR, deleteNameEN))  
                    
                    ##Commits the transactions.
                    connection.commit()
                    
                    ##Closes the connection.
                    connection.close() 

                    ##Displays completion message.
                    self.covidView.printCompletion("\nRecord has been deleted from the database.")
        
        ##Handles any errors.                
        except mysql.connector.Error as error:
            
            #Displays error message.
            self.covidView.printError("\nFailed to delete the record in the database table: {}".format(error))  
                
    def loadFromDatabase(self, DBname):
        '''
        Loads records from the database to the in-memory data.
        '''
        
        ##Clears the in-memory data.
        self.covidModels.clear()
        
        ##Following assignment 2, we will only load 100 records from the database. 
        numRecords = 100    
        
        try:
            
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.        
            cursor = connection.cursor();
                
            ##Database query that selects all information from the table.
            selectQuery = "SELECT * FROM covidcases"
                
            ##Executes the Query
            cursor.execute(selectQuery)
            
            ##Gathers only 100 records from the database.
            records = cursor.fetchmany(numRecords)
                
            ##Formats and stores each record into the data structure.
            for row in records:
                                                
                    rowID = row[0]
                    rowDate = row[1]
                    rowCases = row[2]
                    rowDeaths = row[3]
                    rowNameFR = row[4]
                    rowNameEN = row[5]
                        
                    covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)
                        
                    ##Appends each record loaded from the database to the list.
                    self.covidModels.append(covidModel)
             
            ##Closes the connection.        
            connection.close()     
                         
            ##Displays completion message.
            self.covidView.printCompletion("\nData set loaded from database.")    
        
        ##Handles any errors.            
        except mysql.connector.Error as error:
            
            ##Displays error message.
            self.covidView.printError("\nFailed to load records in the database table: {}".format(error))     
                
    def saveToDatabase(self, DBname):
        
        try:
            
            ##Creates a database and a table when the user saves for the first time.
            self.initalizeDb(DBname)
            
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.        
            cursor = connection.cursor();
                
            ##For the number of records that exist in the data structure,
            for i in range(len(self.covidModels)):
                ##Store each record to CovidRecord.
                CovidRecord = self.covidModels[i]
                    
                ##Format and store all the records into the records list.
                records = [CovidRecord.getID(), CovidRecord.getDate(), CovidRecord.getCases(), CovidRecord.getDeaths(), 
                            CovidRecord.getNameFr(), CovidRecord.getNameEn()]
                
                ##Database insert query that will be used to insert all the in-memory data to the database.
                insertQuery = "INSERT INTO covidcases (id, date, cases, deaths, name_fr, name_en) VALUES (%s, %s, %s, %s, %s, %s)"
                
                ##Executes the query.
                cursor.execute(insertQuery, records)
                
                ##Commits the transactions.
                connection.commit()
            
            ##Closes the connection.
            connection.close() 
                  
            ##Displays completion message.      
            self.covidView.printCompletion("\nData set saved to database.")
        
        ##Handles any errors.            
        except mysql.connector.Error as error:
            
            ##Displays error message.
            self.covidView.printError("\nFailed to save records in the database table: {}".format(error))  
            
    def initalizeDb(self, DBname):
        '''
        Creates a database and a table.
        '''
        
        ##Connects to the connection.
        connection = mysql.connector.connect(host='localhost', user='root')
        
        ##Allows us to manipulate the database.
        cursor = connection.cursor(buffered=True) 
        
        ##Database show database query that will find all the databases in MySQL.
        showDatabases = "SHOW DATABASES"
        
        ##Executes the query.
        cursor.execute(showDatabases)
        
        ##Boolean variable initialized to false.
        databaseFound = False
        
        ##Finds out if the database being used in the program already exists or not.
        for x in cursor:
            if x[0] == DBname:
                databaseFound = True
                break
            
        ##If database is not found, display a completion message with the database name. 
        if databaseFound == False:
            self.covidView.printCompletion("\nDatabase: '" + DBname + "' created.")
        
        ##Database create query that will create a database if it does not already exist.    
        createDbQuery = "CREATE DATABASE IF NOT EXISTS " + DBname 
        
        ##Executes the query.
        cursor.execute(createDbQuery)
        
        ##Connects to the database.
        connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
        
        ##Allows us to manipulate the database.
        cursor = connection.cursor(buffered=True) 
        
        ##Database show tables query that will find all the tables that are in this database in MySQL.
        showTables = "SHOW TABLES"
        
        ##Executes the query.
        cursor.execute(showTables)
        
        ##Boolean variable initialized to false.
        tableFound = False
        
        ##Finds out if the table being used in the program already exists or not.
        for x in cursor:
            if x[0] == 'covidcases':
                tableFound = True
                break
        
        ##If table is not found, display a completion message with the table name.     
        if tableFound == False:
            self.covidView.printCompletion("\nTable: 'covidcases' created.")
            
        ##Database create query that will be used to create a table in the database in MySQL if it does not already exist.
        createTableQuery = '''CREATE TABLE IF NOT EXISTS `covidcases` (
                              `id` varchar(2) NOT NULL,
                              `date` varchar(10) DEFAULT NULL,
                              `cases` varchar(7) DEFAULT NULL,
                              `deaths` varchar(7) DEFAULT NULL,
                              `name_fr` varchar(60) DEFAULT NULL,
                              `name_en` varchar(60) DEFAULT NULL
                            );
                            '''
        
        ##Executes the query.
        cursor.execute(createTableQuery)
        
        ##Closes the connection.
        connection.close()
        
    def findRecordsFromDatabase(self, DBname):
        '''
        Finds specific records in the database based of user input. 
        '''
        
        try:
            ##Boolean variable initialized to be false.
            recordFound = False
            
            ##Connects to the database.
            connection = mysql.connector.connect(host='localhost', database=DBname, user='root')
            
            ##Allows us to manipulate the database.        
            cursor = connection.cursor();
            
            ##Gets the user's selection for the WHERE clause in the SELECT query.
            findFieldStrings = self.covidView.findRecordMenu()
         
            ##Split the user input.
            addFields = findFieldStrings.split(',')
                
            ##Variables that will eventually hold user input.
            oldID = ""
            oldDate = ""
            oldCases = ""
            oldDeaths = ""
            oldNameFR = ""
            oldNameEN = ""
                
            ##Starts the beginning of the database select query.
            searchQuery = "SELECT * FROM covidcases WHERE"
                
            ##Store the strings in field.
            for field in addFields:
                    
                ##If user entered id, prompt for a Country ID. Also, add the Country ID to the select query. 
                if field.strip() == 'id':
                    oldID = self.covidView.userPrompt("\nEnter Country ID: ")
                    searchQuery = searchQuery + " id = %(oldID)s and"

                ##If user entered date, prompt for a Date. Also, add the date to the select query.
                if field.strip() == 'date':
                    
                    ##Gets the user's selection of how to search for the record.
                    query = self.covidView.queryMenu()
                    
                    ##If the user selects 1, we will get the input and search for less than.
                    if query == '1':
                        
                        oldDate = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")
                        searchQuery = searchQuery + " date < %(oldDate)s and"
                    
                    ##If the user selects 2, we will get the input and search for equals.
                    elif query == '2':
                
                        oldDate = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")
                        searchQuery = searchQuery + " date = %(oldDate)s and"
                    
                    ##If the user selects 3, we will get the input and search for greater than.    
                    elif query == '3':
                        
                        oldDate = self.covidView.userPrompt("Enter Date (YYYY-MM-DD): ")
                        searchQuery = searchQuery + " date > %(oldDate)s and"
                        
                ##If user entered cases, prompt for a Number of Cases. Also, add the Number of Cases to the select query.
                if field.strip() == 'cases':
                    oldCases = self.covidView.userPrompt("Enter Number of Cases: ")
                    searchQuery = searchQuery + " cases = %(oldCases)s and"
                        
                ##If user entered deaths, prompt for a Number of Deaths. Also, add the Number of Deaths to the select query.
                if field.strip() == 'deaths':
                    oldDeaths = self.covidView.userPrompt("Enter Number of Deaths: ")
                    searchQuery = searchQuery + " deaths = %(oldDeaths)s and"
                        
                ##If user entered name_fr, prompt for a Country Name in French. Also, add the Country Name in French to the select query.
                if field.strip() == 'name_fr':
                    oldNameFR = self.covidView.userPrompt("Enter Country Name in French: ")
                    searchQuery = searchQuery + " name_fr = %(oldNameFR)s and"
                    
                ##If user entered name_en, prompt for a Country Name in English. Also, add the Country Name in English to the select query.
                if field.strip() == 'name_en':
                    oldNameEN = self.covidView.userPrompt("Enter Country Name in English: ")
                    searchQuery = searchQuery + " name_en = %(oldNameEN)s and"
        
            ##Removes the last 'and' in the select query.        
            searchQuery = searchQuery[0:len(searchQuery)-4]
            
            ##A dictionary that will be used to place the values in the correct spots in the select query.
            covidModelDict = {'oldID': oldID, 'oldDate': oldDate, 'oldCases': oldCases, 'oldDeaths': oldDeaths, 'oldNameFR': oldNameFR,
                              'oldNameEN': oldNameEN}
            
            ##Executes the query.    
            cursor.execute(searchQuery, covidModelDict)
            
            ##Gets all the records associated with the select query.
            records = cursor.fetchall()
            
            ##Formats and displays the records.
            for row in records:
                                                
                rowID = row[0]
                rowDate = row[1]
                rowCases = row[2]
                rowDeaths = row[3]
                rowNameFR = row[4]
                rowNameEN = row[5]
                        
                covidModel = CovidModel(rowID, rowDate, rowCases, rowDeaths, rowNameFR, rowNameEN)
                
                ##Prints out the records.
                self.covidView.printRecord(covidModel)
                
                ##Changes the variable to true since records were found. 
                recordFound = True
                
            ##If no records in the database match the user's input, the boolean variable stays false.    
            if recordFound == False:
                
                ##Displays error message.
                self.covidView.printError("\nNo record(s) found in the database.")
                
            ##Closes the connection.
            connection.close() 
        
        ##Handles any errors.            
        except mysql.connector.Error as error:
            
            ##Displays error message.
            self.covidView.printError("\nFailed to find records in the database table: {}".format(error))  