# version: 4/15, 12:30PM
#===================== DO NOT EDIT THIS BLOCK =================================#
import collections
from collections import namedtuple
import json
import os, pickle
import math
import numpy as np

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

REQUIRED_FILES = ['expected.html']

# set this to [] if they're not supposed to download any files
FILES_TO_DOWNLOAD = ['QSranking.json']


questions = [
    Question(number=1, weight=1, format=HTML_FORMAT),
    Question(number=2, weight=1, format=HTML_FORMAT),
    Question(number=3, weight=1, format=HTML_FORMAT),
    Question(number=4, weight=0.5, format=PNG_FORMAT),
    Question(number=4.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=5, weight=1, format=HTML_FORMAT),
    Question(number=6, weight=0.5, format=PNG_FORMAT),
    Question(number=6.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=7, weight=1, format=HTML_FORMAT),
    Question(number=8, weight=0.5, format=PNG_FORMAT),
    Question(number=8.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=9, weight=0.5, format=PNG_FORMAT),
    Question(number=9.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=10, weight=0.5, format=PNG_FORMAT),
    Question(number=10.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=11, weight=1, format=TEXT_FORMAT),
    Question(number=12, weight=1, format=TEXT_FORMAT),
    Question(number=13, weight=1, format=HTML_FORMAT),
    Question(number=14, weight=1, format=HTML_FORMAT),
    Question(number=15, weight=1, format=HTML_FORMAT),
    Question(number=16, weight=0.5, format=PNG_FORMAT),
    Question(number=16.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=17, weight=0.5, format=PNG_FORMAT),
    Question(number=17.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=18, weight=0.5, format=PNG_FORMAT),
    Question(number=18.1, weight=0.5, format=TEXT_FORMAT),
    Question(number=19, weight=1, format=TEXT_FORMAT),
    Question(number=20, weight=0.5, format=PNG_FORMAT),
    Question(number=20.1, weight=0.5, format=TEXT_FORMAT),
]

expected_json = {
        "4.1": True,
        "6.1": True,
        "8.1": True,
        "9.1": True,
        "10.1": True,
        "11": 0.18978846844574526,
        "12": 0.557397228343763,
        "16.1": True,
        "17.1": True,
        "18.1": True,
        "19": 56,
        "20.1": True
    }

# The following code is used to verify plots for p13. See the p13 solution for how to generate
# plot_data.pkl
with open("plot_data.pkl", "rb") as fp:
    read_dicts = pickle.load(fp)

REL_TOL = 6e-04  # relative tolerance for floats
ABS_TOL = 15e-03  # absolute tolerance for floats

def df_to_dict(df, x_name, y_name):
    return dict(zip(df[x_name], df[y_name]))

def df_to_xylist(df, x_name, y_name):
    return sorted(zip(df[x_name], df[y_name]))

def verify_bar(input_dict, answer_dict):
    if len(answer_dict) != len(input_dict):
        #tested
        print("Expected dict of length %d but got length %d" % (len(answer_dict), len(input_dict)))
        return False
    try:
        for key in answer_dict:
            answer_value = answer_dict[key]
            input_value = input_dict[key]
            if type(answer_value) != type(input_value):
                #tested
                print("Expected values of type %s but got %s" % (str(type(answer_value)), str(type(input_value))))
                return False
            if type(answer_value) == float:
                if np.isnan(answer_value) and not np.isnan(input_value): # This logic is needed as NaN!=NaN is True.
                    print("For key %s: expected NaN value but found %f" % (str(key), input_value)  )
                    return False
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

def verify_scatter(input_list, answer_list):
    if len(answer_list) != len(input_list):
        #tested
        print("Expected lists of length %d but got length %d" % (len(answer_list), len(input_list)))
        return False
    for i in range(len(answer_list)):
        x_ans, y_ans = answer_list[i]
        x_in, y_in = input_list[i]
        if type(x_ans) != type(x_in) or type(y_ans) != type(y_in):
            #tested
            print("Expected types %s, %s but got %s, %s" % (str(type(x_ans)), str(type(y_ans)), str(type(x_in)), str(type(y_in))))
            return False
        if x_ans != x_in and not (np.isnan(x_ans) and np.isnan(x_in)): # This logic is needed as NaN!=NaN is True.
            #tested
            print("When x,y pairs were sorted, expected x value %s at index %d, but found %s" % (str(x_ans), i, str(x_in)))
            return False
        if type(y_ans) == float:
            if np.isnan(y_ans) and not np.isnan(y_in): # This logic is needed as NaN!=NaN is True.
                print("For x value %s: expected NaN value but found %f" % (str(x_ans), y_in))
                return False
            if not math.isclose(y_in, y_ans, rel_tol=REL_TOL, abs_tol=ABS_TOL):
                print("For x value %s: expected float value %f but found %f" % (str(x_ans), y_ans, y_in))
                return False
        elif y_ans != y_in: #answer is not a float
            #tested
            print(type(y_ans))
            print("For key %s: expected value %s but found %s" % (str(x_ans), str(y_ans), str(y_in)))
            return False
    return True

def verify_plot(df, qnum):
    if not 1 <= qnum <= 20:
        print("qnum is invalid")
        return False
    q_dict = read_dicts[qnum-1]
    if q_dict == {}:
        print("This question has no plot to verify")
        return False
    plot_type = q_dict['type']
    if plot_type == 'bar':
        x_name = q_dict['x_name']
        y_name = q_dict['y_name']
        try:
            input_dict = df_to_dict(df, x_name, y_name)
        except KeyError:
            print('Check your column names! Expected: %s, %s' %(x_name, y_name))
            return False
        answer_dict = df_to_dict(q_dict['df'], x_name, y_name)
        return verify_bar(input_dict, answer_dict)
    elif plot_type == 'scatter':
        x_name = q_dict['x_name']
        y_name = q_dict['y_name']
        try:
            input_list = df_to_xylist(df, x_name, y_name)
        except KeyError:
            print('Check your column names! Expected: %s, %s' %(x_name, y_name))
            return False
        answer_list = df_to_xylist(q_dict['df'], x_name, y_name)
        return verify_scatter(input_list, answer_list)
    elif plot_type == 'horizontal_bar':
        bool_list = []
        x_name = q_dict['x_name']
        for y_name in q_dict['y_name']:
            try:
                input_dict = df_to_dict(df, x_name, y_name)
            except KeyError:
                print('Check your column names! Expected: %s, %s' %(x_name, y_name))
                return False
            answer_dict = df_to_dict(q_dict['df'], x_name, y_name)
            bool_list.append(verify_bar(input_dict, answer_dict))
        return all(bool_list)
