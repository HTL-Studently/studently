from argon2 import PasswordHasher

class SecurityFunctions():
    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def hash_str(self, plain: str):
        """Returnes the hash of a string"""

        hashed_string = self.ph.hash(plain)
        if self.ph.verify(hashed_string, plain):
            return hashed_string

    def verify_hash(self, hashed_string: str, plain):
        """Verifies hash"""
        self.ph.verify(hashed_string, plain)

    def check_rehash(self, plain):
        """Rehashes password if needed"""
        if self.ph.check_needs_rehash:
            return self.hash_str(plain)
