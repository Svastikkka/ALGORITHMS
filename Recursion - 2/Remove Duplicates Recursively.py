# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string
    Hypo = removeConsecutiveDuplicates(string[1:])

    if string[0]== string[1]:
        return Hypo
    else:
        return  string[0]+Hypo



# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
