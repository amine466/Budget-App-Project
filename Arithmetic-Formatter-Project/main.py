def show_numb1(numb1, length):
    string = ""
    for i in range(len(numb1)):
        string = string + (length[i]-len(numb1[i]))*' ' + numb1[i] + '    '
    return string[:-4]

def show_numb2(numb2, length, operator):
    string = ""
    for i in range(len(numb2)):
        string = string + operator[i] + (length[i]-len(numb2[i])-1)*' ' + numb2[i] + '    '
    return string[:-4]

def show_slash(length):
    string = ""
    for i in range(len(length)):
        string = string + (length[i])*'-' + '    '
    return string[:-4]

def show_result(result, length):
    string = ""
    for i in range(len(result)):
        string = string + (length[i]-len(str(result[i])))*' ' + str(result[i]) + '    '
    return string[:-4]

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    numb1 = []
    numb2 = []
    length = []
    result = []
    operator = []
    for i in range(len(problems)):
        d = 0
        for j in range(len(problems[i])):
            if problems[i][j].isdigit():
                if d == 4:
                    return 'Error: Numbers cannot be more than four digits.'
                else: 
                    d += 1
            elif problems[i][j] == ' ':
                pass
            elif problems[i][j] == '+':
                if (problems[i][0:j-1].isdigit() and problems[i][j+2:].isdigit()):
                    d = 0
                    operator.append('+')
                    numb1.append(problems[i][0:j-1])
                    numb2.append(problems[i][j+2:])
                    result.append(int(numb1[i])+int(numb2[i]))
                else: 
                   return 'Error: Numbers must only contain digits.' 
            elif problems[i][j] == '-':
                if (problems[i][0:j-1].isdigit() and problems[i][j+2:].isdigit()):
                    d = 0
                    operator.append('-')
                    numb1.append(problems[i][0:j-1])
                    numb2.append(problems[i][j+2:])
                    result.append(int(numb1[i])-int(numb2[i]))
                else: 
                   return 'Error: Numbers must only contain digits.' 
            else:
                return "Error: Operator must be '+' or '-'."
        length.append(max(len(numb1[i]), len(numb2[i]))+2)
    if show_answers:
        return show_numb1(numb1, length) +"\n" + show_numb2(numb2, length, operator) +"\n" + show_slash(length) +"\n" + show_result(result, length)
    else:
        return show_numb1(numb1, length) +"\n" + show_numb2(numb2, length, operator) +"\n" + show_slash(length)

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
