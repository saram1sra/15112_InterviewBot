
#took help from https://docs.python.org/2/library/json.html,
#https://www.ibm.com/watson/developercloud/personality-insights/api/v3/

import json
import requests


def callPersonalityInsights(text,savename):
        response = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile",
                auth=("cb1abd9d-b865-4389-9d6c-a1e5319d161f", "poJFIdFHGOQt"),
                headers = {"content-type": "text/plain"},
                data=text
                )
        test = json.loads(response.text)
        #print("##############################################################3", test)
        with open(savename +'.json', 'w') as outfile:
                json.dump(test, outfile, sort_keys = True, indent = 4,ensure_ascii=False)

msg = open("C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/testingFile.txt","r+")
MyText =msg.read()
dalpha = callPersonalityInsights(MyText, "candidate")
##Testing 
'''from WEBCRAWLER import *
from Comparison import *
from getData import *

#text = findJob("executive-director-cover-letter")
#othertext = findJob("youth-worker-cover-letter")
#print(text, othertext)
#alpha = callPersonalityInsights(text*4, "comparison")

import random 

final  =[]
d,e,f = getData("candidate.json")

for ele in [d[0],d[1], e]: 
        true = {}
        for k in ele :
                true[k]= ele[k]
                #print(true)
        final += [[true]]

parser = URLS()
titles,urls  = parser.getURLS('http://www.jobhero.com/sample-cover-letters/',"http://www.jobhero.com" ) 

i = titles.index('3d-artist-cover-letter')
i2 = titles.index('zookeeper-cover-letter')
titles = titles[i:i2+1]
textJobnames = []
z = random.choice(range(0,741))
print(z)
for i in titles[z:z+17] :
        print(i)
        txt = findJob(i)
        textJobnames += [txt]

#for i in titles [19 : 36] :
#        txt = findJob(i)
#        textJobnames += [txt]
#print(len(textJobnames))
def bestMatch(candidateData,startIndex, titles, jobnames):
    totalComp = []
    for i in range(len(titles) ):
        comparisons = 0
        jobname = jobnames[z+i]
        print(jobname)
        txt = findJob(jobname) 
        callPersonalityInsights(txt, jobname)
        a,b,c = getData(jobname+".json")
        admin = {}	
        things = []
        things = [a[0],a[1],b]
        #for k in [a[0],a[1],b] :
        #    #print(k)    
        #    for d in k :
        #        #print(d)
        #        admin[d] = k[d]
        #    things += [admin]
        #print(b)
        print(len(things))
        for ele in range(len(things)) :
            print(candidateData[ele])
            match,res = Comparing(candidateData[ele], things[ele])
            comparisons += res
           # print(ele) 
        totalAvg = comparisons/len(things)
        totalComp += [(jobname,totalAvg)]
    for element in totalComp :
         name,avg = element       
         if currAvg < avg : 
                betterJobs += [element]

        
    #for key in totalComparisons:
     
     #  for k in key :pass
    #pass
bestMatch(final, z, textJobnames, titles)'''