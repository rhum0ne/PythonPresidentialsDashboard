import pandas as pd
from abc import ABC, abstractmethod

class Interpreter(ABC):
    @abstractmethod
    def getGlobalData(self, tour=1) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement getGlobalData method")
    
    @property
    @abstractmethod
    def year(self) -> int:
        raise NotImplementedError("Subclasses must implement year property")
    
    @property
    @abstractmethod
    def file_name(self) -> str:
        raise NotImplementedError("Subclasses must implement file_name property")
    
    @abstractmethod
    def getDepartmentCodeColumnName(self) -> str:
        raise NotImplementedError("Subclasses must implement getDepartmentCodeColumnName method")
    
    @abstractmethod
    def getAbstentionsColumnName(self) -> str:
        raise NotImplementedError("Subclasses must implement getAbstentionsColumnName method")