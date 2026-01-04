from interpreters import (
    Interpreter,
    FirstInterpreter,
    SecondInterpreter,
    ThirdInterpreter,
    FourthInterpreter
)

interpretersByYear: dict[int, Interpreter] = {}
availableYears = [2024, 2022, 2007, 2002, 1997, 1993, 1988]

def loadYears() -> None:
    global interpretersByYear
    interpretersByYear = {
        2024: FirstInterpreter(2024),
        2022: SecondInterpreter(2022),
        2007: ThirdInterpreter(2007),
        2002: ThirdInterpreter(2002),
        1997: ThirdInterpreter(1997),
        1993: FourthInterpreter(1993),
        1988: ThirdInterpreter(1988),
    }

def getData(year: int) -> Interpreter:
    return interpretersByYear[year]

def getAvailableYears() -> list[int]:
    return availableYears