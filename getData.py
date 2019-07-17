import os
import json


def getData(filename) :
    with open('C:/Users/saram/Dropbox/Classes/Sem1/15112/TermProject/Test code/' + filename, 'r') as f:
     data = json.load(f)
    #get data from format of json file taken from WatsonAPIPersonality Insights
    returnPersonality,returnConsumer_Needs, returnValues = {},{},{}
    data = data["tree"]
    #personality dictionary
    val1= data["children"][0]
    val1 = val1["children"][0]
    personality = val1["children"]
    #consumer_needs dictionary
    val2 = data["children"][1]
    val2 = val2["children"][0]
    consumer_needs = val2["children"]
    #values dictionary
    val3 = data["children"][2]
    val3 = val3["children"][0]
    values =  val3["children"]
    #traits
    personality_traits = personaltyValues(personality)
    consumer_needs_traits = consumerNeedValues(consumer_needs)
    value_traits =  ValValues(values)   
    return (personality_traits,consumer_needs_traits,value_traits )
    
###########################################################################################################################################
#Helper Functions
###########################################################################################################################################
#formating mutlilayered dictionary to single dictionary 
def personaltyValues(d, i = 0, personal ={}, internal = {}) : 
    if len(d) == i : 
        return (personal,internal)
    else :
        personal[d[i]["name"]] = (d[i]["percentage"], d[i]["sampling_error"])
        z =internalPersonalityValues(d[i]["children"])
        internal = dict(internal.items() + z.items())
        return (personaltyValues(d,i+1,personal,internal))

def internalPersonalityValues(d, i =0, p ={}):
     if len(d) == i : return p
     else :
         p[d[i]["name"]] = (d[i]["percentage"], d[i]["sampling_error"])
         return (internalPersonalityValues(d,i+1,p))

def consumerNeedValues(d, i = 0, needs ={}) :
    if len(d) == i : return needs
    else :
        needs[d[i]["name"]] = (d[i]["percentage"], d[i]["sampling_error"])
        return (consumerNeedValues(d,i+1,needs))

def ValValues(d, i = 0, val ={}) :
    if len(d) == i : return val
    else :
        val[d[i]["name"]] = (d[i]["percentage"], d[i]["sampling_error"])
        return (ValValues(d,i+1,val))
################################################################################################################################################   
##Testing Values
#candperson, candneeds, candval = (getData("candidate.json"))
#comparisonpersonal, comparisonneeds,comparisonvalues= getData("comparison.json")
#f = candperson[0]
#print("1",f["Openness"])
#candperson, candneeds, candval = 
#a,b,c= getData("comparison.json")
#z =a[1]
#admin = {}
#true = {}
#print(z)
#for key in z :
 #   admin[key]= z[key]
#print(admin)
#d,e,f = getData("candidate.json")
#for k in d[0] :
#    true[k]= d[0][k]
#print(true)    
#print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",x)
#print(len(admin))

#Comparing(admin,true)
#personality, needs,values = getData("candidate.json")
#print(personality) 
#personalitycomp, needscomp,valuescomp = getData("candidate.json")
#print(personalitycomp)