import json

login_teacher = {"teach_id":"", "teach_password":""}


def fetchTeacherDetails(teach_id):
    pass


def verifyDetails(teach_id, teach_password):
    teacher_login_info = open("Teacher/teacher_login_info.txt","r")
    data = teacher_login_info.read()
    teacher_data = data.strip("][").split(",\n")
    for data in teacher_data:
        data = json.loads(data)
        if data['teach_id'] == teach_id and data['teach_password']==teach_password:
            print("login Success...")
            teacher_details = fetchTeacherDetails(teach_id)
            break


