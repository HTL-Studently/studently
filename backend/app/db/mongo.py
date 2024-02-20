import time
from typing import Literal
import uuid
from pymongo import MongoClient, errors
import json
from app.db.schemas import Student, Payment, License, Admin, LicenseGroup, ClassHead

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
        self.DBURL = f"mongodb://{self.DBUSER}:{self.DBPASSWD}@{self.DBIP}:{self.DBPORT}/?authMechanism=DEFAULT"

        self.client = MongoClient(self.DBURL)
        self.db = self.client["StudentlyDB"]
        self.students = self.db["Students"]
        self.classHeads = self.db["ClassHeads"]
        self.payments = self.db["Payments"]
        self.admins = self.db["Admins"]
        self.licenses = self.db["Licenses"]


    # Student DB Functions
    def create_student(self, student: Student | list[Student]):
        try:
            if type(student) == list:
                entry_list = [entry.return_dict() for entry in student]
                for entry in entry_list:
                    entry["_id"] = entry["identifier"]
                return self.students.insert_many(entry_list)
            else:
                dict_student = student.__dict__
                dict_student["_id"] = student.identifier
                return self.students.insert_one(dict_student)

        except errors.DuplicateKeyError:
            print("Student already Exists")
            return False
    
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    def read_student(self, student_list: list[Student] = [], search_par: str = "", search_val: any = ""):

        if student_list:
            return_list = []
            for student in student_list:
                read = self.students.find_one({"identifier": student.identifier})
                if read:
                    return return_list.append(read)
                else:
                    return False
                
        elif search_par:
            read = self.students.find({search_par: search_val})
            entry_list = [entry for entry in read]
            return entry_list
        
        else:
            read = self.students.find()
            entry_list = [entry for entry in read]
            return entry_list
        
    def update_student(self, id: str,  field: any, value: any, update_type: Literal["set", "push", "pull"] = "set", ):
        query = {"_id": id}
        new_values = {f"${update_type}": {field: value}}

        result = self.students.update_one(query, new_values)
        
        return f"matches: {result.matched_count}"


    def create_classHead(self, classHead: ClassHead | list[ClassHead]):        
                

        if type(classHead) == list:
            entry_list = [entry.return_dict() for entry in classHead]
            for entry in entry_list:
                entry["_id"] = entry["identifier"]
            return self.classHeads.insert_many(entry_list)
        else:
            dict_student = classHead.__dict__
            dict_student["_id"] = classHead.identifier
            return self.classHeads.insert_one(dict_student)

        # except errors.DuplicateKeyError:
        #     print("Student already Exists")
        #     return False
    
        # except Exception as e:
        #     print(f"Unexpected error: {e}")
        #     return False


    # Payment DB Functions
    
    def create_payment(self, payment: Payment):
        dict_payment = payment.__dict__
        dict_payment["_id"] = str(uuid.uuid4())
        return self.payments.insert_one(dict_payment)


    # License DB Functions
    def create_license_group(self, licenses_group: LicenseGroup):
        try:
            return_dict = licenses_group.return_dict()
            return_dict["_id"] = licenses_group.identifier

            inserted = self.licenses.insert_one(return_dict)

        except errors.DuplicateKeyError:
            print("License Group already Exists")
            return False
    
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def create_license(self, lic: list[License]):

        print(lic)

        for entry in lic:
            dict_entry = entry.return_dict()

            belongs_to = dict_entry["license_group"]
            license_id = dict_entry["identifier"]

            update_query = {"$set": {f"licenses.{license_id}": dict_entry}}
            update = self.licenses.update_one({"_id": belongs_to}, update_query)
            update_list.append(update_list)
    
