from netzob.all import *
from sklearn.cluster import dbscan
import math
import copy

def cluster(L,eps=100):
    """
    cluster - separate messages in differents cluster
    return a list of clusters containing the messages
    param: a list of raw data to be correlated
    param (optional): maximum distance between two samples

    note: if the length of the message are varying, the difference in lenght
    can outweight the similiarity in content
    """

    assert(type(L[0])==bytes)

    def eucl(vt,wt): 
        v,w=copy.copy(vt),copy.copy(wt)
        if len(v)>len(w): v,w=w,v
        v+=b'\x00'*(len(w)-len(v)) # equalization of the length
        x=math.sqrt(sum((x-y)**2 for x,y in zip(v,w)))
        return x

    # distance matrix
    n=len(L)
    M=[]
    for i in range(n):
        M.append([eucl(L[i],L[j]) for j in range(n)])

    # we use DBSCAN to do the actual clustering
    _,c=dbscan(M, metric='precomputed',eps=eps,min_samples=3)
   
    nc=max(c)
    if nc<2: raise ValueError('no clusters found. try to tune the parameters')
    r=[[]]*max(c)
    for ci in range(max(c)):
        for i in range(len(c)):
            if c[i]==ci:
                r[ci].append(L[i])

    return r
