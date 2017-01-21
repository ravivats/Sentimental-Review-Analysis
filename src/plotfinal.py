import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
jd=open('dataset_asin-wise_final_testset1.json')
jm=open('finalanswer_test.json')
data=json.load(jd)
js =json.load(jm)
l=[]
m=[]
for x in data:
    l.append(x['mean_overall'])
   
print(l)
print(len(l))

for y in js:
    m.append((y['overall_sentiment']))
    
print(m)
print(len(m))
cov = np.cov(l, m)
lambda_, v = np.linalg.eig(cov)
lambda_ = np.sqrt(lambda_)


ax = plt.subplot(111, aspect='equal')
for j in range(0,4):
    ell = Ellipse(xy=(np.mean(l), np.mean(m)),
                  width=lambda_[0]*j*2, height=lambda_[1]*j*2,
                  angle=np.rad2deg(np.arccos(v[0, 0])))
    ell.set_facecolor('none')
    ax.add_artist(ell)
plt.xlim(0,6.5)
plt.ylim(-1,1)
plt.scatter(l, m)
plt.show()