from base import BaseModel

class Customer (BaseModel):
    def __init__ (self,email,password):
        self._email=email
        self._password=password
        pass


    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        self.email = value


    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("Password is required")
        self.password = value