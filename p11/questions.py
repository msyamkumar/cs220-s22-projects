# version: 4/15, 12:30PM
#===================== DO NOT EDIT THIS BLOCK =================================#
import collections
from collections import namedtuple
import json
import os
import math

PASS = "PASS"
TEXT_FORMAT = "text"  # question type when expected answer is a str, int, float, or bool
NO_RERUN = "no_rerun" #any question involving paths. Do not expect the rerun to match submission
TEXT_NO_RERUN = TEXT_FORMAT + " " + NO_RERUN
TEXT_FORMAT_NAMEDTUPLE = "text namedtuple"  # question type when expected answer is a namedtuple
TEXT_FORMAT_UNORDERED_LIST = "text list_unordered"  # question type when the expected answer is a list where the order does *not* matter
TEXT_FORMAT_ORDERED_LIST = "text list_ordered"  # question type when the expected answer is a list where the order does matter
TEXT_FORMAT_ORDERED_LIST_NO_RERUN = "text list_ordered no_rerun"  # question type when the expected answer is a list where the order does matter and contains paths
TEXT_FORMAT_ORDERED_LIST_NAMEDTUPLE = "text list_ordered namedtuple"  # question type when the expected answer is a list of namedtuples where the order does matter
TEXT_FORMAT_SPECIAL_ORDERED_LIST = "text list_special_ordered"  # question type when the expected answer is a list where order does matter, but with possible ties. All tied elements are put in a list, where internal order does not matter.
TEXT_FORMAT_DICT = "text dict"  # question type when the expected answer is a dictionary
TEXT_FORMAT_LIST_DICTS_ORDERED = "text list_dicts_ordered"  # question type when the expected answer is a list of dicts where the order does matter
PNG_FORMAT = "png"  # use when the expected answer is an image
HTML_FORMAT = "html"
FILE_FORMAT = "file"
FILE_JSON_FORMAT = "file json"

Question = collections.namedtuple("Question", ["number", "weight", "format"])
#===================== DO NOT EDIT THIS BLOCK =================================#


# EDIT THIS: definitions specific to this project
Comment = collections.namedtuple("Comment", ['video_id', 'comment_length', 'author_id', 'likes', 'published_at'])

