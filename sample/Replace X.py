def replaceChar(s,a,b):
    if len(s)==0:
        return s
    Hypo=replaceChar(s[1:],a,b)
    if s[0]==a:
        return b+Hypo
    else:
        return s[0]+Hypo
print(replaceChar("abcdabcd","a","e"))
