TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
from collections import namedtuple

Question = namedtuple("Question", ["number", "weight", "format"])

questions = [
    Question(number=1, weight=1, format=TEXT_FORMAT),
    Question(number=2, weight=1, format=TEXT_FORMAT),
]

expected_json = {"1": "Hello World!", "2": 2022}
