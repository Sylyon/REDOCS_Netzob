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

def verifDelim(msgs):
    L=[x.data for x in msgs]
    D=possible_delim(L)
    for j in range(0,len(D)):
        print(D[j][0])
    Del=[]
    d=D[0]
    for d in D:
        ms=msgs[d[1]]
        for i in range(0,len(d[0])):
            ms=modifyMessageByte(ms, d[2]+i, 1)
        ms=modifyMessageByte(msgs[d[1]], d[2], 1)
        try:
            response = sendTCP_raw_single(ms, "157.136.198.69",102)
        except socket.timeout:
            #print("Socket timeout reached.")
            Del.append(d[0])
            pass
             
    return removeDouble(Del)
    
	

if __name__=="__main__":
    from modify import *
    from netzob.all import *
    from imitateValidTraffic import *
    from replayTraffic import *
    from removeDouble import *
    msgs=PCAPImporter.readFile('../S7-Pcaps/R1.pcap').values()
    D=verifDelim(msgs)
    print(D)


    for d in D:
        sym=Symbol(messages=msgs)
        Format.splitDelimiter(sym,Raw(d))
        print(sym)
        
