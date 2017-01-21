import json
js=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\reviews_processed_electronics.json','r')
jnew=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\dataset_asin-wise_final_testset1.json','w')
data=json.load(js)
jnew.write('[')
i=0
while(i<len(data)):     
    jnew.write('{"asin":'+json.dumps(data[i]['asin'])+',')
    jnew.write('"overall":[')
    asin=data[i]['asin']
    j=i
    mean=0
    c=0
    while(asin==data[j]['asin']):
        jnew.write(json.dumps(data[j]['overall'])+',')         
        mean+=(data[j]['overall'])
        c+=1
        j+=1
        if(j>=len(data)):
            break
    i=j
    mean/=c
    jnew.write('0.0],"mean_overall":'+str(mean)+'},')
    x=i
    if(x>=len(data)):
        break
jnew.write(']')    
jnew.close()
js.close()