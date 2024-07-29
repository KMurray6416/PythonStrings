    # Task 1
first_str = input("What is your first name?")
last_str = input("what is your last name?")

def validate_input_length(first_str,last_str):
    if len(first_str) < 2 > len(last_str):
        print("!!ERROR!! Both names MUST have TWO or MORE characters in them.")
    elif len(first_str) >= 2 <= len(last_str):
        first_counter = 0
    for i in first_str:
        first_counter += 1
    last_counter = 0
    for j in last_str:
        last_counter += 1
    return(first_counter,
    last_counter)

print(validate_input_length(first_str,last_str))
