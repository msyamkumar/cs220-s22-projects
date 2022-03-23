# Lab-P8: Lists and Dictionaries

This lab is designed to help you prepare for p8. We will focus on dictionaries, mutating lists, binning, and copying.

------------------------------
## Corrections/Clarifications

**Find any issues?** Please report to us:

- Brian Husang <thuang273@wisc.edu>
- AARANYAK BHATTACHARYA <abhattacha25@wisc.edu>

------------------------------
## Learning Objectives

In this lab, you will practice how to...
* Integrate relevant information from various sources (e.g. multiple csv files)
* Build appropriate data structures for organization and informative presentation (e.g. list of dictionaries)
* Practice good coding style

------------------------------
## Note on Academic Misconduct

**IMPORTANT**: P8 and P9 are two parts of the same data analysis. You **cannot** switch project partners between these two projects. That is if you partner up with someone for P8, you have to sustain that partnership until end of P9. You must acknowledge to the lab TA to receive lab attendance credit.

You may do these lab exercises with only with your project partner; you are not allowed to start working on lab-p8 with one person, then do the project with a different partner.  Now may be a good time to review [our course policies](https://www.msyamkumar.com/cs220/s22/syllabus.html).

------------------------------
## Project partner

We strongly recommend students to find a project partner. If you are still looking for a project partner, take a moment now to ask around the room if anyone would like to partner with you on this project. Then you can work with them on this lab as well as the project.

------------------------------
## Introduction

In this project and the next, we will be working on the [IMDb Movies Dataset](https://www.imdb.com/interfaces/). We will use Python to discover some cool facts about our favorite movies, actors, and directors.

In this lab, you will combine the data from the `small_movies.csv` and `small_mapping.csv` files into a more useful format. Let's start by downloading the following files: `practice.ipynb`, `small_mapping.csv`, and `small_movies.csv`.

------------------------------
## Segment 1: Setup

Open `small_movies.csv` and `small_mapping.csv` in any spreadsheet viewer, and see what the data looks like. `small_movies.csv` has 7 columns: `title`, `year`, `genres`, `duration`, `directors`, `actors`, and `rating`.

When seen with a good spreadsheet viewer, this is what it will look like:

| title | year            | genres                      | duration | directors                                                           | actors                                       | rating |
| ----  |-----------------|-----------------------------|----------|---------------------------------------------------------------------|----------------------------------------------|--------| 
| tt3104988 | 2018  |  "Comedy, Drama, Romance" | 120  | nm0160840                                                           | "nm2090422, nm6525901, nm0000706, nm2110418, nm0523734" | 6.9 |
| tt4846340 | 2016  | "Biography, Drama, History"   | 127  | nm0577647                                                           | "nm0378245, nm0818055, nm1847117" | 7.8|

The `year` column refers to the year the movie was released in, `duration` refers to the duration of the movie (in minutes), `genres` refers to the genres that the movie belongs to, and `rating` refers to the IMDb rating of that movie. The weird alphanumeric sequences used for the columns `title`, `actors` and `directors` are the unique identifiers that IMDb uses for identifying either an actor or a director or a movie title. 

The IDs that begin with `tt` refer to a movie title, and the IDs that begin with `nm` refer to a person's name (either an actor or a director).

Next, open `small_mapping.csv` which has 2 columns: `id` and `name`, mapping these unique identifiers to their actual names.  Notice that each ID in `small_mapping.csv` appears in both files.  Take a moment to notice the connection between the IDs that appear in both files. Later in this lab, you will be reading `small_mapping.csv` into a dictionary.

```
tt3104988,Crazy Rich Asians
nm0160840,Jon M. Chu
nm2090422,Constance Wu
nm6525901,Henry Golding
nm0000706,Michelle Yeoh
nm2110418,Gemma Chan
nm0523734,Lisa Lu
tt4846340,Hidden Figures
nm0577647,Theodore Melfi
nm0378245,Taraji P. Henson
nm0818055,Octavia Spencer
nm1847117,Janelle Monáe
```

------------------------------
## Segment 2: Loading Data from CSV File
## Segment 3: Mapping IDs to Actual Names

For the remaining segments, detailed instructions are provided in practice.ipynb. From the terminal, open a jupyter notebook session, open your practice.ipynb, and follow the instructions in practice.ipynb.

------------------------------
## Project 8

Hopefully, this lab helped you get familiar with dictionaries! Now you're ready to start p8. If you have time left in lab, go ahead and start p8 now, so you can ask your lab TA questions. 
