'''
Created on Oct. 14, 2020
Updated on Nov. 8, 2020

@author: Khosla
'''

import unittest
from covid19.Controller.CovidController import CovidController
from covid19.View.CovidView import CovidView
import mysql.connector


class Test(unittest.TestCase):
    '''
    Tests a newly implemented method in CovidController.
    '''
    
    def setUp(self):
        '''
        Before doing the test, we will create a database and a table inside that database.
        '''
        
        ##Creates a new instance of CovidView().
        self.covidView = CovidView()
        
        ##Connects to the connection.
        self.connection = mysql.connector.connect(host='localhost', user='root')
        
        ##Allows us to manipulate the database.        
        self.cursor = self.connection.cursor();
        
        ##Database create query that will create a database if does not already exist.
        createDbQuery = "CREATE DATABASE IF NOT EXISTS testDB"
        
        ##Executes the query.
        self.cursor.execute(createDbQuery)
        
        ##Displays completion message.
        self.covidView.printCompletion("Database created.")
        
        ##Connects to the database.
        self.connection = mysql.connector.connect(host='localhost', database='testDB', user='root')
        
        ##Allows us to manipulate the database.  
        self.cursor = self.connection.cursor();
        
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
        self.cursor.execute(createTableQuery)
        
        ##Displays a completion message.
        self.covidView.printCompletion("\nTable created.")
    
    def tearDown(self):
        '''
        After doing the test, we will remove the database from MySQL.
        '''
        
        ##Database delete query that will remove the database in MySQL. 
        deleteDbQuery = "DROP DATABASE IF EXISTS testDB"
        
        ##Executes the query.
        self.cursor.execute(deleteDbQuery)
        
        ##Displays completion message.
        self.covidView.printCompletion("\nDatabase deleted.")
    
        
    def test_NewRecord(self):
        '''
        Creates a new record in the table.
        '''
        
        ##Creates a new instance of CovidController().
        covidController = CovidController()
        
        ##Database query that selects all information from the table. In this case,
        ##it will be used to determine the number of rows in the database.
        numOfRecordsQuery = "SELECT * FROM covidcases"
        
        ##Executes the Query.
        self.cursor.execute(numOfRecordsQuery)
        
        ##Gathers all the records in the database.
        recordsInDatabase = self.cursor.fetchall()
                
        ##The database should be empty as we have not created a record for the table yet.
        self.assertTrue(len(recordsInDatabase) == 0)
        
        ##Closes the connection.
        self.connection.close()
        
        ##Connects to the database.
        self.connection = mysql.connector.connect(host='localhost', database='testDB', user='root')
        
        ##Allows us to manipulate the database.  
        self.cursor = self.connection.cursor();
        
        ##Calls the databaseCreateRecord() method and uses the newly created database, 'testDB'.
        covidController.databaseCreateRecord('testDB')
        
        ##Executes the query.
        self.cursor.execute(numOfRecordsQuery)
        
        ##Gathers all the records in the database.
        recordsInDatabase = self.cursor.fetchall()
        
        ##A record has now been added to the table, so it should no longer be equal to 0.        
        self.assertFalse(len(recordsInDatabase) == 0)
        
        ##A record has been added to the table, so it should be equal to 1.
        self.assertTrue(len(recordsInDatabase) == 1)
        
if __name__ == '__main__':
    '''
    Calls the main() method in unittest.
    '''
    unittest.main()
