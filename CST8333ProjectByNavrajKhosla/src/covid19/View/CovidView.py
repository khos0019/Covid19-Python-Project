'''
Created on Oct. 7, 2020
Updated on Nov. 29, 2020

@author: Khosla
'''

class CovidView():
    '''
    Controls and showcases what the user will see when interacting with the menus and prompts.  
    '''
    
    ##Variable choice will hold an integer.
    choice: int   
    
    def displayMenu(self):
        '''
        Displays a menu for the user to interact with.
        '''
        
        ##Choice is initialized to be equal to zero.
        choice = 0
       
        ##Prints out the options for the user to see.
        print("\n1. Display Records")
        print("2. Display Specific Record(s) from Database")
        print("3. Create a Record")
        print("4. Edit a Record")
        print("5. Delete a Record")
        print("6. Load Records")
        print("7. Save Records")
        print("8. Exit")
     
        ##Try until a valid choice has been entered by the user.
        try: 
            ##Stores the users input into choice.
            choice = self.userNumericPrompt("\nEnter a selection from the menu: ")
            
            ##If user inputs a invalid choice, throw the ValueError Exception.
            if choice < 0 and choice > 8: 
                raise ValueError
            return choice
        
        ##Handles any errors when user enters an invalid choice.    
        except ValueError:
            self.printError("Please enter a valid choice.")
    
    def editRecordMenu(self):
        '''
        Displays a prompt to gather information of which field the user wants to change.
        '''
        
        ##Prints out the fields for the user to choose from.
        print("\nEnter the field(s) you would like to edit from the following list: [id, date, cases, deaths, name_fr, name_en]")
        ##Stores the users input of which field to edit.
        fields = self.userPrompt("\nInput each field separated by a comma (Ex.id, date): ")

        return fields
    
    def findRecordMenu(self):
        '''
        Displays a prompt to gather information of which field to use to search for records in the database.
        '''
        
        ##Prints out the fields for the user to choose from.
        print("\nEnter the field(s) you would like to use to search for record(s) from the following list: [id, date, cases, deaths, name_fr, name_en]")
        ##Stores the users input of which field to use.
        fields = self.userPrompt("\nInput each field separated by a comma (Ex.id, date): ")
        
        return fields
    
    def queryMenu(self):
        '''
        Displays a prompt to determine how the user wants to search.
        '''
        
        ##Asks the user to select from the following selection.
        print("\nEnter how you would like to search for the record(s):")
        
        ##Prints out a selection to manipulate the query.
        print("\n1. Less Than")
        print("2. Equals To")
        print("3. Greater Than")
        
        ##Stores the users input of which query to use.
        selection = self.userPrompt("\nInput the number associated with the selection (Ex. 1): ")
        
        return selection
    
    def userPrompt(self, prompt):
        '''
        A method that allows other classes to call it if user input is needed to be stored.
        '''
        
        ##Stores the user input into userInput as a string.
        userInput = input(prompt)
        return userInput
    
    def printError(self, error):
        '''
        A method that allows other classes to call it if an error message needs to be printed out.
        '''
        
        ##Prints the error message.
        print(error)
        
    def printCompletion(self, complete):
        '''
        A method that allows other classes to call it if a completion message needs to be printed out.
        '''
        
        ##Prints the completion message.
        print(complete)
            
    def userNumericPrompt(self, prompt): 
        '''
        A method that allows other classes to call it if user input is needed to be stored.
        '''
        
        ##Stores the user input into userInput as a string.
        userInput = input(prompt)
        
        ##Try until a valid number has been inputed by the user.
        try:
            ##Changes the stored string in userInput into an integer and stores that integer into choice.
            choice = int(userInput)
            return choice
        
        ##Handles any errors when the user does not enter a number.
        except ValueError:
            self.printError("Please enter a number.")
            
    def printRecord(self, covidRecord):
        '''
        Formats and displays a record's information.
        '''
        
        ##Prints out all the information of a record for the user to see.
        print("\nID = " + covidRecord.getID() + "\n" + "DATE = " + covidRecord.getDate() + "\n" + "CASES = " + covidRecord.getCases() + "\n"
          + "DEATHS = " + covidRecord.getDeaths() + "\n" + "NAME_FR = " + covidRecord.getNameFr() + "\n" + "NAME_EN = " 
          + covidRecord.getNameEn())       