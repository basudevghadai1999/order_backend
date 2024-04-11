def calculate(expression, variables=None, default=1):
    if variables is None:
        variables = {}
    
    tokens = []
    current_token = ""
    for char in expression:
        if char.isalnum() or char == "_":
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    if current_token:
        tokens.append(current_token)

    for i in range(len(tokens)):
        if tokens[i].isalpha():
            tokens[i] = str(variables.get(tokens[i], default))

    evaluated_expression = "".join(tokens)
    result = eval(evaluated_expression, globals(), variables)
    return result

expression = "(5*(2-1)+(item2-2)*1-5+10)"
variables = None # {"item2": 3}  # Define variable values
result = calculate(expression, variables)
print(result)
