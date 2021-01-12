

import docx

ans = []
qns = []
newq=[]

tempa = []
tempb = []
tempc = []
tempd = []

a=[]
b=[]
c=[]
d=[]

  
def readfile(filename):
    doc = docx.Document(filename)
    qs = 0
    an = 0
    high=0
    low=0
    line=0


    for paragraph in doc.paragraphs:
        l = 0
        m = 0
        

        if ('(a)' in paragraph.text) or ('(b)' in paragraph.text) or ('(c)' in paragraph.text) or ('(d)' in paragraph.text):
            
            if(line==1):
                low=high
                for i in range(low-1,high):
                    newq.append(qns[i])
                    

            elif(line>1):
                st=""
                for i in range(low,high):
                    st+=qns[i]
                    low=low+1
                newq.append(st)
                low=high


            ans.append(''.join(paragraph.text).replace('\t',""))
            if(l==0 and an<=qs):
                an+=1
            #print('aa'+str(an))
            m+=1
            line=0

        else:
            line+=1
            high+=1
            qns.append(''.join(paragraph.text).replace('\t',""))
            if(m==0 and qs>=an):
                qs+=1
            #print(str('qq')+str(qs))
            l+=1
            an=0


def result(ans):
    for i in ans:
        if('(a)' in i):   
            tempa.append(i)
        elif('(c)' in i):
            tempc.append(i)
    for i in ans:
        if('(b)' in i):
            tempb.append(i)
        elif('(d)' in i):
            tempd.append(i)
        
    for x in tempa:
        x= x.split('(b)')[0]
        a.append(x)
    for x in tempb:
        x= x.split('(b)')[-1]
        b.append('(b)'+x)
    for x in tempc:
        x= x.split('(d)')[0]
        c.append(x) 
    for x in tempd:
        x= x.split('(d)')[-1]
        d.append('(d)'+x)
    

    for i in range(642):
        dic=[{i:{"Question":newq[i],"Answer":{"a":a[i],"b":b[i],"c":c[i],"d":d[i]}}}]
        print(dic)
    


readfile('Assignment1.docx')    #file path
result(ans)

