# Project 3 (P3) grading rubric

## Code reviews

- A TA / grader will be reviewing your code after the deadline.
- They will make deductions based on Rubric provided below.
- To ensure that you don't lose any points in code review, you must review the rubric and make sure that you have followed the instructions provided in the project correctly.

## Rubric

### General guidelines:
- Do not hardcode (-5 deduction per instance of hardcoding)
	- Don't hardcode and output the answer. You should show the working (code) for how you got the answer to a question. For example, if the index of Solar Energy is 5, you should find that index by calling `get_idx("Solar Energy")` and outputting that value instead of just typing in 5.
	- Do not hardcode indices. For example, if we ask how much Wood Energy was consumed in 2020, you should not pass arguments as (5, 2020). Instead of 5, you should use the appropriate function call to determine the ID from the name of the energy. The argument to the year parameter here is not considered as hardcoding. Any literal value in the question isn't considered as hardcoding. For example: "Wood Energy" and 2020 are literals that you can use.
	- In places where we explicitly state "you may hardcode some value", you are allowed to use those literals as such.
- If we have asked you to create and use a function for some questions, do not compute the answer without creating that function (-3 deduction per instance of not writing any of the following funcitons): 
	- year_max
	- energy_min
	- year_sum
	- change_per_year
	- find_threshold_year
	- find_overtake_year
- import statements not at the top of the notebook (-3 deduction per instance of incorrect placement)
	- all import statements must be part of a single cell at the top of the notebook file, right underneath the header cell with your indentification information.

### Question specific guidelines:
- Q4 & Q5: Please use year_max to answer these question (-3 deduction if year_max is not used)
- Q6 & Q7: Please use energy_min to answer this question (-3 deduction if energy_min is not used)
- Q8, Q9, & Q10: Please use energy_avg to answer this question (-3 deduction if energy_avg is not used)
- Q11: Do not pass any arguments to `year_sum` function. Please make use of the default value (-2 deduction if default value is not utilized appropriately)
- Q13: Pass only one argument to `change_pear_year`. (-2 deduction if default value is not utilized appropriately)
- Q14: Do not pass more than the minimum required number of arguments to get the correct answer (-2 deduction if default values are not utilized appropriately)
- `find_threshold_year`: must invoke `change_pear_year` function (-2 if change_pear_year is not used).
- `find_overtake_year`: must invoke `change_pear_year` function (-2 if change_pear_year is not used).
- Q20: For unit market share computation, you must invoke a function you previously defined (-2 if the appropriate function is not used).
