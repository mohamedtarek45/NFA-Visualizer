def parsing(regex):
    tokens = []
    operators = ["*", "|", "(", ")"]
    i = 0
    while i < len(regex):
        if regex[i] not in operators:
            tokens.append(regex[i])
            i += 1
        else:
            if regex[i] == "(":
                sub = []
                sub.append(regex[i])
                i += 1
                while i < len(regex) and regex[i] != ")":
                    if regex[i] == "(":
                        sub.append(regex[i])
                        i += 1
                        while i < len(regex) and regex[i] != ")":
                            sub.append(regex[i])
                            i += 1
                    sub.append(regex[i])
                    i += 1
                sub.append(regex[i])
                i += 1
                tokens.append(''.join(sub))
            elif regex[i] == "|":
                tokens.append(regex[i])
                i += 1
            elif regex[i] == "*":
                tokens[-1] = tokens[-1] + regex[i]
                i += 1
    if '|' in tokens:
        temp = ['','','']
        index = tokens.index('|')
        while '|' in tokens[index+1:]:
            index = tokens[index+1:].index('|') + index + 1
        temp[0] = ''.join(tokens[:index])
        temp[1] = '|'
        temp[-1] = ''.join(tokens[index+1:])
        tokens = temp
    return tokens