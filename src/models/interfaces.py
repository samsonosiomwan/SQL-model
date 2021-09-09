from abc import ABC, abstractmethod

class UserInterface(ABC):
   
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def destroy():
        pass
