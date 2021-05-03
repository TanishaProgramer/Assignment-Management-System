import Utils.utils1 as u
import Teacher.AddAssignment as add

def openDashboard(teacher_details):
    while True:
        u.clearScreen()
        print("------- Teacher DashBoard -------\n")
        print("Welcome Dear ,", teacher_details['teach_name'], "\n\n")

        print("1. Add New Assignment")
        print("2. Check Assignment")
        print("3. Add New Student")
        print("4. Add New Class")
        print("5. Exit....")

        choice = int(input("Enter Your choice : "))

        if choice == 1:
            result = addNewAssignment(teacher_details)
            if result:
                print("Added Success")
            else:
                print("something went wrong....")
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            exit(0)
        else:
            print("Wrong input try again....")


# department , subject , deptname_subjectName_teacherName.txt , num_questions , quetions
# {1:"",2:""}
def addNewAssignment(teacher_details):

    department = teacher_details['teach_dept']
    teacher_subjects = teacher_details['Subjects']
    teacher_subjects = teacher_subjects.strip('][').split(',')
    index = 1
    for i in teacher_subjects:
        print(index," : ", i)
        index += 1
    ch = 1
    try:
        ch = int(input("Enter choice : "))
    except IndexError:
        print("Wrong input....")
        return False
    ch = ch-1
    subject = teacher_subjects[ch]
    filename = str(department).replace(" ","")+"_"+subject.strip("'").replace(" ","")+"_"+str(teacher_details['teach_name']).replace(" ","")+".txt"
    input("Enter to continue.")
    u.clearScreen()
    isadded = add.addAssignment(teacher_details, "Assignment/"+filename)
    input("Enter to continue.")
    return isadded
