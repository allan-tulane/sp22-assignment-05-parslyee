
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    a, b = len(S), len(T)
    
    MED = [[0 for x in range(b+1)] for y in range(a+1)]
    
    for i in range(len(b+1):
        for j in range(len(a+1):
            if i == 0:
                MED[i][j] = j
            elif j == 0:
                MED[i][j] = i
            elif S[i-1] == T[j-1]:
                MED[i][j] = MED[i-1][j-1]
            else:
                MED[i][j] = 1 + min(MED[i][j-1], MED[i-1][j-1], MED[i-1][j])
    return MED[-1][-1]
    
    

def fast_align_MED(S, T, MED={}):
    a, b = len(S), len(T)
    
    MED = [[0 for x in range(b+1)] for y in range(a+1)]
    
    for i in range(len(b+1):
        for j in range(len(a+1):
            if i == 0:
                MED[i][j] = j
            elif j == 0:
                MED[i][j] = i
            elif S[i-1] == T[j-1]:
                MED[i][j] = MED[i-1][j-1]
            else:
                MED[i][j] = 1 + min(MED[i][j-1], MED[i-1][j-1], MED[i-1][j])
                       
                       
    insert = fast_MED(S, T[1:])
    delete = fast_MED(S[1:], T)
    substitute = fast_MED(S[1:], T[1:])                
    
    if len(S) == 0:
        SAlign = '-' * len(T)
        return SAlign, T
                       
    if len(T) == 0:
        TAligned = '-' * len(S)
        return S, TAlign

    if S[0] == T[0]:
        SAlign = (S[0]+ fast_align_MED(S[1:], T[1:])[0])
        TAlign = (T[0]+ fast_align_MED(S[1:], T[1:])[1])    
                       
    if min(insert, delete, substitute) == insert and insert != substitute:
        SAlign = ('-' + fast_align_MED(S, T[1:])[0])
        TAlign = (T[0] + fast_align_MED(S, T[1:])[1])
    
    if min(insert, delete, sub) == delete and delete != sub:
        SAlign = (S[0] + fast_align_MED(S[1:], T)[0])
        TAlign = ('-' + fast_align_MED(S[1:], T)[1])

    if min(insert, delete, sub) == sub: 
        SAlign = (S[0] + fast_align_MED(S[1:], T[1:])[0])
        TAlign = (T[0] + fast_align_MED(S[1:], T[1:])[1])
                       
    return SAlign, TAlign
                       
                       
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
