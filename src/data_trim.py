#f=open("finalfile1234.txt","w")
import json
jw=open('newjson1234.json','w')
jw.write('[')
x=','
a=':'
y='"'
with open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\reviews_processed_electronics.json') as js:
    data = json.load(js)
    for r in data[:]:
            str1='{'+y+'reviewerID'+y+a+y+r['reviewerID']+y+x
            str2=y+'asin'+y+a+y+r['asin']+y+x
            str3=y+'reviewText'+y+a+y+r['reviewText']+y+'},'
            
            jw.write(str1+str2+str3)         
jw.write(']')
jw.close()
js.close()
        
    


