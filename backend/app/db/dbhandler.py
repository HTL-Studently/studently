from datetime import datetime, timedelta
from argon2 import PasswordHasher as PH

from app.db.schemas import Student, Admin, Payment, BaseObject, License
from app.db.mongo import MongoDB


class DBHandler():
    def __init__(
        self,
        STARTUP_ADMIN_EMAIL: str|None = "admin@edu.htl-villach.at",
        STARTUP_ADMIN_USER: str|None = "admin",
        STARTUP_ADMIN_PASSWD: str|None = "admin",
    ):
        self.db = MongoDB(
            DBIP = "10.1.1.130",
            DBPORT = 27017,
            DBUSER = "studently",
            DBPASSWD = "studently",
        )


        # self.on_start(
        #     startup_admin_email = STARTUP_ADMIN_EMAIL,
        #     startup_admin_user = STARTUP_ADMIN_USER,
        #     startup_admin_passwd = STARTUP_ADMIN_PASSWD
        # )

    def on_start(
        self,
        startup_admin_email: str|None = "admin@edu.htl-villach.at",
        startup_admin_user: str|None = "admin",
        startup_admin_passwd: str|None = "admin",

    ):
        # Create a Admin account:
        startup_admin_hash = PH().hash(startup_admin_passwd)

        startup_admin = Admin(
            disabled = False,
            username = startup_admin_user,
            full_name = startup_admin_user,
            email = startup_admin_email,
            pwdhash = startup_admin_hash,
            expires = datetime.now() + timedelta(days=7),
            created = datetime.now()
        )
        #self.db.create_admin(admin = startup_admin)

    def health_check(self):
        pass



    # Student DB Functions

    def create_student(self, student: Student | list[Student]):
        return self.db.create_student(student)

    def read_student(self, student_list: list = [],search_par: str = "", search_val: any = ""):
        return self.db.read_student(student_list, search_par, search_val)

    def update_student(self, id: str, field: any, value: any):
        return self.db.update_student(id=id, field=field, value=value)



    # Admin DB Functions

    def create_admin(self, admin: Admin | list[Admin]):
        return self.db.create_admin(admin)

    def read_admin(self, search_par: str, search_val: any):
        return self.db.read_admin(search_par, search_val)


    # License DB Functions

    def create_license(self, licenses: list[License]):
        return self.db.create_license(licenses=licenses)

    def read_license(self, search_par: str = "", search_val: any = ""):
        return self.db.read_license(search_par=search_par, search_val=search_val)

    def update_license(self):
        return self.db.update_license()

    def delete_license(self):
        return self.db.delete_license()


    # Student Payment

    def add_payment(self, id: str, obj: Payment):
        return self.db.update_student(update_type="push",id=id, field="owned_objects", value=obj.return_dict())
    
    def delete_payment(self, id: str, obj: Payment):
        return self.db.sub_update_student(update_type="pull", id=id, field="owned_objects", sub_filed="id", value=obj.id)
    
    # Student Licenses

    def add_license(self):
        pass

    def delete_license(self):
        pass