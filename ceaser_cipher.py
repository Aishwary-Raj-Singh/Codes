s="YHNYL WUGYLU JCFF ILCACHUF"
for rot in range(26):
    result = ""
    for x in s:
        if x == ' ':
            result = result + ' '
            continue
        y = ord(x) + rot
        if y > 90:
                y = y - 26
        result = result + chr(y)
    print(result)
