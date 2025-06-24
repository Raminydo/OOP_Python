

class student:
    def __init__(self, firstname: str, lastname: str, age: str, gender: str, nationalcode: str, stdcode: str) -> None:
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.nationalcode = nationalcode
        self.stdcode = stdcode

    def show_std(self) -> str:
        return f'firstname: {self.firstname}    lastname: {self.lastname}   age: {self.age}\
            gender: {self.gender}   nationalcode: {self.nationalcode}    stdcode: {self.stdcode}'