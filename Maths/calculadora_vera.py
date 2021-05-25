expression = input("Enter the expression:\n")

filtered_expression = filter(lambda x: x not in "+-*/%", filter(lambda x: not x.isdigit(), expression))

if len(list(filtered_expression)) == 0:
    result = eval(expression)
    print(result)
else:
    raise ValueError("No words allowed!")
