from fileinput import filename


def addAssignment(teacher_details, filepath):
    isadded = False

    questions = {}
    assignment_file = open(filepath, "w")
    data = getFileData(filepath)
    print(data)
    input()
    count_ques = int(input("Enter Number of Ques.."))
    if count_ques <= 0:
        return False
    else:
        for i in range(0,count_ques):
            q = input("please enter the question..")
            questions[i] = q
        data.append(str(questions)+"\n")
        assignment_file.write(str(data))
        isadded = True
    return isadded

def getFileData(assignment_filepath):
    assignment_file = open(assignment_filepath, "r")
    data = assignment_file.read().strip("[]").split("\n")
    return data
