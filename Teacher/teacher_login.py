import json
import Utils.utils1 as u
import Teacher.teacher_dashboard as dashboard

login_teacher = {"teach_id": "", "teach_password": ""}

def fetchTeacherDetails(teach_id):
    teacher_detail = {}
    teachers_info = open("Teacher/teachers_info.txt","r")
    data = teachers_info.read()
    teachers_data = data.strip("][").split(",\n")
    for data in teachers_data:
        data = json.loads(data)
        if data['teach_id'] == teach_id:
            teacher_detail = data
            break
    return teacher_detail


def verifyDetails(teach_id, teach_password):
    teacher_login_info = open("Teacher/teacher_login_info.txt", "r")
    data = teacher_login_info.read()
    teacher_data = data.strip("\n").strip("[]").split(",\n")
    for data in teacher_data:
        data = json.loads(data)
        if data['teach_id'] == teach_id and data['teach_password'] == teach_password:
            print("login Success...")
            teacher_details = fetchTeacherDetails(teach_id)
            u.clearScreen()
            dashboard.openDashboard(teacher_details)
            break

