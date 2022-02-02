from collections import namedtuple
TEXT_FORMAT = "text"

Question = namedtuple("Question", ["number", "weight", "format"])
questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
    Question(number=3, weight=1, format=TEXT_FORMAT),
    Question(number=4, weight=1, format=TEXT_FORMAT),
    Question(number=5, weight=1, format=TEXT_FORMAT),
    Question(number=6, weight=1, format=TEXT_FORMAT),
    Question(number=7, weight=1, format=TEXT_FORMAT),
    Question(number=8, weight=1, format=TEXT_FORMAT),
    Question(number=9, weight=1, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT),
    Question(number=12, weight=1, format=TEXT_FORMAT),
    Question(number=13, weight=1, format=TEXT_FORMAT),
    Question(number=14, weight=1, format=TEXT_FORMAT),
    Question(number=15, weight=1, format=TEXT_FORMAT),
    Question(number=16, weight=1, format=TEXT_FORMAT),
    Question(number=17, weight=1, format=TEXT_FORMAT),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT),
]


expected_json = {
    "1": 8760,
    "2": 80235,
    "3": "int",
    "4": "float",
    "5": "int",
    "6": 7,
    "7": 11,
    "8": "bool",
    "9": "str",
    "10": "bool",
    "11": ":-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-)",
    "12": 2000,
    "13": 944.0761410000001,
    "14": 5.0,
    "15": True,
    "16": True,
    "17": True,
    "18": False,
    "19": False,
    "20": 50.0,
}
