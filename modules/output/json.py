import json

class GradeEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"Course": obj.course,
                "Title": obj.title,
                "Letter": obj.letter,
                "Score": obj.score,
                "Teacher": obj.teacher
               }

def output(grades):
    print(json.dumps(grades, cls=GradeEncoder))
