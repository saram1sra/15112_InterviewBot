from getData import *

def Comparing(candidate, comparison) :#comapring value of traits of comparison
    #data and candidate data.
    match = {}
    total = 0
    keys = []
    for key in comparison :
        keys += [key]
        #print(keys)
    for key in keys:
        if isinstance(candidate, list) : candidate = candidate[0]
        compValue = comparison[key][0]
        candValue = candidate[key][0]
        #print(key, compValue, candValue)
        valu = (1/compValue)*candValue*100
        total += valu
        match[key] = str(valu) + "%"
    avg = total/len(keys)    
    
    return(match, avg)
###################
##TestValues
########################    
'''a,b,c= getData("comparison.json")
z =a[0]
admin = {}
true = {}
#print(z)
for key in z :
    admin[key]= z[key]
#print(admin)
d,e,f = getData("candidate.json")
for k in d[0] :
    true[k]= d[0][k]
#print(true)    

#print(d["Openness"][0],a["Openness"][0] )
#print(comparisonpersonal[0], candidatepersonal[0])
#Comparing(admin,true)
#Comparing(candidateneeds, comparisonneeds)'''

