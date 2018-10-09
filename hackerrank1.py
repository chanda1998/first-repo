# split string into len/k subsegments each subsegment has n characters where n = len/k

string = "AABCAAADA"
string1 = "chandananjanjsbfvkhsbkwubohfvbwbvibuwbbvux" # len = 42
k = 3


def merge_the_tools(stri, k):
    n = int(len(stri)/k)        # n = 42/6 = 7
    lt = []
    for i in range(k):
        print(stri[i*n:i*n+n])      # n-k = 7-6 = 1  n*i = 7*0=0 7*1 = 7
        # lt.append(''.join(sorted(set(stri[n-k:n]), key=stri[n-k:n].index)))
        n += k






merge_the_tools(string1, 6)
