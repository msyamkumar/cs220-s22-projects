# Student Rubric for P7

## General deductions
-2 for every instance where they don't use the `cell()` function to access a value in vaccinations.csv (max deduction for 3+ violations: -5)  \
-5 for hardcoding answers. Max -5 per question.   
-4 for hardcoding indexes (max deduction for 3+ violations: -10)  \
-3 if they use any "advanced" stuff like pandas (the only modules that can be imported are `csv` and `datetime`)  \
-2 for each instance of not using a required function (max deductions for 6+ violations: -10)   \
Do not deduct from a question if it has already failed the autograder   

## Required functions and data structures:
```python
daily_vaccinations_on(date) # returns a dict
most_recent_total(col_name, date, covid_data) # returns a dict
vaccination_stats # a dict of dicts
```

## Q1
-5 if hardcoded.  
-2 if they don't use `cell()` to access column values  

## Q2
-5 if answer is hardcoded without working code.  
-2 if they don't use `cell()` to access column values

## Q3
-5 if answer is hardcoded without working code.  
-2 if they don't use `cell()` to access column values

## Q4
-5 if answer is hardcoded without working code.  
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/28/2022')  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `daily_vaccinations`)  \
-2 if they don't use `cell()` to access column values

## Q5
-5 if answer is hardcoded without working code.  
-4 if `daily_vaccinations_on` is not used  
-4 if `daily_vaccinations_on` is not created (deduct only once)

## Q6
-5 if answer is hardcoded without working code.   
-3 if they hardcode each of the dates instead of using Q1's answer  
-2 if they recreate date list instead of using a stored answer

## Q7
-5 if answer is hardcoded without working code.  
-3 if correct answer is obtained without using the `dict` from Q6.

## Q8
-5 if answer is hardcoded without working code.  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `daily_vaccinations`)

## Q9
-5 if answer is hardcoded without working code.  
-3 if they don't answer using `"people_fully_vaccinated"`

## Q10
-5 if answer is hardcoded without working code.  
-4 if `most_recent_total()` is not used   
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `people_fully_vaccinated`)  \
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/31/2022')

## Q11
-5 if answer is hardcoded without working code.  
-3 if they don't use the `dict` from Q10  
-3 if they don't use the populations `dict` from Q3  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `people_fully_vaccinated`)  \
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/31/2022')  

## vaccination_stats:
-5 if `vaccination_stats` is not created  
-3 if `most_recent_total()` is not used in the creation of `vaccination_stats`

## Q12
-5 if answer is hardcoded without working code.  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  

## Q13
-5 if answer is hardcoded without working code.  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  \

## Q14
-5 if answer is hardcoded without working code.  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  \

## Q15
-5 if answer is hardcoded without working code.  
-2 if they hardcode the country with max `population` without working code  
-2 if they don't get max population from `vaccination_stats` or the answer to Q3  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  \
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/29/2022')  

## Q16
-5 if answer is hardcoded without working code.  
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/31/2022')  
-3 if correct answer is obtained by using incorrect columns (that is, any column that is not `people_fully_vaccinated` or `people_vaccinated`)  

## Q17
-5 if answer is hardcoded without working code.  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  \
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/31/2022')  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `total_boosters`)  

## Q18
-5 if answer is hardcoded without working code.  
-2 if `vaccination_stats` is not used (deduct only if `vaccination_stats` was created)  \
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/25/2022')  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `total_boosters`)  

## Q19
-5 if answer is hardcoded without working code.  
-3 if correct answer is obtained by using incorrect date (that is, any date that is not '01/31/2022')  
-3 if correct answer is obtained by using incorrect column (that is, any column that is not `total_boosters`)  

## Q20
-5 if answer is hardcoded without working code.  
-3 if they use sort() or sorted()  \
-3 if they don't use the `dict` from Q19 OR `vaccination_stats`