REQUIRED_FILES = [os.path.join('data', 'channel_ids1.json'),
         os.path.join('data', 'channel_ids2.json'),
         os.path.join('data', 'channel_ids3.json'),
         os.path.join('data', 'channel_ids4.json'),
         os.path.join('data', 'channel_ids5.json'),
         os.path.join('data', 'comment_data1.csv'),
         os.path.join('data', 'comment_data2.csv'),
         os.path.join('data', 'comment_data3.csv'),
         os.path.join('data', 'comment_data4.csv'),
         os.path.join('data', 'comment_data5.csv'),
         os.path.join('data', 'video_data.csv'),
         os.path.join('data', 'video_ids.json'),
         os.path.join('broken_file', 'english_lowercase', 'a_to_m', 'a_to_m.json'),
         os.path.join('broken_file', 'english_lowercase', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'A', 'A.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'E.json'),
         os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'rest', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'F_to_H.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'I', 'I.json'),
         os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
         os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json'),
         os.path.join('broken_file', 'english_uppercase', 'R_to_W.json'),
         os.path.join('broken_file', 'english_uppercase', 'rest.json'),
         os.path.join('broken_file', 'non_english', 'korean.json'),
         os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
         os.path.join('broken_file', 'non_english', 'rest', 'rest.json'),
         os.path.join('broken_file', 'non_english', 'russian', 'russian.json'),
         os.path.join('broken_file', 'number.json'),
         os.path.join('broken_file', 'special', 'special.json')]

questions = [
    Question(number=1, weight=0.5, format=PNG_FORMAT),
    Question(number=1.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=2, weight=0.5, format=PNG_FORMAT),
    Question(number=2.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=3, weight=0.5, format=PNG_FORMAT),
    Question(number=3.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=4, weight=0.5, format=PNG_FORMAT),
    Question(number=4.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=5, weight=0.5, format=PNG_FORMAT),
    Question(number=5.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=6, weight=0.5, format=PNG_FORMAT),
    Question(number=6.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=7, weight=0.5, format=PNG_FORMAT),
    Question(number=7.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=8, weight=0.5, format=PNG_FORMAT),
    Question(number=8.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=9, weight=0.5, format=PNG_FORMAT),
    Question(number=9.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=10, weight=1, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
    Question(number=12, weight=0.5, format=PNG_FORMAT),
    Question(number=12.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=13, weight=0.5, format=PNG_FORMAT),
    Question(number=13.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=14, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=15, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=16, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=17, weight=1, format=TEXT_FORMAT_ORDERED_LIST_NO_RERUN),
    Question(number=18, weight=1, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=1, format=TEXT_FORMAT_ORDERED_LIST),
]

expected_json = {
        "1.1": True,
        "2.1": True,
        "3.1": True,
        "4.1": True,
        "5.1": True,
        "6.1": True,
        "7.1": True,
        "8.1": True,
        "9.1": True,
        "10": 66,
        "11": 478.6,
        "12.1": True,
        "13.1": True,
        "14": [os.path.join('broken_file', 'special', 'special.json')],
        "15": [os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'rest.json')],
        "16": [os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json')],
        "17": [os.path.join('broken_file', 'english_lowercase', 'a_to_m', 'a_to_m.json'),
                os.path.join('broken_file', 'english_lowercase', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'A', 'A.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'E.json'),
                os.path.join('broken_file', 'english_uppercase', 'A_to_E', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'F_to_H.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'I', 'I.json'),
                os.path.join('broken_file', 'english_uppercase', 'F_to_K', 'I_to_K', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'O.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'M.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'L_to_N', 'rest', 'rest.json'),
                os.path.join('broken_file', 'english_uppercase', 'L_to_Q', 'rest', 'P_to_Q.json'),
                os.path.join('broken_file', 'english_uppercase', 'R_to_W.json'),
                os.path.join('broken_file', 'english_uppercase', 'rest.json'),
                os.path.join('broken_file', 'non_english', 'korean.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'japanese', 'japanese.json'),
                os.path.join('broken_file', 'non_english', 'rest', 'rest.json'),
                os.path.join('broken_file', 'non_english', 'russian', 'russian.json'),
                os.path.join('broken_file', 'number.json'),
                os.path.join('broken_file', 'special', 'special.json')],
        "18": 18519,
        "19": 'Like it Matters',
        "20": ['ChippyGaming',
                 'Odin J',
                 'A comely black woman',
                 'BadBoyHalo',
                 'Nakatomino Calamari ']
    }

# The following code is used to verify plots. See the p11 solution for how to generate
# plot_points.json
with open("plot_points.json", "r", encoding="utf-8") as fp:
    read_dicts = json.load(fp, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})

REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

def verify_bar(plot_dict, qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return False
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return False
    answer_dict = read_dicts[qnum-1]
    if len(answer_dict) != len(plot_dict):
        #tested
        print("Expected dict of length %d but got length %d" % (len(answer_dict), len(plot_dict)))
        return False
    try:
        for key in answer_dict:
            answer_value = answer_dict[key]
            input_value = plot_dict[key]
            if type(answer_value) != type(input_value):
                #tested
                print("Expected values of type %s but got %s" % (str(type(answer_value)), str(type(input_value))))
                return False
            if type(answer_value) == float:
                if not math.isclose(input_value, answer_value, rel_tol=REL_TOL, abs_tol=ABS_TOL):
                    print("For key %s: expected float value %f but found %f" % (str(key), answer_value, input_value))
                    return False
            elif answer_value != input_value: #answer is not a float
                #tested
                print("For key %s: expected value %s but found %s" % (str(key), str(answer_value), str(input_value)))
                return False

    except KeyError:
        #tested
        print("Did not find key " + str(key) + "; make sure key type is " + str(type(key)))
        return False
    return True

def verify_scatter(x, y, qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return None
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return None
    # allow for iterables like .keys()
    x = list(x)
    y = list(y)
    answer = sorted(zip(read_dicts[qnum-1]["x"], read_dicts[qnum-1]["y"]))
    input = sorted(zip(x, y))

    if len(answer) != len(input):
        #tested
        print("Expected lists of length %d but got length %d" % (len(answer), len(input)))
        return False
    for i in range(len(answer)):
        x_ans, y_ans = answer[i]
        x_in, y_in = input[i]
        if type(x_ans) != type(x_in) or type(y_ans) != type(y_in):
            #tested
            print("Expected types %s, %s but got %s, %s" % (str(type(x_ans)), str(type(y_ans)), str(type(x_in)), str(type(y_in))))
            return False
        if x_ans != x_in:
            #tested
            print("When x,y pairs were sorted, expected x value %s at index %d, but found %s" % (str(x_ans), i, str(x_in)))
            return False
        if type(y_ans) == float:
            #tested
            if not math.isclose(y_in, y_ans, rel_tol=REL_TOL, abs_tol=ABS_TOL):
                print("For x value %s: expected float value %f but found %f" % (str(x_ans), y_ans, y_in))
                return False
        elif y_ans != y_in: #answer is not a float
            #tested
            print(type(y_ans))
            print("For key %s: expected value %s but found %s" % (str(x_ans), str(y_ans), str(y_in)))
            return False
    return True

def view_plot_data(qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return None
    if read_dicts[qnum-1] == {}:
        print("This question has no plot to verify")
        return None
    return read_dicts[qnum-1]
