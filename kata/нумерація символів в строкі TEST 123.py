def number(lines):
    count = 1
    line = []
    for x in lines:
        line.append(str(count) + ': ' + x)
        count += 1
    return line

