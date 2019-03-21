from urllib import request as url
from modules import Cookie
import ssl, json

"""Connection module for Joe's Grade Checker

Handles all the work relating to establishing a connection with the parentconnect servers and getting data
DOES NOT parse any html or any other related grade function
This is all handled by the Grades module

Procedure for how this script should go
Load cookie from stored file and check if still valid
if not, procede to login with new cookie
get AssignmentSchedule.asp and pass html to grade parser
"""

sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

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
        cookie = getNewCookie()

def cookieIsValid(cookie):
    """Check validity of cookie by performing a get request on the assignmentschedule url"""

    host = cfg["Connection"]["Host"] + cfg ["Connection"]["Assignment"]
    
    print(host)

def getNewCookie():
    """Obtains a new, authenticated sessionid (cookie) to use when retreiving grades and such
    
    Should go as follows:
    Make a simple get request to the root and store the given sessionid
    Make a post request to the login url with the user's username and password
    Then check if the given cookie is valid or not
    If it is, contine execution
    If its not, throw an exception and stop program
    """
    
    #First, get sessionid by making a GET request
    host = cfg["Connection"]["Host"]
    request = url.urlopen(host, context = sslContext)
    sessionid = request.getheader("Set-Cookie").split(";")[0]

    #Next, perform a login request via POST
    data = getData()

    print(data)

def getData():
    """Constructs a special data string for submition to server"""
    base = Cookie.base
    base = json.loads(base)
    base["acctParms"]["acctName"] = cfg["Login"]["Username"]
    base["acctParms"]["valuePwdOld"] = cfg["Login"]["Password"]

    print(json.dumps(base, indent=4))
