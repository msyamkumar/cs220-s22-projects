# Project 3 (P3) grading rubric

## Code reviews

- A TA / grader will be reviewing your code after the deadline.
- They will make deductions based on Rubric provided below.
- To ensure that you don't lose any points in code review, you must review the rubric and make sure that you have followed the instructions provided in the project correctly.

## Rubric

### General guidelines:
- Do not hardcode (-5 deduction per instance of hardcoding)
	- Don't hardcode and output the answer. You should show the working (code) for how you got the answer to a question. For example, if the index of Solar Energy is 5, you should find that index by calling `get_idx("Solar Energy")` and outputting that value instead of just outputting 5.
	- Do not hardcode indices (except for Q2 only; read Q2 for further details): For example, if we ask how much Wood Energy was consumed in 2020, you could obtain the answer with this code: `get_consumption(get_idx("Wood Energy"), 2020)`. Do not write code like this: `get_consumption(5, 2020)`
- If we have asked you to create and use a function for some questions, do not compute the answer without creating that function (-3 deduction per instance of not writing any of the following funcitons): 
	- year_max
	- energy_min
	- year_sum
	- change_per_year
	- find_threshold_year
	- find_overtake_year

### Question specific guidelines:
- Q4: Please use year_max to answer this question (-3 deduction if year_max is not used)
- Q6: Please use energy_min to answer this question (-3 deduction if energy_min is not used)
- Q8: Please use energy_avg to answer this question (-3 deduction if energy_avg is not used)
- Q11: Do not pass any arguments to `year_sum` function. Please make use of the default argument (-2 deduction if default argument is not utilized appropriately)
- Q13: Pass only one argument to `change_pear_year`. (-2 deduction if default argument is not utilized appropriately)
- Q14: Do not pass more than the minimum required number of arguments to get the correct answer (-2 deduction if default arguments are not utilized appropriately)
- `find_threshold_year`: Ensure that you have used previously defined functions such as, for example, change_per_year in the function body of find_threshold_year to calculate useful values to implement the find_threshold_year function. (-2 if change_pear_year is not used).
