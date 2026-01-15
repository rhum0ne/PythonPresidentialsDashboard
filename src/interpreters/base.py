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
    
    @abstractmethod
    def get4MainData(self, tour: int) -> dict[str, int]:
        """Get the 4 main data points for the rigt panel: inscrits, votants, blancs_nuls, abstention.

        Raises:
            NotImplementedError: If the subclass does not implement this method.

        Returns:
            dict[str, int]: key(inscrits, votants, blancs_nuls, abstention) and their values
        """
        raise NotImplementedError("Subclasses must implement get4MainData method")