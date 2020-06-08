"""
1 b



"""


# Problem: Remove x from string
def replaceChar(s):
    if len(s) == 0:
        return s
    Hypo = replaceChar(s[1:])
    if s[0] == "x":
        return Hypo
    else:
        return s[0] + Hypo



# Main
string = input()
print(replaceChar(string))
