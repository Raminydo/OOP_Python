

class contact:
    def __init__(self, firstname: str, lastname: str, phone: str, gender: str, description: str = '') -> None:
        
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.gender = gender
        self.description = description

    
    #region firstname
    @property
    def firstname(self) -> str:
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname: str) -> None:
        if not firstname.islower():
            raise NameError()
        
        self.__firstname: str = firstname
    #endregion

    #region lastname
    @property
    def lastname(self) -> str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname: str) -> None:
        if not lastname.islower():
            raise NameError()
        
        self.__lastname: str = lastname
    #endregion

    #region phone
    @property
    def phone(self) -> str:
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str) -> None:
        if not isinstance(phone, str):  # type: ignore
            raise TypeError()
        
        if len(phone) != 10:
            raise NameError()
        
        self.__phone: int = phone
    #endregion

    #region gender
    @property
    def gender(self) -> str:
        return self.__gender
    
    @gender.setter
    def gender(self, gender: str) -> None:
        if gender not in ('male', 'female'):
            raise NameError()
        
        self.__gender: str = gender
    #endregion

    #region description
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, description: str) -> None:
        self.__description: str = description
    #endregion

    def show_contact(self) -> str:
        return f'Fullname: {self.firstname} {self.lastname}    Phone: {self.phone}    Gender: {self.gender}    Description: {self.description}'



