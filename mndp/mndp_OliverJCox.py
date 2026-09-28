def calculate_Nesting_Depth(input_string :str) -> int:      # Specifying input and return types

    characters = [*input_string]    # Break string into list of characters
    acceptable_characters = ['-','*','/',')','(','+','0','1','2','3','4','5','6','7','8','9']

    max_nesting_depth = 0
    current_nesting_depth = 0

    for a in characters:

        '''Every time a open bracket is detected, add to current indent. Update max indent if 
        required. Reduce currrent indent when close bracket detected'''

        if a not in acceptable_characters or 1 >= len(characters) >= 100:
            print("Uneceptable character or input exceeds max length of 100 or less than 1")
            return
        elif a == '(':
            current_nesting_depth += 1
        elif a == ')':
            if current_nesting_depth > max_nesting_depth:
                max_nesting_depth = current_nesting_depth
                current_nesting_depth -= 1