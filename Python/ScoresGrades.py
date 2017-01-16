print "Scores and Grades"
def scoresGrades():
    for count in range(10):
        score = -1
        while (score >= 60 and score <= 100):
            score = input("Enter score: ")
            if score < 70:
                grade = 'D'
            elif score < 80:
                grade = 'C'
            elif score < 90:
                grade = 'B'
            elif score <= 100:
                grade = 'A'
            print 'Score: ' + str(score) + '; Your grade is ' + grade
            print 'End of program. Bye!'

scoresGrades()
