import datetime

class Person():
    def __init__(
        self,
        active: bool,
        fname: str,
        lname: str, 
        email: str,
        pwdhash: str|None = None,
        expires: datetime = datetime.now().replace(year=datetime.now.year+1),
        created: datetime = datetime.now(),
        
    ):
        self.active = active
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pwdhash = pwdhash
        self.created = created
        self.expires = expires

class Student(Person):
    def __init__(
            self, 
            fname: str, 
            lname: str, 
            email: str, 
            pwdhash: str, 
            expires: datetime,
            sclass: str,
            created: any = datetime.now(),
            licenses: list = [],
            req_licenses: list = [], 
            legal_age: bool = False,
            bank_data: dict = {},
            class_rep: bool = False):
        super().__init__(fname, lname, email, pwdhash, expires, created)
        self.sclass = sclass
        self.licenses: list[License] = licenses
        self.req_licenses = req_licenses
        self.legal_age = legal_age
        self.bank_data = bank_data
        self.class_rep = class_rep

class ClassHead(Person):
    def __init__(
            self, 
            fname: str, 
            lname: str, 
            email: str, 
            pwdhash: str | None = None,
            expires: any = datetime.now().replace(year=datetime.now.year + 1), 
            created: any = datetime.now(),
            manage_class: list = []):
        super().__init__(fname, lname, email, pwdhash, expires, created)
        self.manage_class = manage_class

class Admin(Person):
    pass

class License():
    def __init__(
        self,
        active: bool,
        name: str,
        cost: float = 0.0,
        expires: any = datetime.now().replace(year=datetime.now.year + 1), 
        license_data: dict = {}
    ):
        pass

class Payment():
    def __init__(
        self,
        active: bool,
        name: str,
        author,
        product: License|str,
        cost: float,
        due_date: datetime,
        lable: list[str] = [],
        expires: any = datetime.now().replace(year=datetime.now.year + 1), 
        ):
        self.active = active
        self.name = name
        self.author = author
        self.product = product
        self.cost = cost
        self.due_date = due_date
        self.lable = lable
        self.expires = expires