import pandas as pd
from abc import ABC, abstractmethod

class Interpreter(ABC):
    @abstractmethod
    def getFirst(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses must implement getFirst method")