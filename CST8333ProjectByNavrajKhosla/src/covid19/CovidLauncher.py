'''
Created on Oct. 8, 2020

@author: Khosla
'''

from covid19.Controller.CovidController import CovidController

def main():
    '''
    Creates an instance of CovidController() and calls the launch method.
    '''   
    covidController = CovidController()  
    covidController.launch()  
        
if __name__ == '__main__':
    '''
    Calls the main method. 
    '''
    main()
        