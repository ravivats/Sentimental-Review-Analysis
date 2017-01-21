import json
from textblob import TextBlob
import nltk
from collections import Counter

jd=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\dataset_asin-wise_final.json')
final=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\finalanswer_test.json','w')
data=json.load(jd)
final.write('[')
for x in data:
    final.write('{"asin":')
    final.write(json.dumps(x['asin']))
    final.write(',')
    final.write('"entities":[')
    entitystring=''
    for review in x['reviews']:
        wiki=TextBlob(review)
        namedent=nltk.ne_chunk(wiki.tags,binary=True)
        for ent in namedent:
            strent=str(ent)
            if('NE' in strent):
                entitystring+=((str(ent[0][0]))+' ')
    entitystring=entitystring.upper()    
    entities=entitystring.split(' ')
    en_count=Counter(entities)
    en_obj=en_count.most_common(8)
    for i in range(0,len(en_obj)):
        wr='"'+en_obj[i][0]+'",'        
        final.write(wr)
    final.write('" "],"sentiment_entity":[')    
    for i in range(0,len(en_obj)):
        en_check=str(en_obj[i][0])
        lim=1.000000
        sum_sent=0.000000
        for r in x['reviews']:
            sent=TextBlob(r)
            if(en_check in r):
                sum_sent+=(sent.sentiment.polarity)
                lim+=1
        sum_sent/=lim       
        final.write(str(sum_sent)+',')
    final.write('0.0],')
    final.write('"overall_sentiment":')
    lim=0.0
    overalls=0.0
    for rev in x['reviews']:
        ovr=TextBlob(rev)
        overalls+=((ovr.sentiment.polarity)*len(rev)*(ovr.sentiment.subjectivity))
        lim+=(len(rev)*(ovr.sentiment.subjectivity))
    overalls/=lim
    final.write(str(overalls)+'},')
final.write(']')
final.close()
jd.close()
    
            