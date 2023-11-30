from pymongo import MongoClient, errors
import json
from app.db.schemas import Student, Admin, Payment

class MongoDB():
    def __init__(self,
        DBIP: str = "localhost",
        DBPORT: str|int = 27017,
        DBUSER: str = "studently",
        DBPASSWD: str = "studently",
    ):

        self.DBIP = DBIP
        self.DBPORT = DBPORT
        self.DBUSER = DBUSER
        self.DBPASSWD = DBPASSWD
        self.DBURL = f"mongodb://{self.DBUSER}:{self.DBPASSWD}@{self.DBIP}:{self.DBPORT}/?authMechanism=DEFAULT"

        self.client = MongoClient(self.DBURL)
        self.db = self.client["StudentlyDB"]
        self.students = self.db["Students"]
        self.admins = self.db["Admins"]

    def create_student(self, student: Student | list[Student]):
        try:
            if type(student) == list:
                entry_list = []
                for entry in student:
                    dict_entry = entry.__dict__
                    dict_entry["_id"] = entry["email"]
                    entry_list.append(dict_entry)
                return self.students.insert_many(entry_list)
            else:
                dict_student = student.__dict__
                dict_student["_id"] = student.email
                return self.students.insert_one(dict_student)

        except errors.DuplicateKeyError:
            print("Student already Exists")
            return False

    def read_student(self, search_par: str, search_val: any):
        read = self.students.find_one({search_par: search_val})

        if read:
            print("READ: ",read)
            return read
        else:
            return False

    def create_admin(self, admin: Admin | list[Admin]):
        try:
            if type(admin) == list:
                entry_list = []
                for entry in admin:
                    dict_entry = entry.__dict__
                    dict_entry["_id"] = entry["email"]
                    entry_list.append(dict_entry)
                return self.admins.insert_many(entry_list)
            else:
                dict_student = admin.__dict__
                dict_student["_id"] = admin.email
                return self.admins.insert_one(dict_student)

        except errors.DuplicateKeyError:
            print("Admin already Exists")
            return False
        
    def read_admin(self, search_par: str, search_val: any):
        try:
            read = self.admins.find_one({search_par: search_val})
        except:
            return False

        if read:
            return read
        else:
            return False

    def create_payment(self, payment: Payment, students: list[Student]):
        pass

