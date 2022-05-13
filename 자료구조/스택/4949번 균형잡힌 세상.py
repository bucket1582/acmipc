def check_bracket_match(opening, closing):
    return (opening == "(" and closing == ")") or (opening == "[" and closing == "]")

def check_line_balanced(line):
    stack = list()
    for char in line:
        if (char == "(") or (char == "["):
            stack.append(char)
        elif (char == ")") or (char == "]"):
            if len(stack) == 0:
                return False
            last_bracket = stack.pop()
            match_flag = check_bracket_match(last_bracket, char)
            if not match_flag:
                return False
    if len(stack) != 0:
        return False
    return True
            

while True:
    line = input()
    if line == ".":
        break
    balance_flag = check_line_balanced(line)
    if balance_flag:
        print("yes")
    else:
        print("no")
    
