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

expected_json = {
    "1": 144,
    "2": 37,
    "3": 130,
    "4": 2,
    "5": 195,
    "6": 75,
    "7": 958107084997,
    "8": 2678957142.86,
    "9": "SALly",
    "10": 1370000,
    "11": "San Ciriaco",
    "12": 91610000000,
    "13": 175,
    "14": 2017,
    "15": 'Bob',
    "16": 5,
    "17": 25,
    "18": '1901 to 1910',
    "19": 15626,
    "20": "Olaf",
}
