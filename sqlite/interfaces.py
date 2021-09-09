from abc import ABC, abstractmethod


class CrudOperationInterface(ABC):

    @abstractmethod
    def read_all():
        pass

    @abstractmethod
    def create():
        pass

    @abstractmethod
    def get_passed():
        pass

    @abstractmethod
    def get_failed():
        pass

    @abstractmethod
    def get_test1():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def destroy():
        pass

class ToSQLInterface(ABC):
    def convert_to_sql():
        pass
    