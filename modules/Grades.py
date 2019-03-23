from html.parser import HTMLParser

class GradeParser(HTMLParser):    

    def __init__(self):
        self.atgradetable = False
        self.gradestring = ""
        super().__init__()

    def handle_starttag(self, tag, attr):
        #Why does it give me a one length list with a tuple inside of it???
        
        if len(attr) > 0:
            attr = attr[0]
        
        if (len(attr) > 1) and (attr[1] == "clIGPClassGrdTbl"):
            self.atgradetable = True

    def handle_data(self, data):
        if self.atgradetable:
            self.gradestring += data + "\n"

class Grade():
    """Defines a grade object with the following attributes

    course(str) Course number
    title(str) Course title
    letter(str) Grade letter
    score(int) Percentage score
    teacher(str) Teacher name
    """

def parseGrades(config, html):
    #Strip all of the unneeded characters from the html
    html = html.replace(b"\r\n", b"")
    html = html.replace(b"\t", b"")
    html = html.replace(b"<br />", b"")
    html = html.decode()  

    parser = GradeParser()
    parser.feed(html)
    gradestrings = parser.gradestring.split("\n")

    grades = []    

    index = 0
    for string in gradestrings:
        if (index < 5):
            pass
        elif int(index / 5) <= int(config["Grades"]["Number"]):
            id = index % 5
            if id == 0:
                grades.append(Grade())
                grades[-1].course = string
            elif id == 1:
                grades[-1].title = string
            elif id == 2:
                grades[-1].letter = string
            elif id == 3:
                grades[-1].score = int(float(string))
            elif id == 4:
                grades[-1].teacher = string

        index += 1

    return grades
