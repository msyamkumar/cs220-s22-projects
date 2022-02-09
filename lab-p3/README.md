# Lab 3: Learning an API

### Corrections/Clarifications

None yet

**Find any issues?** Report to us:

- Brian Huang <thuang273@wisc.edu>
- Lakshmi M. Nair <muraleedhara@wisc.edu>

------------------------------
## Learning Objectives

In this lab, you will practice...
* Writing functions with return statements
* Importing a module and using its functions
* Using parameters' default values when calling functions
* Avoiding hardcoding by using a `get_idx` funtion
* Working with the index of a row of data

------------------------------
## Note on Academic Misconduct

You may do these lab exercises with only with your project partner; you are not allowed to start working on lab3 with one person, then do the project with a different partner.  Now may be a good time to review [our course policies](https://www.msyamkumar.com/cs220/s22/syllabus.html).

------------------------------

## Project partner

We strongly recommend students to find a project partner. Pair programming is a great way to learn from a fellow student. Project difficulty level increases explonentially in this course. It is a good idea to find a project partner early on during the semester. 

If you are still looking for a project partner, take a moment now to ask around the room if anyone would like to partner with you on this project. Then you can work with them on this lab as well as the project. 

------------------------------
## Description

For many projects this semester, we'll provide you with a *module* (a collection of functions) named `project`, in a file named `project.py`. This module will provide functions that will help you complete the project. In the lab, we might introduce `lab.py`, which will be similar to (but not the same as) `project`.py

When using an unfamiliar module, the first thing you should do is study the module's *API*. API stands for "Application Programming Interface". 
Loosely defined, an API describes everything an application programmer (that's you) needs to know about piece of module in order to use it. Understanding the API will involve learning about each function and the arguments it takes, and what functions might need to be called before you can use other functions. 

There are two ways you can learn about an API. First, the person who created the API may have provided written directions, called *documentation*. Second, there are ways you can write code to learn about a collection of functions; this approach is called *inspection*.

------------------------------
## Segment 1: Setup

Create a `lab3` directory and download the following files into the `lab3` directory:

* `lab.csv`
* `madison.csv`
* `lab.py`
* `practice.ipynb`

Note: Remember that downloading files from github is tricky! You need to click on these files, right click on `Raw` then click `Save Link As`. Do *not* save the files as txt. If necessary, select the dropdown "All Files" and manually type the correct extension (such as .csv).  

If you accidentally downloaded the file as a `.txt` instead of `.csv`, you can execute `mv madison.txt madison.csv`. Recall that `mv` (move) command lets you rename a source file (first argument, example: madison.txt) to destination file (second argument, example: madison.csv).

Once you have downloaded the files, open a terminal and navigate to your `lab3` directory.  Run `ls` to make sure the three above files are available.

From the terminal, open a `jupyter notebook` session and open your `practice.ipynb`. For each task in the remaining segments, you will have corresponding input cells in `practice.ipynb`. Complete each task and come back to this github page to read further instructions.

------------------------------
## Segment 2: Defining your own functions and testing them. 
For each function, complete the provided starter code in `practice.ipynb` and run the cells that contain example function calls.
Follow the instructions in `practice.ipynb` to complete Segment 2. After finishing Segment 2 tasks, come back to this github page.

#### Task 2.1: Practice using `min()` and `max()`

#### Task 2.2: Write the function `get_avg_drop_lowest`.

#### Task 2.3: Write the function `get_avg_max_counts_twice` with 4 parameters.

#### Task 2.4: Write the function `get_range` with 4 parameters.

#### Task 2.5: Write the function `get_change_per_year`.

--------------------------------------------
## Segment 3: Inspecting `lab`.py

#### Task 3.1: Exploring `lab.py`
For each task, follow the directions provided in `practice.ipynb`. For some tasks, there will be a comment stating "If you want, you can check expected output in github page for lab-p3 (not required).". Come here if you want to verify your output (not required).

`dir(lab)` expected output:

```python
dir(lab)
['__DictReader',
 '__agency_to_id',
 '__builtins__',
 '__cached__',
 '__data',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'dump',
 'get_idx',
 'get_spending',
 'init']
```

`lab.dump()` invocation prior to `lab.init()` will produce the following error:

```python
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
----> 1 lab.dump()

     34     """prints all the data to the screen"""
     35     if __agency_to_id == None:
---> 36         raise Exception("you did not call init first")
     37 
     38     for agency in sorted(__agency_to_id.keys()):

Exception: you did not call init first
```

Expected output for `help(lab.init)`:

```python
Help on function init in module lab:

init(path)
    init(path) must be called to load data before other calls will work.  You should call it like this: init("madison.csv")
```

#### Task 3.2: Using `lab.py`

Expected output after running `lab.init("madison.csv")` and `lab.dump()`:

```
governments [ID 15]
  2017: $25.368880 MILLION
  2018: $28.228622 MILLION
  2019: $26.655754 MILLION
  2020: $27.798934 MILLION

gyms    [ID 6]
  2017: $49.737579 MILLION
  2018: $51.968340 MILLION
  2019: $53.144053 MILLION
  2020: $55.215007 MILLION

restaurants [ID 7]
  2017: $16.965434 MILLION
  2018: $18.125521 MILLION
  2019: $19.136348 MILLION
  2020: $19.845066 MILLION

schools [ID 3]
  2017: $68.063469 MILLION
  2018: $71.325756 MILLION
  2019: $73.247948 MILLION
  2020: $77.875535 MILLION

stores  [ID 122]
  2017: $18.371421 MILLION
  2018: $19.159243 MILLION
  2019: $19.316837 MILLION
  2020: $19.760710 MILLION
```

Now let's see what's inside `lab.csv`:

```python
lab.dump()
environments [ID 2]
  2017: $14.733000 MILLION
  2018: $12.060000 MILLION
  2019: $13.851000 MILLION
  2020: $15.765000 MILLION

libraries [ID 9]
  2017: $20.063469 MILLION
  2018: $21.325756 MILLION
  2019: $23.247948 MILLION
  2020: $27.875535 MILLION
```

Here is the `help` function output for `get_idx` and `get_spending` functions:

```python
help(lab.get_idx)
Help on function get_idx in module lab:

get_idx(agency)
    get_idx(agency) returns the ID of the specified agency.

help(lab.get_spending)
Help on function get_spending in module lab:

get_spending(agency_id, year=2018)
    get_spending(agency_id, year) returns the dollars spent (in millions) by the specified agency in specified year.
```

Expected outputs:

* `lab.get_idx("environments")` (looks up index of environments, which should be 2)
* Bad example, `lab.get_spending(2, 2020)` (looks up spending of environments with index 2 in 2020, which should be 15.765)
* `lab.get_spending(lab.get_idx("libraries"))` (looks up spending of libraries in 2018, the default year argument, which should be 21.32575615)

#### Task 3.3: Other Tasks
----------------------------------------------
## Segment 4: Analysing `madison.csv`

Complete the following tasks by following the directions in `practice.ipynb`

#### Task 4.1: what is the maximum/minimum spending in 2020 in `madison.csv`?

#### Task 4.2: what is the change rate of schools between 2017 and 2020 in `madison.csv`?

----------------------------------------------
## Project 3

Great, now you're ready to start [p3](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p3)!   Remember to only work with your partner from this lab on p3 from this point on.  Have fun!
