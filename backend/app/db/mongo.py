import time
from typing import Literal
from pymongo import MongoClient, errors
import json
from app.db.schemas import Student, Admin, Payment, BaseObject, License

class MongoDB():
    def __init__(self,
        DBIP: str = "studently.mongodb",
        DBPORT: str|int = 27017,
        DBUSER: str = "studently",
        DBPASSWD: str = "studently",
    ):
        self.DBIP = DBIP
        self.DBPORT = DBPORT
        self.DBUSER = DBUSER
        self.DBPASSWD = DBPASSWD
<<<<<<< HEAD
        self.DBURL = f"mongodb://{self.DBUSER}:{self.DBPASSWD}@{DBIP}:{self.DBPORT}/?authMechanism=DEFAULT"


=======
        self.DBURL = f"mongodb://{self.DBUSER}:{self.DBPASSWD}@{self.DBIP}:{self.DBPORT}/?authMechanism=DEFAULT"
>>>>>>> uiwip

        self.client = MongoClient(self.DBURL)
        self.db = self.client["StudentlyDB"]
        self.students = self.db["Students"]
        self.admins = self.db["Admins"]
        self.licenses = self.db["Licenses"]

    # Student DB Functions

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

    def read_student(self, student_list: list[Student] = [], search_par: str = "", search_val: any = ""):

        if student_list:
            return_list = []
            for student in student_list:
                read = self.students.find_one({"email": student.email})
                if read:
                    print("READ: ",read)
                    return return_list.append(read)
                else:
                    return False
        else:
            read = self.students.find_one({search_par: search_val})
            if read:
                print("READ: ",read)
                return read
            else:
                return False

    def update_student(self, update_type: Literal["set", "push", "pull"], id: str,  field: any, value: any):
        query = {"_id": id}
        new_values = {f"${update_type}": {field: value}}

        result = self.students.update_one(query, new_values)
        
        return f"matches: {result.matched_count}"
    
    def sub_update_student(self, update_type: Literal["set", "push", "pull"], id: str,  field: any, sub_filed: any, value: any):
        query = {"_id": id}
        new_values = {f"${update_type}": {field: {sub_filed: value}}}

        result = self.students.update_one(query, new_values)
        
        return f"matches: {result.matched_count}"
    

    # Admin DB Functions

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

    
    # License DB Functions

    def create_license(self, licenses: list[License]):
        if type(licenses) == list:
            entry_list = []
            for license in licenses:
                dict_license = license.return_dict()
                dict_license["_id"] = license.id
                entry_list.append(dict_license)
            self.licenses.insert_many(entry_list)

        else:
            dict_license = license.return_dict()
            dict_license["_id"] = license.id
            self.licenses.insert_one(dict_license)


    def read_license(self,search_par: str = "", search_val: any = ""):
        return_list = []

        if search_par and search_val:
            result = self.licenses.find({search_par: search_val})
            for entry in result:
                return_list.append(entry)

        else:
            result = self.licenses.find()
            for entry in result:
                return_list.append(entry)

        return return_list
            

        

    def update_license():
        pass

    def delete_lecense():
        pass