from interpreter import Interpreter
from first_interpreter import FirstInterpreter

interpretersByYear: Dict[int, Interpreter] = {}

def loadYears() -> None:
    global interpretersByYear
    interpretersByYear = {
        2024: FirstInterpreter(2024),
        2022: FirstInterpreter(2022),
    }

def getData(year: int) -> Interpreter:
    return interpretersByYear[year]