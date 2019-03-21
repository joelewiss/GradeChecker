from urllib import request
from ssl import SSLContext, PROTOCOL_SSLv23

"""Connection module for Joe's Grade Checker

Handles all the work relating to establishing a connection with the parentconnect servers and getting data
DOES NOT parse any html or any other related grade function
This is all handled by the Grades module

Procedure for how this script should go
Load cookie from stored file and check if still valid
if not, procede to login with new cookie
get AssignmentSchedule.asp and pass html to grade parser
"""

def readGrades(config):
    #Store config globally
    global cfg
    cfg = config

    #Load cookie from file, move on if file does not exist
    valid=False
    try:
        cookie = open("lastcookie", mode="r").readline()
        if cookieIsValid(cookie):
            valid=True
    except OSError:
        #File can't be opened (probably dosent exist)
        valid=False
    
    #If we don't have a valid cookie, get a new one by logging in
    if (not valid):
        cookie = getNewCookie(config)


def cookieIsValid(cookie):
    #TODO: write function
    pass

def getNewCookie(config):
    #TODO: write function
    pass 
