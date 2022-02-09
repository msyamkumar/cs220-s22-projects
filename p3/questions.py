TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
from collections import namedtuple

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

expected_json = {"1": 3,
                 "2": 185.145,
                 "3": 2307.717,
                 "4": 2752.024,
                 "5": 2998.142,
                 "6": 227.901,
                 "7": 1775.705,
                 "8": 484.537,
                 "9": 2550.499,
                "10": 10.289,
                "11": 5080.059,
                "12": 6468.264,
                "13": -11.742,
                "14": 219.119,
                "15": 2028,
                "16": 2032,
                "17": 2029,
                "18": 2050,
                "19": 4248.807,
                "20": 0.846,
            }
