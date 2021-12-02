def openFile(path):
    with open(path) as fhand:
        lines=fhand.readlines()
    return lines

def puzzle1(arr):
    horizontal=0
    vertical=0
    for i in arr:
        if i.startswith('f'):
            horizontal+=int(i[-1])
        elif i.startswith('u'):
            vertical+=int(i[-1])
        else:
            vertical-=int(i[-1])
    return horizontal*abs(vertical)

def puzzle2(arr):
    horizontal=0
    vertical=0
    aim=0
    for i in arr:
        if i.startswith('f'):
            horizontal+=int(i[-1])
            if aim!=0:
                vertical+=int(i[-1])*aim

        elif i.startswith('u'):
            aim-=int(i[-1])
        else:
            aim+=int(i[-1])
    return horizontal*abs(vertical)


arr=[line.strip() for line in openFile('day2/input.txt')]

print(puzzle1(arr))
print(puzzle2(arr))