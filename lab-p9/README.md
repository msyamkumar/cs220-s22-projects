# Lab-P9: Plotting and Sorting

In this lab, you'll learn to create simple plots and take your sorting to the next level.  Have fun!

-----------------------------
## Corrections/Clarifications


**Find any issues?** Please report to us:

- Adil Ahmed <oahmed4@wisc.edu>
- Ishita Dhoot <idhoot@wisc.edu>

------------------------------
## Learning Objectives

In this lab, you will practice how to...
* Create simple plots from dictionaries
* Sort dictionaries by keys and values
* Use bucketizing to obtain useful data structures
* Use comprehensions to create lists and dictionaries

------------------------------
## Note on Academic Misconduct

IMPORTANT: P8 and P9 are two parts of the same data analysis. You cannot switch project partners between these two projects. If you partnered up with someone for P8, you have to sustain that partnership until the end of P9.

You may do these lab exercises only with your project partner. Now may be a good time to review our [course policies](https://www.msyamkumar.com/cs220/s22/syllabus.html).

------------------------------
## Segment 1: Setup

Create a `lab9` directory and download the `practice.ipynb` file into the directory.
### New packages

For this lab, you'll need to use two new packages: `matplotlib` and
`pandas`.  We'll eventually learn a lot about these, but for now you
just need to call some functions we provide.

**Note:** if you installed Anaconda as recommended  at the beginning of this class, these modules must have already been installed on your laptop. Run the first cell in the `practice.ipynb` notebook. If you don't see an error, the modules are already installed.
However, if you did not follow those instructions, you will need to install
these packages now. [Go to Package Installation section](#package-installation).

------------------------------
## Segments 2-6: Plotting and Sorting
For the remaining segments, detailed instructions are provided in `practice.ipynb`. From the terminal, open a `jupyter notebook` session, open your `practice.ipynb` and follow the instructions in `practice.ipynb`.

------------------------------

## Project Instructions

Copy the `plot_dict`, `median` and `year_to_decade` functions over to your project notebook.

Good luck for p9!

------------------------------

## Package Installation

**Note:** if you were able to successfully import `matplotlib` and `pandas` modules, you can **skip this optional section**.

`matplotlib`, `pandas` and many other Python packages are available on 
the [PyPI site](https://pypi.org/). 
`pip install` takes care of the details of going to PyPI and installing these 
packages for you.

Once you know the name of a Python package, installing it is easy.  You just
run the following in the terminal, substituting in the package name:

```
pip install ????
```

So in this case, you should run the following (in either the Mac
Terminal or Windows PowerShell):

```
pip install matplotlib
pip install pandas
```

You may see "Requirement already satisfied" messages (e.g., if you
already installed these by following the setup videos we provided at
the beginning of the semester), so don't be surprised if your output
looks something like this:

```
Requirement already satisfied: pandas in c:\users\ms\anaconda3\lib\site-packages (1.2.4)
Requirement already satisfied: pytz>=2017.3 in c:\users\ms\anaconda3\lib\site-packages (from pandas) (2021.1)
Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\ms\anaconda3\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: numpy>=1.16.5 in c:\users\ms\anaconda3\lib\site-packages (from pandas) (1.20.1)
Requirement already satisfied: six>=1.5 in c:\users\ms\anaconda3\lib\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)
```

Common issues:
* If you have both Python 2 and 3 installed, you may need to replace `pip` with `pip3`.
* If neither pip command is found, you may need to replace `pip` with `python -m pip` or `python3 -m pip`.  This just means pip, although installed, is not on the PATH (i.e., your computer doesn't know where to find it).
* If you run into any other error - ask your lab TA, visit office hours or post a screenshot of the error on Piazza.
