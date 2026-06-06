# ==============================================================================
# RULE 1: HOW TO WRITE COMMENTS (Code that Python ignores)
# ==============================================================================

# This line starts with a '#' symbol. Python skips this line completely.
# Use this to write quick notes to yourself or explain a single line of code.

"""
These are triple quotes. They allow you to write a multi-line comment.
Everything inside these quotes will be ignored by Python.
Use this for long explanations, rules, or to describe a whole file.
"""

# ==============================================================================
# RULE 2: VARIABLE NAMING RULES (What is allowed and what isn't)
# ==============================================================================

# RULE: You must use lowercase letters and underscores (_) to separate words.
# This style guideline is officially called 'snake_case'.
student_age = 20  
total_score_count = 150

# RULE: Variables are case-sensitive. Python sees these as two different buckets!
items_count = 5   # This is bucket 1
Items_Count = 10  # This is bucket 2 (because of capital letters)

# RULE: You can start a variable with an underscore, which is common for advanced code.
_secure_key = "secret123"

# --- THE WRONG WAY (Will break your code) ---
# 1st_place = "John"  # WRONG: Cannot start with a number. Python gets confused.
# user-name = "Alex"  # WRONG: Hyphens are not allowed. Python thinks it means minus (-).
# class = "Math"      # WRONG: 'class' is a word Python already owns for its own logic.

# ==============================================================================
# RULE 3: INDENTATION AND SPACING RULES (The structure)
# ==============================================================================

# RULE: Every time you use a colon (:), it means a new block of code is starting.
# RULE: Every line inside that block MUST be pushed to the right by 4 spaces.

def calculate_discount(price):
    # This line has 4 spaces. It belongs to the function 'calculate_discount'.
    
    if price > 100:
        # This line has 8 spaces. It belongs to the 'if' statement.
        # It only runs if the price is greater than 100.
        final_price = price - 20
        print("Discount applied!")
        
    else:
        # This line has 8 spaces. It belongs to the 'else' statement.
        # It only runs if the price is 100 or less.
        final_price = price
        print("No discount available.")
        
    # This line goes back to 4 spaces. It means the if/else block is OVER.
    # But it is still inside the function.
    return final_price

# This line has 0 spaces. The function is completely OVER.
# This code runs normally from top to bottom.

# ==============================================================================
# RULE 4: GENERAL SYNTAX RULES
# ==============================================================================

# RULE: You do not need a semicolon (;) at the end of lines like in Java or C++.
# Just press Enter and start a new line. Python knows the line is done.
current_year = 2026 

# RULE: Strings (text) must be wrapped in matching quotes.
# You can use single quotes or double quotes, but do not mix them on the same line.
welcome_message = "Welcome to Python programming!" # Matching double quotes
goodbye_message = 'Goodbye for now!'               # Matching single quotes

# ==============================================================================
# RUNNING THE CODE
# ==============================================================================

# We call the function we made earlier and pass our price variable into it.
saved_price = calculate_discount(150)
print(saved_price) # This will print the final calculation to your screen
