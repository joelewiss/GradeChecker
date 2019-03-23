def output(grades):
    for grade in grades:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(grade.course, grade.title, grade.letter, grade.score, grade.teacher))
