def mostFrequentLetter(s):
    s = s.lower()
    curletter=''
    curcounter=0
    maxletter=''
    maxcounter=0
    for i in range(len(s)):
        curcounter=0
        curletter=s[i]
#        print curletter
        for j in range(len(s)):
            if s[j]==curletter:
                curcounter+=1
        if curcounter > maxcounter:
            maxletter=curletter
            maxcounter=curcounter
#            print "change",maxletter,maxcounter
    return maxletter

print mostFrequentLetter('aabbbccd')

