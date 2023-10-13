from security import SecurityFunctions
from db.schemas import Student
from db.mongo import MongoDB

class DBHandler():
    def __init__(self,
                 
                 ):
        self.db = MongoDB()

    def create_student(self, student: Student | list[Student]):
        return self.db.create_student(student)

    def read_student(self, search_par: str, search_val: any):
        return self.db.read_student(search_par, search_val)