import json
jd=open('C:\\Users\\ATIF ADIB\\Desktop\\xhackathon\\dataset_asin-wise.json')
data=json.loads(jd)
for x in data:
    print(x['asin'])
    l=len(x['reviews'])
    for i in range(0,l):
        print(x['reviews'][i])
        print("\n")