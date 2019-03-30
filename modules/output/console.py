def output(grades):
    print("Course\tTitle\tGrade\tScore\tTeacher")
    for grade in grades:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(grade.course, grade.title, grade.letter, grade.score, grade.teacher))
