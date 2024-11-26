def construct_lps(pat):
    l=len(pat)
    lps=[0]*l
    i=1
    m=0
    while i<l:
        if pat[i]==pat[m]:
            m+=1
            lps[i]=m
            i+=1
        else:
            if m!=0:
                m=lps[m-1]
            else:
                lps[i]=0
                i+=1
    
    return lps

def search(txt,pat):
    lps=construct_lps(pat)
    a=len(txt)
    b=len(pat)
    i=0
    j=0
    rec=[]
    while i<a:
        if txt[i]==pat[j]:
            i+=1
            j+=1
            if j==b:
               rec.append(i-j)
               j=lps[j-1]
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    print(rec)
    
if __name__=="__main__":
    txt=input("text= ")
    pat=input("enter pattern: ")
    search(txt,pat)