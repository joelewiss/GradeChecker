from http import client
from modules import Data
from urllib import parse
import ssl, json, time

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
        print("We have a valid cookie: " + cookie)

    #Make a request to assignment schedule and return the response
    connection = client.HTTPSConnection(cfg["Connection"]["Host"], context=sslContext)
    connection.request("GET", cfg["Connection"]["Assignment"], headers={"Cookie":cookie})
    response = connection.getresponse()
    return response.read()


def cookieIsValid(cookie):
    """Check validity of cookie by performing a get request on the assignmentschedule url"""

    host = cfg["Connection"]["Host"]
    connection = client.HTTPSConnection(host, context=sslContext)
    connection.request("HEAD", cfg["Connection"]["Assignment"], headers={"Cookie":cookie})
    code = connection.getresponse().status

    if code == 302:
        return False
    elif code == 200:
        return True
    else:
        raise Exception("Unexpected return code from parentconnect: " + str(code))

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
    connection = client.HTTPSConnection(host, context=sslContext, timeout=5)
    connection.request("GET", "/")
    response = connection.getresponse()
    cookie = response.getheader("Set-Cookie").split(";")[0]

    print(cookie)
    print("\nIs cookie valid?")
    print(cookieIsValid(cookie))

    #Next, perform a login request via POST
    data = getData(1)
    print("\nTrying to login...")
    
    #connection = client.HTTPSConnection(host, context=sslContext, timeout=5)
    #connection.request("POST", "/WebService/OCE_ws.asmx/CheckUpdateAccountInfo", body=data, headers=Data.connection1)
    #print(connection.getresponse().status)
 
    connection = client.HTTPSConnection(host, context = sslContext, timeout=5)
    data = getData(2)
    head = Data.connection2
    head["Cookie"] = cookie
    connection.request("POST", cfg["Connection"]["Login"], body=data, headers=head) 
    connection.getresponse()
    
    connection = client.HTTPSConnection(host, context=sslContext, timeout=5)
    connection.request("GET", cfg["Connection"]["Home"], headers={"Cookie":cookie})
    connection.getresponse()    

 
    if cookieIsValid(cookie):
        return cookie
    else:
        raise Exception("Unable to obtain valid cookie")   

def getData(connection):
    """Constructs a special data string for submition to server"""
    if connection == 1:
        base = Data.base
        data = json.loads(base)
        data["acctParms"]["acctName"] = cfg["Login"]["Username"]
        data["acctParms"]["valuePwdOld"] = cfg["Login"]["Password"]
        return json.dumps(data)
    elif connection == 2:
        data = parse.urlencode({"RegisterMe":1, "UserID":cfg["Login"]["Username"], "UserPwd":cfg["Login"]["Password"]})
        return data

def writeCookie(cookie):
    """Once a valid cookie is known, it should be written to disk for later use"""
    pass
