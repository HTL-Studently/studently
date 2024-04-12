from datetime import datetime, timedelta
from typing import Literal
from app.db.schemas import Student, Payment, License, LicenseGroup, Admin, ClassHead, PaymentConfirmation, SClass
from app.db.mongo import MongoDB


class DBHandler():
    def __init__(
        self,
        # STARTUP_ADMIN_EMAIL: str|None = "admin@edu.htl-villach.at",
        # STARTUP_ADMIN_USER: str|None = "admin",
        # STARTUP_ADMIN_PASSWD: str|None = "admin",
    ):
        self.db = MongoDB(
            DBIP = "203.0.113.141",
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
        pass
        # # Create a Admin account:
        # startup_admin_hash = PH().hash(startup_admin_passwd)

        # startup_admin = Admin(
        #     disabled = False,
        #     username = startup_admin_user,
        #     full_name = startup_admin_user,
        #     email = startup_admin_email,
        #     pwdhash = startup_admin_hash,
        #     expires = datetime.now() + timedelta(days=7),
        #     created = datetime.now()
        # )
        # #self.db.create_admin(admin = startup_admin)

    def health_check(self):
        pass



    # Student DB Functions

    def create_student(self, student: Student | list[Student]):
        return self.db.create_student(student)

    def read_student(self, student_list: list = [], search_par: str = "", search_val: any = ""):
        return self.db.read_student(student_list, search_par, search_val)

    def update_student(self, id: str,  field: any, value: any, update_type: Literal["set", "push", "pull"] = "set", ):
        return self.db.update_student(id=id, field=field, value=value, update_type=update_type)

    def add_payment(self, id: str, payment: Payment):
        return self.db.add_payment(id=id, payment=payment)

    def add_payment_confirmation(self, payment_confirmation: PaymentConfirmation):
        return self.db.add_payment_confirmation(payment_confirmation=payment_confirmation)



    # Class Head Function

    def get_class(self, id: str | None = None):
        return self.db.get_class(id=id)

    def create_classHead(self, classHead: ClassHead):
        return self.db.create_classHead(classHead=classHead)


    # Class Functions

    def create_sclass(self, sclass_list: list[SClass]):
        return self.db.create_sclass(sclass_list=sclass_list)

    def read_sclass(self, id: str | None = None, name: str | None = None):
        return self.db.read_sclass(id=id, name=name)

    # Admin DB Functions

    def create_admin(self, admin: Admin | list[Admin]):
        return self.db.create_admin(admin)


    # Payment DB Function

    def create_payment(self, payment: Payment):
        return self.db.create_payment(payment)

    def update_payment(self, id: str,  field: any, value: any, update_type: Literal["set", "push", "pull"] = "set"):
        return self.db.update_payment(id=id, field=field, value=value, update_type=update_type)
    


    def get_payment(self, id: str = "", field: str = "", value: any = ""):
        return self.db.get_payment(id=id, field=field, value=value)

    # License DB Functions

    def create_license_group(self, licenses_group: LicenseGroup | list[LicenseGroup]):
        return self.db.create_license_group(licenses_group=licenses_group)

    def read_license_group(self, search_par: str = "", search_val: any = ""):
        return self.db.read_license(search_par=search_par, search_val=search_val)

    def create_license(self, lic: list[License]):
        return self.db.create_license(lic=lic)

