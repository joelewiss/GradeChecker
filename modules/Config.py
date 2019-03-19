import configparser

"""Simple module for getting the configuration file for the program

Can be called with an optional argument specifying file location
Path to configuration should be supplied as a command line argument to the main script
"""

def getConfig(location = "../GradeChecker.conf"):
    configuration = configparser.ConfigParser()
    configuration.read(location)
    return configuration 
