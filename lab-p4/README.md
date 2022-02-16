# Lab-P4: Conditional Statements and Pokémon API

In p4, you will be playing with some Pokémon and you will simulate simple Pokémon battles using conditional statements. In lab-p4, you will learn to use `project.py`, which you will need to complete p4. You will also be introduced to some simple conditional statements and 'helper functions' which will be useful for p4.

### Corrections/Clarifications

None yet

**Find any issues?** Report to us:

- Adil Ahmed <oahmed4@wisc.edu>
- Ishita Dhoot <idhoot@wisc.edu>
- Aaranyak Bhattacharya <abhattacha25@wisc.edu>

------------------------------
## Learning Objectives

In this lab, you will practice...
* Learning and using an 'API' (Application Programming Interface)
* Building 'helper' functions that can be used to create more advanced functions
* Writing conditions using if/elif/else statements
* Writing advanced conditions using nested if/else statements
* Writing advanced conditions using logical operators (or/and)

------------------------------
## Note on Academic Misconduct

You may do these lab exercises with only with your project partner; you are not allowed to start working on lab4 with one person, then do the project with a different partner.  Now may be a good time to review [our course policies](https://www.msyamkumar.com/cs220/s22/syllabus.html).

------------------------------

## Project partner

We strongly recommend students to find a project partner. Pair programming is a great way to learn from a fellow student. Project difficulty level increases exponentially in this course. It is a good idea to find a project partner early on during the semester.

If you are still looking for a project partner, take a moment now to ask around the room if anyone would like to partner with you on this project. Then you can work with them on this lab as well as the project.

------------------------------
## Segment 1: Setup

Create a `lab4` directory and download the following files into the `lab4` directory:

* `project.py`
* `pokemon_stats.csv`
* `type_effectiveness_stats.csv`
* `practice.ipynb`

If you found your `.csv` files are downloaded as `.txt` files (e.g. `pokemon_stats.txt` instead of `pokemon_stats.csv`), run `mv pokemon_stats.txt pokemon_stats.csv` from your Powershell/Terminal to change the extension of the file into `.csv` file manually. Here `mv` is a shell command to rename or move files. All the data that we need for p4 is stored in `pokemon_stats.csv` and `type_effectiveness_stats.csv`.

------------------------------
## Segment 2: Learning the API

For the remaining segments, detailed instructions are provided in `practice.ipynb`. From the terminal, open a `jupyter notebook` session, open your `practice.ipynb`, and follow the instructions in `practice.ipynb`. 

We will provide sample output in this README page, you can come here to verify your output, if needed.

### Task 2.1: Examine the Pokemon CSV file

### Task 2.2: Examine the Type Effectiveness stats CSV file

### Task 2.3: Explore the API

`help(project)` expected output:
```python
import project
help(project)

Help on module project:

NAME
    project

FUNCTIONS
    __init__()
        Automatically loads the data from 'pokemon_stats.csv' and 'type_effectiveness_stats.csv' when this module is imported.

    get_attack(pkmn)
        get_attack(pkmn) returns the Attack of the Pokémon with the name 'pkmn'

    get_defense(pkmn)
        get_defense(pkmn) returns the Defense of the Pokémon with the name 'pkmn'

    get_hp(pkmn)
        get_hp(pkmn) returns the HP of the Pokémon with the name 'pkmn'

    get_region(pkmn)
        get_region(pkmn) returns the region of the Pokémon with the name 'pkmn'

    get_sp_atk(pkmn)
        get_sp_atk(pkmn) returns the Special Attack of the Pokémon with the name 'pkmn'

    get_sp_def(pkmn)
        get_sp_def(pkmn) returns the Special Defense of the Pokémon with the name 'pkmn'

    get_speed(pkmn)
        get_speed(pkmn) returns the Speed of the Pokémon with the name 'pkmn'

    get_type1(pkmn)
        get_type1(pkmn) returns Type 1 of the Pokémon with the name 'pkmn'

    get_type2(pkmn)
        get_type2(pkmn) returns Type 2 of the Pokémon with the name 'pkmn'

    get_type_effectiveness(type1, type2)
        get_type_effectiveness(type1, type2) returns the effectiveness of type1 against type2

    print_stats(pkmn)
        print_stats(pkmn) prints all the statistics of the Pokémon with the name 'pkmn'

DATA
    __effectiveness__ = {'Bug': {'Bug': 1.0, 'Dark': 2.0, 'Dragon': 1.0, '...
    __pokemon__ = {'Abomasnow': {'Attack': 92, 'Defense': 75, 'HP': 90, 'N...

FILE
    c:\Users\ms\Documents\cs220\p4\project.py
```
------------------------------

## Segment 3: Conditional Statements

### Task 3.1: Explore the `project.get_region` function.

### Task 3.2: Explore the `project.get_hp` function.

### Task 3.3: Create a `compare_hp` function

### Task 3.4: Write a `compare_attack` function

------------------------------

## Segment 4: Advanced Conditional Statements

### Task 4.1: Count how many types a Pokémon has

### Task 4.2: Determine if two Pokémon have a matching type.

### Task 4.3: Debug your function

------------------------------

## Segment 5: Modifying Previous functions

### Task 5.1: Use Boolean operators to refactor `same_types`

### Task 5.3: Write the function `same_region`

### Task 5.3: Write the function `same_types_and_region`

### Task 5.4: Write a function that determines the stronger type

------------------------------

## Good Coding Style for Functions

When we are trying to design a function, we want to make sure that only the latest version for that function exists in our code. For example, in the previous section, we introduced an initial version of `same_types(pkmn1, pkmn2)`, where the conditional expressions needed some modifications. Do not duplicate the original function to fix the bug. Instead, modify the original directly and rerun the cell to update the definition. This way, there won't be multiple `same_types(pkmn1, pkmn2)` function definitions and that makes it easier to maintain your code.

You can now get started with [p4](https://github.com/msyamkumar/cs220-s22-projects/tree/main/p4). **You can use any helper function that you have created here in project p4.** Good luck and have fun!
