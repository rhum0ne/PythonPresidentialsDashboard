from interpreter import Interpreter
from first_interpreter import FirstInterpreter
from second_interpreter import SecondInterpreter

interpretersByYear: dict[int, Interpreter] = {}
availableYears = [2024, 2022]

def loadYears() -> None:
    global interpretersByYear
    interpretersByYear = {
        2024: FirstInterpreter(2024),
        2022: SecondInterpreter(2022),
    }

def getData(year: int) -> Interpreter:
    return interpretersByYear[year]

def getAvailableYears() -> list[int]:
    return availableYears