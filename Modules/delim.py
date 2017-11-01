def get_grams(s,l):
    return [s[i:i+l] for i in range(len(s)-l)]

def possible_delim(L,th=0.9):
    """
    possible_delim - give sequences in messages 
    return a list of potential delimiters, the first message they appear in and the pos in the message
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
            np=Lg[0].count(g)
            cnt=[lg.count(g)==np for lg in Lg]
            if np>0 and sum(cnt)>th*len(L):
                idx=cnt.index(True)
                pos=Lg[idx].index(g)
                R.append((g, idx, pos))
    return R

if __name__=="__main__":

    from netzob.all import *

    msgs=PCAPImporter.readFile('../S7-Pcap/Ws.pcap').values()
    L=[x.data for x in msgs]
    print(possible_delim(L))
