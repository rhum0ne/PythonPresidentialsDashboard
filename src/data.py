from interpreters import (
    Interpreter,
    FirstInterpreter,
    SecondInterpreter,
    ThirdInterpreter,
    FourthInterpreter,
    FifthInterpreter
)

interpretersByYear: dict[int, Interpreter] = {}
availableYears = [2024, 2022, 2007, 2002, 1997, 1993, 1988, 1986, 1978, 1973, 1968, 1967, 1962, 1958]

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
        1986: FifthInterpreter(1986),
        1978: ThirdInterpreter(1978),
        1973: ThirdInterpreter(1973),
        1968: ThirdInterpreter(1968),
        1967: ThirdInterpreter(1967),
        1962: ThirdInterpreter(1962),
        1958: ThirdInterpreter(1958),
    }

def getData(year: int) -> Interpreter:
    return interpretersByYear[year]

def getAvailableYears() -> list[int]:
    return availableYears