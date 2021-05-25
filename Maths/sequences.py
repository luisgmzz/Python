import re


def sequence(general_term: str, term: int):
    # Yoy have to use operators in order the function to work correctly

    pattern = r"[A-Za-z]"
    filtered_string = filter(lambda x: not x.isdigit(), general_term)

    for i in filtered_string:
        if i != "n" and re.match(pattern, i):
            raise ValueError(
                "general_term can only contain numbers, operators or word n")

    actual_term = eval(general_term.replace("n", str(term)))
    return actual_term


print(sequence("2*n", 4))
