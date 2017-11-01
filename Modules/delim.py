def get_grams(s,l):
    return [s[i:i+l] for i in range(len(s)-l)]

def possible_delim(L,th=0.9):
    """
    possible_delim - give repeted sequences in messages
    return a list of potential delimiters
    param L: list of raw messages
    param th (optional): frequency above which the sequence must appears in th messages (default 90%) 
    """
    R=[]
    for l in range(1,5):
        Lg=[get_grams(x,l) for x in L]
        ga=set()
        for lg in Lg:
            for x in lg:
                ga.add(x)
        for g in ga:    
            if sum([g in lg for lg in Lg])>th*len(L):
                R.append(g)
    return R

if __name__=="__main__":

    from netzob.all import *

    msgs=PCAPImporter.readFile('../S7-Pcap/10[C1D1].pcap').values()
    L=[x.data for x in msgs]
    print(possible_delim(L))
