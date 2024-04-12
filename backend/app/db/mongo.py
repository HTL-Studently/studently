import time
from typing import Literal
import uuid
from pymongo import MongoClient, errors
import json
from app.db.schemas import Student, Payment, License, Admin, LicenseGroup, Teacher, PaymentConfirmation, SClass, Product

class MongoDB():
    def __init__(self,
        DBIP: str = "192.168.160.100",
        DBPORT: str|int = 27017,
        DBUSER: str = "studently",
        DBPASSWD: str = "studently",
    ):
        self.DBIP = DBIP
        self.DBPORT = DBPORT
        self.DBUSER = DBUSER
        self.DBPASSWD = DBPASSWD
        self.DBURL = f"mongodb://studently:studently@{self.DBIP}:{self.DBPORT}/?authMechanism=DEFAULT"



        self.client = MongoClient(self.DBURL)
        self.db = self.client["StudentlyDB"]
        self.students = self.db["Students"]
        self.teachers = self.db["Teachers"]
        self.payments = self.db["Payments"]
        self.payment_confirmation = self.db["Payment-Confirmations"]
        self.admins = self.db["Admins"]
        self.licenses = self.db["Licenses"]
        self.sclass = self.db["SClass"]
        self.products = self.db["Products"]



    # Student DB Functions
    def create_student(self, student: Student | list[Student]):
        try:
            if type(student) == list:
                entry_list = [entry.__dict__ for entry in student]
                for entry in entry_list:
                    entry["_id"] = entry["identifier"]
                    try:
                        self.students.insert_one(entry)
                    except errors.DuplicateKeyError:
                        pass
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
        
    def update_student(self, id: str,  field: any, value: any, update_type: Literal["set", "push", "pull"] = "set"):
        query = {"_id": id}
        new_values = {f"${update_type}": {field: value}}

        result = self.students.update_one(query, new_values)

        return f"matches: {result.matched_count}"

    def add_payment_confirmation(self, payment_confirmation: PaymentConfirmation):
        payment_confirmation = payment_confirmation.__dict__
        payment_confirmation["_id"] = payment_confirmation["identifier"]

        result = self.payment_confirmation.insert_one(payment_confirmation)

        return result



    ##### Class Head Function #####

    def create_classHead(self, classHead: Teacher | list[Teacher]):        
        if type(classHead) == list:
            entry_list = [entry.return_dict() for entry in classHead]
            for entry in entry_list:
                entry["_id"] = entry["identifier"]
                try:
                    self.teachers.insert_one(entry)
                except errors.DuplicateKeyError:
                    pass
        else:
            dict_classHead = classHead.__dict__
            dict_classHead["_id"] = classHead.identifier
            return self.teachers.insert_one(classHead)
        


    ##### SClass Functions #####
        
    def create_sclass(self, sclass_list: list[SClass]):
            entry_list = [sclass.__dict__ for sclass in sclass_list]
            for entry in entry_list:
                entry["_id"] = entry["identifier"]
                self.sclass.insert_one(entry)

    def read_sclass(self, search_par = "", search_val: str = ""):
        if search_par:
            found = self.sclass.find_one({search_par: search_val})
            return found
        
        else:
            found = self.sclass.find()
            sclass_list = []
            for sclass in found:
                sclass_list.append(sclass)
            return sclass_list
    
    
    ##### Payment DB Functions #####
    
    def create_payment(self, payment: Payment):
        dict_payment = payment.__dict__
        dict_payment["_id"] = str(uuid.uuid4())
        return self.payments.insert_one(dict_payment)

    def update_payment(self, id: str,  field: any, value: any, update_type: Literal["set", "push", "pull"] = "set"):
        query = {"identifier": id}
        

        new_values = {f"${update_type}": {field: value}}
        # result = self.payments.update_one(query, new_values)
    
        query = {"identifier": "36154f01-2a94-4346-8046-7d68780f3d2c"}
        values = { "$set": { "type": "TEST123" } }

        result = self.payment_confirmation.update_one(query, values)


        print(result, values, query)

        return f"matches: {result.matched_count}"


    ##### License DB Functions #####
        
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
    

    ##### Product DB Functions #####

    def create_product(self, product: Product):
        product_dict = product.__dict__
        product_dict["_id"] = str(uuid.uuid4())
        return self.products.insert_one(product_dict)
    
    def read_product(self, id: str = ""):
        if id:  
            return self.products.find_one({"_id": id})
        else:
            return self.products.find({})

    def delete_product(self, id: str):
        return self.products.delete_one({"_id": id})
    
    
    ##### Student Product DB Functions #####

    def assign_product(self, product: Product, id: str):
        product = product.__dict__
        product["_id"] = product["identifier"]

        result = self.students.update_one(
            {"_id": id},
            {"$push": {"owned_objects": product}}
        )

        return result

    def update_product(self, product, id: str ):
        """
        Updates an individual product owned by a student
        - product: Updated product object
        - product_id: ID of the product
        - id: User id
        """
    
        print(id)
       

        result = self.students.update_one(
            {"_id": id},
            {"$set": {"owned_objects": product}}
        )


        return result

    def remove_product(self, product_id: str, id: str):
        """
        Removes an individual product from student
        - product_id: ID of the product
        - id: User id
        """

        result = self.students.update_one(
            {"_id": id},
            {"$pull": {"owned_objects": {"_id": product_id}}}
        )

        return result

    