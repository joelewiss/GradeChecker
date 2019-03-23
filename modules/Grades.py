from html.parser import HTMLParser

class GradeParser(HTMLParser):
    atTable = False    

    def handle_starttag(self, tag, attr):
        if atTable:
            pass
        else:
            pass

    def handle_data(data):
        if atTable:
            print(data)

    def handle_comment(data):
        if data == " end #sidebar1 ":
            atTable = true
        

def parseGrades(html):
    pass
