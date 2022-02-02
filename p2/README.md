# Project 2 (P2)

## Clarifications/Corrections

**Find any issues?** Report to us:

- SAURABH KULKARNI <skulkarni27@wisc.edu>
- ZACHARY BAKLUND <baklund@wisc.edu>

## Learning Objectives

In this project you will demonstrate your ability to:
- Use arithmetic operators, including the *floor division* operator.
- Call the `type` function on an expression
- Use logical operators such as `and` and `or`.
- Use comparison operators.

## Overview

In this project, we will focus on types, operators, and boolean logic.  To start, create a `p2` directory, and download `main.ipynb`, `test.py` and `questions.py` to that directory. Make sure to follow the steps mentioned in the lab, which involves right-clicking the "Raw" button.

You will work on `main.ipynb` and hand it in. You **should not change** `test.py` or `questions.py`, and you **should not hand them in**.

After you've downloaded both files to `p2`, open a terminal window and use `cd` to navigate to that directory. To make sure you're in the correct directory in terminal, type `pwd`. To make sure you've downloaded the files, type `ls` ensure `main.ipynb`, `test.py` and `questions.py` are listed.

Now run the following command:

```
python test.py
```

You should see the following output:

```
Summary:
  Test 1: PASS
  Test 2: no Out[N] output found for cell
  Test 3: PASS
  Test 4: no Out[N] output found for cell
  Test 5: no Out[N] output found for cell
  Test 6: no Out[N] output found for cell
  Test 7: no Out[N] output found for cell
  Test 8: no Out[N] output found for cell
  Test 9: no Out[N] output found for cell
  Test 10: no Out[N] output found for cell
  Test 11: expected ':-(:-(:-(:-(:-(:-(:-(:-(:-(:-(:-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-)' but found ':-(:-(:-(:-(:-(:-):-)'
  Test 12: expected to find type int but found type str
  Test 13: no Out[N] output found for cell
  Test 14: no Out[N] output found for cell
  Test 15: no Out[N] output found for cell
  Test 16: expected True but found False
  Test 17: expected True but found False
  Test 18: expected False but found True
  Test 19: expected to find type bool but found type int
  Test 20: expected 50.0 but found -98.5

TOTAL SCORE: 10.00%
```

This means if you turn in `main.ipynb` now, you'll get 10% for your score. Pretty good for having done nothing yet, no?

You would get 10% because there are 20 problems, each worth 5%, and we have done problems 1 and 3 for you.  You can see this because the output above says "PASS" by them.  Your goal is to get more points by getting test.py to print "PASS" for more problems.  In some cases, you can see there is no answer in the original notebook (when it says `no outputs in an Out[N] cell`), and in other cases you need to make a change to correct a wrong answer (e.g., when it says `expected 50.0 but found -98.5`).

Now let's open a second terminal window in the p2 directory, then run `jupyter notebook` (or, if that doesn't work, try `python -m jupyter notebook`, or perhaps `python3 -m jupyter notebook`).  

Open up `main.ipynb`.  

Try solving the second question.  Then do a `Kernel` > `Restart & Run All`.  If that looks good, save your work, switch to your other terminal (where you previously ran the tests), and run the tests again.

Make sure you're scoring 15% before proceeding to the other questions. If it appears the test did not change from when you ran your tests in the notebook make sure to SAVE.

The instructions in `main.ipynb` will guide you from here. Once you're done, and `python test.py` says you're getting 100%, follow the submission instructions from P1 to submit.

Have fun, and run `python test.py` often to track your progress!

------------------------------

## IMPORTANT: Submission instructions
- Review [Grading Rubric](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p2/Rubric.MD), to ensure that you don't lose points during code review.
- Please remember to **`Kernel->Restart and Run All`** to check for errors, save your notebook, then run the **`test.py`** script one more time before submitting the project.
- Make sure that all the fields in the header cell are correctly populated, including **submitter** and **partner**.
- Follow the same steps as P1 to turn in main.ipynb to the course website. If required, review those steps.
- __If you are unable to solve a question and have partial code that is causing an error__ when running test.py, please __comment out the lines in the cell for that question.__ Failing to do so will cause the auto-grader to fail when you submit your file and give you 0 points even if you have some questions correctly answered.
- It is your responsibility to make sure that your project clears auto-grader tests on our testing system. 
	- Approximately 4 hours after you submit your program, auto-grader test results will become available. Make sure to use **View Submissions** to check the auto-grader test results.

------------------------------
