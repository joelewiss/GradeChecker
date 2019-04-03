def output(grades):
    print("Course\tTitle\tPeriod\tGrade\tScore\tTeacher")
    for grade in grades:
        print("{0}\t{1}\t\t{2}\t{3}\t{4}\t{5}".format(grade.course, grade.title, grade.period, grade.letter, grade.score, grade.teacher))
