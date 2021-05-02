# assignment management System...
# execution of the project will start from this file....
import Utils.utils1 as u
import Teacher.teacher_login as teacher

users = ["student", "teacher"]
entry_options = ["login", "register"]

def openMenu():

    while True:
        u.clearScreen()
        print("1. Student")
        print("2. Teacher")
        print("3. EXIT...")
        choice = int(input("Choose what you are : "))
        if choice == 1:
            login(users[0])
        elif choice == 2:
            login(users[1])
        elif choice == 3:
            exit(0)
        else:
            print("INVALID INPUT\nTry Again...")

# user_type -> student , teacher.
def login(user_type):

    ## for student
    if user_type == users[0]:
        print("------ Login As A Student ------")
        std_id = int(input("Enter Your Student ID"))
        std_password = input("Enter Your Student Password")

    ## for teacher
    elif user_type == users[1]:
        print("------ Login As A Teacher ------")
        teach_id = int(input("Enter Your Instructor ID"))
        teach_password = input("Enter Your Instructor Password")
        teacher.verifyDetails(teach_id, teach_password)


if __name__ == "__main__":
    openMenu()
