import json
from textblob import TextBlob
import nltk
from collections import Counter
jd=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\dataset_asin-wise_final.json')
final=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\finalanswer.json','w')
data=json.load(jd)
final.write('[')
count=0
for x in data:
    final.write('{"asin":')
    final.write(json.dumps(x['asin']+','))
    final.write('"entities":[')
    for i in x['reviews']:
        wiki=TextBlob(i)
        namedent=nltk.ne_chunk(wiki.tags,binary=True)
        str1=''
        #print(wordcount)
        for x in namedent:
            strne=str(x)
            if('NE' in str1):
                str1+=strne+' '
                #final.write('"'+str1+'",')
        #count+=1
        str1=str1.upper()
        words=str1.split(' ')
        a={}
        for wordout in words:
            a['wordout']=0
        for wordout in words:
            for word in words:
                if(word==wordout):
                    a['wordout']+=1
                else:
                    a['wordout']=1
        print(a)            
    final.write(']')
    count+=1
    final.write('}')
    print('--------------------\n---------------\n')
    if(count>5):
        break
print(count)
final.write(']')
final.close()
jd.close()
        