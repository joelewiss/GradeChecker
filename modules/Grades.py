from html.parser import HTMLParser

class GradeParser(HTMLParser):    

    def __init__(self):
        self.atgradetable = False
        self.gradestrings = []
        super().__init__()

    def handle_starttag(self, tag, attr):
        #Why does it give me a one length list with a tuple inside of it???
        
        if len(attr) > 0:
            attr = attr[0]
        
        if (len(attr) > 1) and (attr[1] == "clIGPClassGrdTbl"):
            self.atgradetable = True

    def handle_data(self, data):
        if self.atgradetable:
            self.gradestrings.append(data)

class Grade():
    """Defines a grade object with the following attributes

    course(str)     Course number
    title(str)      Course title
    period(str)     Grading period
    letter(str)     Grade letter
    score(int)      Percentage score
    teacher(str)    Teacher name
    """

def parseGrades(config, html):
    #Strip all of the unneeded characters from the html
    html = html.replace(b"\r\n", b"")
    html = html.replace(b"\t", b"")
    html = html.replace(b"<br />", b"")
    html = html.decode() 

    parser = GradeParser()
    parser.feed(html)

    grades = []    

    for index in range(len(parser.gradestrings)):
        string = parser.gradestrings[index]

        id = index % 5
        if (index < 5):
            pass
        elif string.find("Italicized") == -1:
            #Every grade should have 5 associated attributes 
            if id == 0:
                #First is the course number
                grades.append(Grade())
                grades[-1].course = string
            elif id == 1:
                #Second is the course title, which needs to be split up
                string = string.split("(")
                grades[-1].title = string[0].strip()
                grades[-1].period = string[-1].replace(")", "")
            elif id == 2:
                #Third is the grade letter
                grades[-1].letter = string
            elif id == 3:
                #Fourth is the percentage score
                grades[-1].score = int(float(string))
            elif id == 4:
                #Fifth is the teacher, converted to upper case for consistency
                grades[-1].teacher = string.upper()
        else:
            break

    return grades
