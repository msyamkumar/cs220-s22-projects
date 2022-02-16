# Project 4 (P4) grading rubric

## Code reviews

- A TA / grader will be reviewing your code after the deadline.
- They will make deductions based on Rubric provided below.
- To ensure that you don't lose any points in code review, you must review the rubric and make sure that you have followed the instructions provided in the project correctly.

## Rubric

### General guidelines:
- Do not hardcode (-5 deduction per instance of hardcoding)
	- Don't hardcode and output the answer. You should show the working (code) for how you got the answer to a question. For example, if the attack of Bulbasaur is 49, you should find that attack by calling `project.get_attack("Bulbasaur")` and outputting that value instead of just typing in 49.
- If we have asked you to create and use a function for some questions, do not compute the answer without creating that function (-3 deduction per instance of not writing any of the following functions): 
	- damage
	- type_bonus
	- effective_damage
	- num_hits
	- battle
	- luap_battle
- In some places, we have explicitly given directions for you to use a helper function that you defined in lab (-2 deduction per instance of not invoking the relevant function):
	- effective_damage function definition
	- luap_battle function definition
- import statements not at the top of the notebook (-3 deduction per instance of incorrect placement)
	- all import statements must be part of a single cell at the top of the notebook file, right underneath the header cell with your indentification information.
- Incorrect logic in a function/question (-3 to -1 deduction, depending on how wrong the logic used is):
	- for example, incorrectly ordered branches of a conditional or incorrectly ordered two different conditionals (ex: `battle` function definition)
- Wrong Pokémon is used in any of the questions even if the answer obtained is correct (-2 deduction per instance of incorrect Pokémon use).
- Do not define the same function more than once. There should only be one definition of each function. If some changes are required to be made to a function (for example, `battle` function is supposed to be changed (refer to paragraph after Q13)), edit the original function definition. (-1 deduction per duplicate function definition)
