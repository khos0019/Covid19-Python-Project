'''
Created on Oct. 7, 2020

@author: Khosla
'''

class CovidModel():
    '''
    Our record object that will get all the information for each record.
    '''
    
    def __init__(self, id, date, cases, deaths, name_fr, name_en):
        '''
        Initializes all of the fields.
        '''

        self.id = id
        self.date = date
        self.cases = cases
        self.deaths = deaths
        self.name_fr = name_fr
        self.name_en = name_en
        
    def getID(self):
        '''
        Gets the Country ID.
        '''
        
        return self.id
    
    def setID(self, _id):
        '''
        Sets the Country ID.
        '''
        
        self.id = _id
    
    def getDate(self):
        '''
        Gets the Date.
        '''
        
        return self.date
    
    def setDate(self, _date):
        '''
        Sets the Date.
        '''
        
        self.date = _date
    
    def getCases(self):
        '''
        Gets the Number of Cases.
        '''
        
        return self.cases
    
    def setCases(self, _cases):
        '''
        Sets the Number of Cases.
        '''
        
        self.cases = _cases
    
    def getDeaths(self):
        '''
        Gets the Number of Deaths.
        '''
        
        return self.deaths
    
    def setDeaths(self, _deaths):
        '''
        Sets the Number of Deaths.
        '''
        
        self.deaths = _deaths
    
    def getNameFr(self):
        '''
        Gets the Country Name in French.
        '''
        
        return self.name_fr
    
    def setNameFr(self, _name_fr):
        '''
        Sets the Country Name in French.
        '''
        
        self.name_fr = _name_fr
    
    def getNameEn(self):
        '''
        Gets the Country Name in English.
        '''
        
        return self.name_en
    
    def setNameEn(self, _name_en):
        '''
        Sets the Country Name in English.
        '''
        
        self.name_en = _name_en