
def myfunc(line):
    crr = 0
    returning = ''
    for a in line:
        if crr % 2 == 0:
            returning = returning + a.upper()
            crr = crr + 1
        else:
            returning = returning + a.lower()
            crr = crr + 1
    return returning



if __name__ == '__main__':
    example = 'coagulantsmedicationsissneeded'
    result = myfunc(example)
    print(result)
