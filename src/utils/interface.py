from abc import ABC, abstractmethod


class SetUpDatabaseInteface(ABC):
   
    @abstractmethod
    def setup_default_data():
        pass
