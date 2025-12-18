import pandas as pd
from abc import ABC, abstractmethod

class Interpreter(ABC):
    @abstractmethod
    def getFirst(self, tour=1) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement getFirst method")
    
    @property
    @abstractmethod
    def year(self) -> int:
        raise NotImplementedError("Subclasses must implement year property")